let a=prompt("Sozu dahil edin : ")
let b =" "
let c=" "
for(let i=0;i<a.length;i++){
if(a[i]==a[i].toUpperCase()){
    b=a[i].toLowerCase()
    c+=b
}
if(a[i]==a[i].toLowerCase()){
    b=a[i].toUpperCase()
    c+=b
}
}
document.write(c)