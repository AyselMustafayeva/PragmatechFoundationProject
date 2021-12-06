var tekst2=`So...My name is Bob.I'll be your friend for today, but before that, introduce yourself. `
let txt2=document.querySelector(".text2")
x=0;


function sozyazma2(){
    if(x<tekst2.length){
        txt2.innerHTML+=tekst2.charAt(x);
        x++;
        setTimeout(sozyazma2, 60);
    }
    else{
        txt2.innerHTML=''
        x=0
        if(x==0){
            sozyazma2()
        }
    }
}


sozyazma2()