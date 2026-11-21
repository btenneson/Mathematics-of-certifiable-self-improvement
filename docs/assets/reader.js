// Private, same-origin full-document reader. Document bytes are fetched from docs/library.
const $=id=>document.getElementById(id);
const params=new URLSearchParams(location.search);
const id=Number(params.get('id'));
const article=(window.LIBRARY_CATALOG||[]).find(x=>x.id===id&&x.filetype==='PDF'&&x.available);
const status=$('reader-status'),canvas=$('reader-canvas'),stage=$('reader-stage');
const prev=$('prev'),next=$('next'),pageInput=$('page-input'),total=$('total-pages');
const zoomIn=$('zoom-in'),zoomOut=$('zoom-out'),fit=$('fit-width');
const original=$('open-original'),download=$('download-pdf');
let pdf=null,pageNumber=1,zoom=1,pdfjs=null,busy=false,pending=false,fitScale=1;
function notice(msg){status.textContent=msg;status.hidden=false}
function enable(){for(const b of [prev,next,pageInput,zoomIn,zoomOut,fit])b.disabled=false;updateNav()}
function updateNav(){if(!pdf)return;prev.disabled=pageNumber<=1;next.disabled=pageNumber>=pdf.numPages;pageInput.value=pageNumber;pageInput.max=pdf.numPages;total.textContent='of '+pdf.numPages}
function go(n){if(!pdf)return;pageNumber=Math.min(pdf.numPages,Math.max(1,Math.floor(Number(n)||1)));updateNav();render()}
async function render(){
 if(!pdf)return;
 if(busy){pending=true;return}
 busy=true;
 const current=pageNumber;
 try{
   const page=await pdf.getPage(current);
   const natural=page.getViewport({scale:1});
   const available=Math.max(280,stage.clientWidth-30);
   fitScale=Math.min(1.7,available/natural.width);
   const view=page.getViewport({scale:fitScale*zoom});
   const ratio=Math.min(window.devicePixelRatio||1,2);
   canvas.width=Math.floor(view.width*ratio);
   canvas.height=Math.floor(view.height*ratio);
   canvas.style.width=view.width+'px';
   canvas.style.height=view.height+'px';
   const ctx=canvas.getContext('2d',{alpha:false});
   ctx.setTransform(ratio,0,0,ratio,0,0);
   await page.render({canvasContext:ctx,viewport:view}).promise;
   canvas.hidden=false;
   status.hidden=true;
   canvas.setAttribute('aria-label','Page '+current+' of '+pdf.numPages);
   updateNav();
 }catch(e){notice('This page could not be rendered. Use Open original PDF to read it in your browser.');}
 finally{busy=false;if(pending){pending=false;render()}}
}
function fail(msg){notice(msg);for(const b of [prev,next,pageInput,zoomIn,zoomOut,fit])b.disabled=true}
async function main(){
 if(!article){fail('No available PDF matches this catalog entry. Return to All papers.');original.hidden=download.hidden=true;return}
 const url=new URL(article.link,location.href);
 const libraryBase=new URL('library/',location.href);
 if(url.origin!==location.origin||!url.pathname.startsWith(libraryBase.pathname)||!url.pathname.toLowerCase().endsWith('.pdf')){
  fail('The catalog PDF address failed the private-library safety check.');original.hidden=download.hidden=true;return
 }
 $('paper-title').textContent=article.title;
 $('paper-meta').textContent=(article.pages||'?')+' pages · Research rating '+article.quality.toFixed(1)+'/10 · AI improvement relevance '+article.relevance.toFixed(1)+'/10';
 document.title=article.title+' — Full PDF reader';
 original.href=url.href;
 download.href=url.href;
 download.download=url.pathname.split('/').pop();
 pageNumber=Math.max(1,Math.floor(Number(params.get('page'))||1));
 try{
  notice('Loading complete PDF reader…');
  // PDF.js executes locally in the browser; the requested manuscript is same-origin.
  pdfjs=await import('https://cdn.jsdelivr.net/npm/pdfjs-dist@6.5.438/build/pdf.mjs');
  pdfjs.GlobalWorkerOptions.workerSrc='https://cdn.jsdelivr.net/npm/pdfjs-dist@6.5.438/build/pdf.worker.mjs';
  notice('Loading document pages…');
  pdf=await pdfjs.getDocument({url:url.href,isEvalSupported:false}).promise;
  pageNumber=Math.min(pdf.numPages,pageNumber);
  enable();await render()
 }catch(e){fail('The enhanced reader could not start. Click Open original PDF to view the entire document in your browser.')}
}
prev.addEventListener('click',()=>go(pageNumber-1));
next.addEventListener('click',()=>go(pageNumber+1));
pageInput.addEventListener('change',()=>go(pageInput.value));
zoomIn.addEventListener('click',()=>{zoom=Math.min(3,zoom*1.2);render()});
zoomOut.addEventListener('click',()=>{zoom=Math.max(.4,zoom/1.2);render()});
fit.addEventListener('click',()=>{zoom=1;render()});
$('full-screen').addEventListener('click',async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen()}catch{}});
document.addEventListener('keydown',e=>{if(e.target instanceof HTMLInputElement||e.altKey||e.ctrlKey||e.metaKey)return;if(e.key==='ArrowRight')go(pageNumber+1);if(e.key==='ArrowLeft')go(pageNumber-1)});
let resizeTimer=0;addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>{if(pdf)render()},200)});
main();