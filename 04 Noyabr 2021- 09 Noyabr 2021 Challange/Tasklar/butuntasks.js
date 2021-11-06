
let telo=document.querySelector("body")
let txt=document.querySelector(".text")
let korobka=document.querySelector(".box2")
let txt2=document.querySelector(".text2")
var i=0;
var n=5;
var tekst=`I regard the brain as a computer which will stop working when its components fail. 
There is no heaven or afterlife for broken down computers; that is a fairy story for people afraid of the dark.`

//ucuncu task
function sozyazma(){
    if(i<tekst.length){
        txt2.innerHTML+=tekst.charAt(i);
        i++;
        setTimeout(sozyazma, 60);
    }
    else{
        txt2.innerHTML=''
        i=0
        if(i==0){
            sozyazma()
        }
    }
}
sozyazma()

//.....

 //birinci task 
function Reng(){
    let random = Math.floor(Math.random()*16777215).toString(16)  
    telo.style.background="#"+random
    txt.innerHTML="#"+random

} 

//...

//ikinci task

function Smile(){
korobka.style.display="flex"
}
function Close(){
korobka.style.display="none"
}

//...

