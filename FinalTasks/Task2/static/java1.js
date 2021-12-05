var tekst=`Hi.I want to show you many insteresting facts and play game with you.




Do you want it too?`

let txt2=document.querySelector(".text2")
var knpk=document.querySelector("#knopka")
var i=0;


function mah(){
    window.addEventListener('click',function(event) {
        knpk.style.left=(event.clientX-knpk.clientWidth/2)+'px';
        knpk.style.top=(event.clientY-knpk.clientHeight/2)+'px';
})
}

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
mah()
