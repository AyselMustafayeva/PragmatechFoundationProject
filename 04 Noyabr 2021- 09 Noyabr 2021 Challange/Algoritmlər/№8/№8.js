
function toplamaq(a,b){
    console.log(a+b)
}
//dedim bawqa bir nesede yazim , stepen demekdi bir reqem ozune ikinci parametr geder vurulacaq , meselen (2,3)=2*2*2
function stepen(a,b){
    let d=1
    for(let i=0;i<b;i++){
        d=d*a
    }
    console.log(d)
}

stepen(-2,6)