let a=prompt("Yaşını daxil et : ")
let b=Number(a)
if (a<=0 || a>=100){
    document.write("Düzgün məlumat daxil etməmisiniz")
}
else{
    if(b<30){
        document.write(b*b)
    }
    if(b>=30 && b<=40){
        document.write(b%10)
    }
    if(b>40){
        document.write("Mawallah")
    }
}