let str=`Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır `
let probel=0;
let zapatoy=0;
let cislo=0;
let vtoroyecislo=0;
let sait=["ə","i","ö","ü","e","a","ı","o","u"];
let a=0;
let txt=0;
let txt2=0;

//birinci
console.log(str.length) // str daxilində neçə xarakter olduğunu ekrana yazdırın

//ikinci
for(let i=0;i<str.length;i++){
if(str[i]==" "){
    probel++
}
if(str[i]==","){
    zapatoy++
}
}
console.log(str.length-probel-zapatoy + " Herflerin sayi") //str daxilində neçə hərf olduğunu ekrana yazdırın


//ucuncu
let array1=[];
  for(let i=0;i<str.length;i++){      
    cislo++
    vtoroyecislo;
   if(str[i]==" "){                      
       array1.push(str.slice(vtoroyecislo,cislo-1))
        vtoroyecislo=cislo
    }
}
console.log(array1)      //str daxilindəki sözləri ayrı bir massiv içərisində toplayın


//dorduncu
for(i=0;i<str.length;i++){
    for(let x=0;x<sait.length;x++){
        if(str[i]==sait[x]){
            a++
        }
    }
}
console.log(a + " Saitlerin sayi")
console.log(str.length-probel-zapatoy-a + " Samitlerin sayi")    //str daxilində neçə sait və neçə samit olduğunu ekrana çap edin


//bewinci
console.log(str.slice(0,84))    //str daxilində son iki sözü silən metod yazın

//altinci
for(let n=0;n<str.length;n++){
    txt++
    if(str[n]==","){
        break
    }
    }
console.log(str.slice(0,txt-1))
console.log(str.slice(txt,str.length))     //str ni vergülə görə ayırıb iki string halına gətirin


//yetdinci
function find(soz){
    while(true){
        for(let q=0;q<array1.length;q++){
            if(array1[q]==soz){
                return " Soz tapildi"
            }
        }
        return "Soz tapilmadi"
    }
    
}

console.log(find("yib"))   //stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın