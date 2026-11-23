// usage: node measure.js <url> <label> <profile desktop|mobile> <runs>
const {chromium}=require('playwright');
const [url,label,profile='desktop',runs='5']=process.argv.slice(2);
const med=a=>{a=[...a].sort((x,y)=>x-y);return a.length?a[Math.floor((a.length-1)/2)]:null}, pct=(a,p)=>{a=[...a].sort((x,y)=>x-y);return a[Math.min(a.length-1,Math.floor(p*a.length))]};
const mobile=profile==='mobile';
async function once(browser){
  const ctx=await browser.newContext(mobile?{viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true,userAgent:'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148'}:{viewport:{width:1280,height:800},deviceScaleFactor:1});
  const page=await ctx.newPage(); const cdp=await ctx.newCDPSession(page);
  await cdp.send('Network.enable'); await cdp.send('Performance.enable');
  if(mobile){await cdp.send('Emulation.setCPUThrottlingRate',{rate:4});
    await cdp.send('Network.emulateNetworkConditions',{offline:false,latency:150,downloadThroughput:1.6*1024*1024/8,uploadThroughput:750*1024/8});}
  const errs=[]; const pend=[];
  ctx.on('requestfinished',r=>{pend.push((async()=>{try{const sz=await r.sizes();const rs=await r.response();const tm=r.timing();return{url:r.url(),enc:sz.responseBodySize+sz.responseHeadersSize,status:rs&&rs.status(),type:r.resourceType(),s:tm.startTime,e:tm.startTime+tm.responseEnd}}catch(e){return null}})())});
  page.on('console',m=>{if(['error','warning'].includes(m.type()))errs.push(m.type()+': '+m.text().slice(0,160))});
  page.on('pageerror',e=>errs.push('pageerror: '+e.message.slice(0,160)));
  await page.addInitScript(()=>{window.__lt=[];window.__paint={};
    new PerformanceObserver(l=>l.getEntries().forEach(e=>window.__lt.push([e.startTime,e.duration]))).observe({type:'longtask',buffered:true});
    new PerformanceObserver(l=>l.getEntries().forEach(e=>{if(e.name==='first-contentful-paint')window.__paint.fcp=e.startTime})).observe({type:'paint',buffered:true});
    new PerformanceObserver(l=>{const e=l.getEntries().pop();window.__paint.lcp=e.startTime}).observe({type:'largest-contentful-paint',buffered:true});});
  await page.goto(url,{waitUntil:'commit'});
  // wait until map interactive: pin layers added, then until tiles idle
  const t={};
  await page.waitForFunction(()=>{try{if(!window.__r&&typeof ready!=='undefined'&&ready){window.__r=performance.now();}return !!window.__r}catch(e){return false}},null,{polling:10,timeout:90000});
  await page.waitForFunction(()=>{try{return map.loaded()&&map.areTilesLoaded()}catch(e){return false}},null,{polling:50,timeout:90000});
  await page.evaluate(()=>{window.__idle=performance.now()}); const nAtIdle=pend.length;
  const nav=await page.evaluate(()=>{const n=performance.getEntriesByType('navigation')[0];return{dcl:n.domContentLoadedEventEnd,load:n.loadEventEnd,ttfb:n.responseStart,ready:window.__r,idle:window.__idle,fcp:window.__paint.fcp,lcp:window.__paint.lcp,lt:window.__lt}});
  const m=Object.fromEntries((await cdp.send('Performance.getMetrics')).metrics.map(x=>[x.name,x.value]));
  const tbt=nav.lt.reduce((s,[,d])=>s+Math.max(0,d-50),0);
  // frame times
  const frames={};
  async function run(name,setup,step,n){
    await page.evaluate(setup); await page.waitForFunction(()=>map.loaded()&&map.areTilesLoaded(),null,{polling:50,timeout:90000});
    const r=await page.evaluate(([step,n])=>new Promise(res=>{const f=new Function('i','map',step);const d=[];let last=performance.now(),i=0;const lt0=window.__lt.length;
      (function tick(now){d.push(now-last);last=now;if(i>=n)return res({d:d.slice(2),lt:window.__lt.slice(lt0)});f(i++,map);requestAnimationFrame(tick)})(performance.now())}),[step,n]);
    const d=r.d;frames[name]={p50:med(d),p95:pct(d,.95),max:Math.max(...d),n:d.length,busy:r.lt.reduce((s,[,x])=>s+x,0),lts:r.lt.length};
  }
  const N=90;
  await run('pan-overview',()=>map.jumpTo({center:[-85.68,38.225],zoom:10.9}),'map.panBy([i%60<30?6:-6,2*(i%2?1:-1)],{animate:false})',N);
  await run('zoom-overview',()=>map.jumpTo({center:[-85.68,38.225],zoom:10.9}),'map.jumpTo({zoom:10.9+0.6*Math.abs(Math.sin(i/15))})',N);
  await run('pan-z13.5',()=>map.jumpTo({center:[-85.7585,38.2527],zoom:13.5}),'map.panBy([i%60<30?8:-8,2*(i%2?1:-1)],{animate:false})',N);
  await run('zoom-13-14',()=>map.jumpTo({center:[-85.7585,38.2527],zoom:13}),'map.jumpTo({zoom:13.5+0.5*Math.sin(i/12)})',N);
  const res=(await Promise.all(pend)).filter(Boolean);
  const host=u=>new URL(u).host;
  const out={nav,tbt,m,frames,errs,nAtIdle,
    reqs:res.map(r=>({u:r.url.length>110?r.url.slice(0,110):r.url,enc:r.enc,st:r.status,h:host(r.url),type:r.type,s:r.s,e:r.e}))};
  await ctx.close();return out;
}
(async()=>{
  const browser=await chromium.launch({args:['--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader','--ignore-gpu-blocklist']});
  const all=[];for(let i=0;i<+runs;i++){all.push(await once(browser));process.stderr.write('.')}
  await browser.close();
  const sum=(r,f)=>r.reqs.filter(f).reduce((s,x)=>s+x.enc,0);
  const col=(f)=>all.map(f);
  const S={label,profile,runs:all.length,
    fcp:med(col(r=>r.nav.fcp)),lcp:med(col(r=>r.nav.lcp)),dcl:med(col(r=>r.nav.dcl)),load:med(col(r=>r.nav.load)),
    pinsReady:med(col(r=>r.nav.ready)),mapIdle:med(col(r=>r.nav.idle)),tbt:med(col(r=>r.tbt)),
    scriptMs:med(col(r=>r.m.ScriptDuration*1000)),taskMs:med(col(r=>r.m.TaskDuration*1000)),layoutMs:med(col(r=>r.m.LayoutDuration*1000)),styleMs:med(col(r=>r.m.RecalcStyleDuration*1000)),heapMB:med(col(r=>r.m.JSHeapUsedSize/1048576)),
    nodes:med(col(r=>r.m.Nodes)),
    reqIdle:med(col(r=>r.nAtIdle)),bytesIdle:med(col(r=>r.reqs.slice(0,r.nAtIdle).reduce((s,x)=>s+x.enc,0))),bytesOwnIdle:med(col(r=>r.reqs.slice(0,r.nAtIdle).filter(x=>/localhost/.test(x.u)).reduce((s,x)=>s+x.enc,0))),
    reqCount:med(col(r=>r.reqs.length)),bytesTotal:med(col(r=>sum(r,()=>true))),bytesOwn:med(col(r=>sum(r,x=>/^(localhost|127)/.test(x.h)))),bytesExt:med(col(r=>sum(r,x=>!/^(localhost|127)/.test(x.h)))),
    frames:Object.fromEntries(Object.keys(all[0].frames).map(k=>[k,{p50:med(col(r=>r.frames[k].p50)),p95:med(col(r=>r.frames[k].p95)),max:med(col(r=>r.frames[k].max)),busy:med(col(r=>r.frames[k].busy)),lts:med(col(r=>r.frames[k].lts))}])),
    errs:[...new Set(all.flatMap(r=>r.errs))],reqsLast:all[all.length-1].reqs};
  require('fs').writeFileSync(`result-${label}-${profile}.json`,JSON.stringify(S,null,1));
  const f=x=>x==null?'-':Math.round(x*10)/10;
  console.log(`\n${label} [${profile}] runs=${S.runs} FCP ${f(S.fcp)} LCP ${f(S.lcp)} DCL ${f(S.dcl)} load ${f(S.load)} pinsReady ${f(S.pinsReady)} idle ${f(S.mapIdle)} TBT ${f(S.tbt)}`);
  console.log(`  initial load: ${S.reqIdle} requests, ${S.bytesIdle} B (own ${S.bytesOwnIdle}); after pan/zoom test: ${S.reqCount} requests`);
  console.log(`  reqs ${S.reqCount} bytes total ${S.bytesTotal} own ${S.bytesOwn} ext ${S.bytesExt}; script ${f(S.scriptMs)}ms task ${f(S.taskMs)}ms layout ${f(S.layoutMs)} style ${f(S.styleMs)} heap ${f(S.heapMB)}MB nodes ${S.nodes}`);
  for(const[k,v] of Object.entries(S.frames))console.log(`  ${k}: p50 ${f(v.p50)} p95 ${f(v.p95)} max ${f(v.max)} longtask-busy ${f(v.busy)}ms (${v.lts})`);
  console.log('  errs',S.errs);
})();
