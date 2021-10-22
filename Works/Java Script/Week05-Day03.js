let a=prompt("Ededi dahil edin : ");
let b=Number(a);
let c=String(a);
function kvadrat(){
    console.log(b*b)
}
function metn(){
    console.log(c+ " bu bir sozdur")
}
if(a==b){
    console.log(typeof(b))
    kvadrat()
}
else{
    console.log(typeof(c))
    metn()
}