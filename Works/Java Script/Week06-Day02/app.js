let box=document.querySelector('.box');
let elementWidth=box.clientWidth;
let leftPos=0;
let toppos=0;
function rengiDeyis(){
    box.style.background='black'
}

function olcunuDeyis(){
    box.style.width='900px'
}

function hereketEletdir(){
    box.style.left='200px'
}

function yoxOlsun(){
    box.style.opacity='0'
}
function geriGelsin(){
    box.style.opacity='1'
}

function daimiHereketEle(){
    box.style.left=`${leftPos}px`
    leftPos+=1;
    if(leftPos>(window.innerWidth-elementWidth)){
        clearInterval(interval)
    }
    console.log(`letfPos=${leftPos}`)
}
function awaqi(){
    let interval2=setInterval(awaqi,1)
    box.style.top=`${toppos}px`
    toppos+=1;
    if(toppos>(window.innerHeight-elementHeight)){
        clearInterval(interval2)
    }
    console.log(`toppos=${toppos}`)
}

let interval=setInterval(daimiHereketEle,1)
