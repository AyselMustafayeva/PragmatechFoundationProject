let maaw =[500,550,300,400,700,1200,4000];
let maaw2=[];
let bonus=[];
for(let i=0;i<maaw.length;i++){
    if(maaw[i]<600){
        maaw2.push(maaw[i])
    }
}
for(let n=0;n<maaw2.length;n++){
bonus.push(((maaw2[n]*15)/100)+maaw2[n])
}
console.log(bonus)