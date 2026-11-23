const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({args:['--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader','--ignore-gpu-blocklist']});
 const views=[['overview',[-85.68,38.225],10.9],['z9.5',[-85.7,38.2],9.5],['z13.5',[-85.7585,38.2527],13.5],['z16',[-85.7585,38.2527],16]];
 for(const [name,url] of [['base','http://localhost:8081/'],['new',process.argv[2]]]){
  const page=await (await b.newContext({viewport:{width:1280,height:800},deviceScaleFactor:1})).newPage();
  await page.goto(url); await page.waitForFunction(()=>{try{return ready&&map.loaded()}catch(e){return false}},null,{timeout:60000});
  for(const [v,c,z] of views){ await page.evaluate(([c,z])=>map.jumpTo({center:c,zoom:z}),[c,z]); await page.waitForTimeout(300); await page.waitForFunction(()=>map.loaded()&&map.areTilesLoaded(),null,{timeout:60000}); await page.waitForTimeout(400); await page.screenshot({path:`vd-${name}-${v}.png`}); }
 }
 await b.close();
})();
