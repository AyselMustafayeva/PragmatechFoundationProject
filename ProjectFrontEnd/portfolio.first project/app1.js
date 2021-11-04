let box=document.querySelector('.mycontacts')
let box2=document.querySelector('.griddi')
let box4=document.querySelector('.kvadratiki')
let box31=document.querySelectorAll('.griddi li')[0]
let box32=document.querySelectorAll('.griddi li')[1]
let box33=document.querySelectorAll('.griddi li')[2]
let box5=document.querySelector('.kvadratiki2')
let box6=document.querySelector('.kvadratiki3')
let pr0 =document.querySelectorAll('.classfirststep1')[0]
let pr1 =document.querySelectorAll('.classfirststep1')[1]
let pr2 =document.querySelectorAll('.classfirststep1')[2]
let pr3 =document.querySelectorAll('.classfirststep1')[3]
let pr4 =document.querySelectorAll('.classfirststep1')[4]
let pr5 =document.querySelectorAll('.classfirststep1')[5]
let pr01 =document.querySelectorAll('.classfirststep2')[0]
let pr11 =document.querySelectorAll('.classfirststep2')[1]
let pr21 =document.querySelectorAll('.classfirststep2')[2]
let pr31 =document.querySelectorAll('.classfirststep2')[3]
let pr41 =document.querySelectorAll('.classfirststep2')[4]
let pr51 =document.querySelectorAll('.classfirststep2')[5]
let kv1=document.querySelectorAll('.kvadrat')[0]
let kv2=document.querySelectorAll('.kvadrat')[1]
let kv3=document.querySelectorAll('.kvadrat')[2]
let kv4=document.querySelectorAll('.kvadrat')[3]
let kv5=document.querySelectorAll('.kvadrat')[4]
let kv6=document.querySelectorAll('.kvadrat')[5]
let kvbolwe=document.querySelectorAll('.kvadratbolwe')
let kvliniya=document.querySelectorAll('.kvaliniya')
let heigtt=2
function itmek(){
  box.style.opacity='0'
}
function gelmek(){
  box2.style.opacity='1'
  box2.style.top='-190px'
  box31.style.display='block'
  box32.style.display='block'
  box33.style.display='block'
}

function Accordion(elem){
 setInterval(itmek,1000)
 setInterval(gelmek,3000)
}





function project1(){
  pr01.style.display='none'
pr0.style.display='none'
kv1.style.display='block'
}

function project2(){
  kv2.style.display='block'
  pr11.style.display='none'
  pr1.style.display='none'
}
function project3(){
  kv3.style.display='block'
  pr21.style.display='none'
  pr2.style.display='none'
}
function project4(){
  kv4.style.display='block'
  pr31.style.display='none'
  pr3.style.display='none'
}
function project5(){
  kv5.style.display='block'
  pr41.style.display='none'
  pr4.style.display='none'
}
function project6(){
  kv6.style.display='block'
  pr51.style.display='none'
  pr5.style.display='none'
}
function back1(){
  kv1.style.display='none'
  pr0.style.display='block'
  pr0.style.backgroundImage = "url('img/qalka3.png')"
  pr01.style.display='block'
}
function back2(){
  kv2.style.display='none'
  pr1.style.display='block'
  pr1.style.backgroundImage = "url('img/qalka3.png')"
  pr11.style.display='block'
  
}
function back3(){
  kv3.style.display='none'
  pr21.style.display='block'
  pr2.style.display='block'
  pr2.style.backgroundImage = "url('img/qalka3.png')"
}
function back4(){
  kv4.style.display='none'
  pr31.style.display='block'
  pr3.style.display='block'
  pr3.style.backgroundImage = "url('img/qalka3.png')"
}
function back5(){
  kv5.style.display='none'
  pr41.style.display='block'
  pr4.style.display='block'
  pr4.style.backgroundImage = "url('img/qalka3.png')"
}
function back6(){
  kv6.style.display='none'
  pr51.style.display='block'
  pr5.style.display='block'
  pr5.style.backgroundImage = "url('img/qalka3.png')"
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



