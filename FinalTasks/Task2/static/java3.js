var tekst3=`Please enter the name of the capital
 of a certain country and I will tell 
 you an interesting and slightly frightening fact about it.`
 
let txt5=document.querySelector(".text5")
n=0;


function sozyazma3(){
    if(n<tekst3.length){
        txt5.innerHTML+=tekst3.charAt(n);
        n++;
        setTimeout(sozyazma3, 60);
    }
    else{
        txt5.innerHTML=''
        n=0
        if(n==0){
            sozyazma3()
        }
    }
}


sozyazma3()