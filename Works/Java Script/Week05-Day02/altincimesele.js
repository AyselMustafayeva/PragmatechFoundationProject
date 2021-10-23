function birinci(){
    let a=0;
    for(let i=0;i<=100;i++){
        a+=i;
    }
    document.write(a)
}
function ikinci(){
    let ad = prompt("Adini dahil et : ");
    document.write(ad + " , Xow gelmisiz !")
}
let vibor=prompt("1 ya 2 daxil et : ");
if(vibor==1){
    birinci()
}
if(vibor==2){
    ikinci()
}
