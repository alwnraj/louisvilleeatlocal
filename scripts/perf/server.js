// Production-like static server: brotli/gzip (precompressed, like Vercel), ETag/304, headers from vercel.json.
const http=require('http'),fs=require('fs'),path=require('path'),zlib=require('zlib'),crypto=require('crypto');
const root=path.resolve(process.argv[2]), port=+process.argv[3]||8080;
const vj=JSON.parse(fs.readFileSync(path.join(root,'vercel.json'),'utf8'));
const rules=(vj.headers||[]).map(h=>({re:new RegExp('^'+h.source.replace(/:\w+/g,'[^/]+').replace(/\.(?!\*)/g,'\\.')+'$'),h:h.headers}));
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json','.woff2':'font/woff2','.png':'image/png','.pbf':'application/x-protobuf','.svg':'image/svg+xml'};
const compressible=/\.(html|js|css|json|svg|pbf)$/; const cache=new Map();
function load(f){const st=fs.statSync(f); const c=cache.get(f); if(c&&c.m===st.mtimeMs) return c;
 const raw=fs.readFileSync(f); const o={m:st.mtimeMs,raw,etag:'"'+crypto.createHash('md5').update(raw).digest('hex').slice(0,16)+'"'};
 if(compressible.test(f)){o.br=zlib.brotliCompressSync(raw,{params:{[zlib.constants.BROTLI_PARAM_QUALITY]:11,[zlib.constants.BROTLI_PARAM_SIZE_HINT]:raw.length}});o.gz=zlib.gzipSync(raw,{level:9});}
 cache.set(f,o);return o;}
http.createServer((req,res)=>{
 let p=decodeURIComponent(req.url.split('?')[0]); if(p.endsWith('/'))p+='index.html';
 const f=path.join(root,p); if(!f.startsWith(root)||!fs.existsSync(f)||!fs.statSync(f).isFile()){res.writeHead(404);return res.end('nf');}
 const o=load(f), ext=path.extname(f), ae=req.headers['accept-encoding']||'';
 const hd={'Content-Type':types[ext]||'application/octet-stream','ETag':o.etag,'Vary':'Accept-Encoding','Cache-Control':'public, max-age=0, must-revalidate'};
 for(const r of rules) if(r.re.test(p)) for(const h of r.h) hd[h.key]=h.value;
 if(req.headers['if-none-match']===o.etag){res.writeHead(304,hd);return res.end();}
 let body=o.raw; if(o.br&&/\bbr\b/.test(ae)){hd['Content-Encoding']='br';body=o.br}else if(o.gz&&/gzip/.test(ae)){hd['Content-Encoding']='gzip';body=o.gz}
 hd['Content-Length']=body.length; res.writeHead(200,hd); res.end(body);
}).listen(port,()=>console.log('serving',root,port));
