let array1=[]
let array2=[]
for(let i=0;i<5;i++){
    let a=prompt("birinci massivin elemntlerini dahil edin : ")
    array1.push(a)
}
for(let i=0;i<5;i++){
    let b=prompt("Ikinci massivin elemntlerini dahil edin : ")
    array2.push(b)
}
let array3=array1.concat(array2)
document.write(array3)