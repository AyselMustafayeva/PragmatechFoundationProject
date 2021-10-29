let box=document.querySelector('.classfirststep2ikinci');
let box2=document.querySelector('.classfirststep1ikinci');
function project(){
     box.style.bottom='250px'
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