let ad =["Aysel","Seyyad","Senan","Huseyn","Mehdi","Murad"];
let soyad=["Mustafayeva","Omerov","Mansurov","Ehmedov","Ceferov","Qafarli"];
let yaw=["21","19","22","20","17","18"];
let array1=[];
let indexx=0;
let a=0;
    for(let i=0;i<ad.length;i++)
    {   
    array1.push( "Telebe0"+(i+1)+" : "+ad[i]+" "+soyad[i]+" "+yaw[i] );
}
function bizimhaqda(){
    console.log(array1[indexx])
    indexx++ 
}
setInterval(bizimhaqda,3000);





