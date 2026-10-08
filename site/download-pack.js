'use strict';
const button=document.getElementById('download-pack');
const status=document.getElementById('download-status');
button.addEventListener('click',async()=>{
  button.disabled=true;
  try{
    status.textContent='Preparing the complete pack…';
    const response=await fetch('downloads/manifest.json');
    if(!response.ok)throw new Error('Download information is unavailable.');
    const manifest=await response.json(),parts=[];
    let received=0;
    for(const part of manifest.parts){
      const response=await fetch(part.url);
      if(!response.ok)throw new Error('The download was interrupted. Please try again.');
      const bytes=await response.arrayBuffer();
      if(bytes.byteLength!==part.bytes)throw new Error('A download part was incomplete. Please try again.');
      if(crypto.subtle){
        const digest=await crypto.subtle.digest('SHA-256',bytes);
        const actual=Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');
        if(actual!==part.sha256)throw new Error('A download part could not be verified. Please try again.');
      }
      parts.push(bytes);received+=bytes.byteLength;
      status.textContent='Downloading pack… '+Math.round(received/manifest.bytes*100)+'%';
    }
    const blob=new Blob(parts,{type:'application/zip'});
    if(blob.size!==manifest.bytes)throw new Error('The pack is incomplete. Please try again.');
    const url=URL.createObjectURL(blob),link=document.createElement('a');
    link.href=url;link.download=manifest.filename;document.body.append(link);link.click();link.remove();
    setTimeout(()=>URL.revokeObjectURL(url),60000);
    status.textContent='Pack ready. Find the ZIP in your downloads, then extract it.';
  }catch(error){status.textContent=error.message;}
  finally{button.disabled=false;}
});
