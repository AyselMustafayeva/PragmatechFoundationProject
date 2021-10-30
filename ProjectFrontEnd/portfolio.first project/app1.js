let box=document.querySelector('.mycontacts')
let box2=document.querySelector('.griddi')
let box4=document.querySelector('.kvadratiki')
let box31=document.querySelectorAll('.griddi li')[0]
let box32=document.querySelectorAll('.griddi li')[1]
let box33=document.querySelectorAll('.griddi li')[2]
let box5=document.querySelector('.kvadratiki2')
let box6=document.querySelector('.kvadratiki3')
function Accordion(elem){
 box.style.display='none'
 box2.style.display='grid'
}
function contact(){
  box31.style.display='none'
  box4.innerHTML='+994553819027'
  box2.style.top='120px'
}
 function contact2(){
  box32.style.display='none'
  box5.innerHTML='ayselmustafayeva25@gmail.com'
  box33.style.top='65px'
  
 }
  
 function contact3(){
  box33.style.display='none'
  box6.innerHTML='My telegram'
 }

   



function vaxt(){
    const a=new Date();
var hour=a.getHours()
var minute=a.getMinutes()
var second=a.getSeconds()
var millisecon=a.getUTCMilliseconds()
document.querySelector('.ulvaxt').innerHTML=`${hour}:${minute}:${second}:${millisecon}`;
}
setInterval(vaxt,1)