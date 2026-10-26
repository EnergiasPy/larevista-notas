function rot5(box,bi){if(box.dataset.rot)return;box.dataset.rot=1;
    var it=[].slice.call(box.querySelectorAll(':scope>.r5i')),hold=false,row=box.parentNode;
    var dw=box.querySelector('.dots5');if(dw)dw.style.display='none';
    function key(x){var im=x.querySelector('img');return (im&&im.getAttribute('src'))||x.textContent;}
    function taken(){var t={};[].forEach.call(row.children,function(b){if(b===box||!b.classList||!b.classList.contains('r5'))return;var o=b.querySelector(':scope>.r5i.on');if(o)t[key(o)]=1;});return t;}
    function pick(){var t=taken(),cur=box.querySelector(':scope>.r5i.on'),c=it.filter(function(x){return x!==cur&&!t[key(x)];});if(!c.length)c=it.filter(function(x){return x!==cur;});return c.length?c[Math.floor(Math.random()*c.length)]:cur;}
    function show(x){it.forEach(function(y){y.classList.toggle('on',y===x);});}
    show(pick()||it[0]); if(it.length<2)return;
    box.addEventListener('mouseenter',function(){hold=true;});box.addEventListener('mouseleave',function(){hold=false;});
    setTimeout(function(){setInterval(function(){if(hold||document.hidden)return;show(pick());},4000+Math.floor(Math.random()*2500));},(bi%4)*900+Math.floor(Math.random()*1500));
  }
