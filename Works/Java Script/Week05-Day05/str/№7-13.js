let str=`Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır`
let probel=0;
let zapatoy=0;
let cislo=0;
let vtoroyecislo=0;
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
console.log(str.length-probel-zapatoy) //str daxilində neçə hərf olduğunu ekrana yazdırın


//ucuncu
let array1=[];

 // for(let i=0;i<str.length;i++){      Bunu istifade ederek her sozun lenght bilib array1 elave ede bilerem.
   //  cislo++
   // if(str[i]==" "){                      Amma legth -1 gotururem, cunki birdefe artiq gedir
   //     console.log(cislo)
   //     cislo=0;
   // }
//}

  for(let i=0;i<str.length;i++){      
    cislo++
    vtoroyecislo;
   if(str[i]==" "){                      
       array1.push(str.slice(vtoroyecislo,cislo-1))
        vtoroyecislo=cislo
    }
}
console.log(array1)

