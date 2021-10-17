let a=prompt('Ədədi daxil edin: ');
let b=(a%10);
let c=(a%100-b)/10;
let d=(a%1000-(c*10)-b)/100;
let e=(a%10000-(d*100)-(c*10)-b)/1000;
if(b%2!=0){
    document.write(b +" , ")
}
if(c%2!=0){
    document.write(c +" , ") 
}
if(d%2!=0){
    document.write(d +" , ")
}
if(e%2!=0){
    document.write(e)
}
