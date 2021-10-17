let a=prompt('Ədədi daxil edin: ');
let b=(a%10);
let c=(a%100-b)/10;
let d=(a%1000-(c*10)-b)/100;
let e=(a%10000-(d*100)-(c*10)-b)/1000;
let sum=b+c+d+e;
document.write(sum)