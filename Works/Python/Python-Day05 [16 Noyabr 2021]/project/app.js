let i = 1;
let x=0;
let tekst="KVA!"
let txt=document.querySelector(".text")
    for(let li of carousel.querySelectorAll('li')) {
      li.style.position = 'relative';
      li.insertAdjacentHTML('beforeend', `<span style="position:absolute;left:0;top:0">${i}</span>`);
      i++;
    }

    let width = 300; 
    let count = 1; 

    let list = carousel.querySelector('ul');
    let listElems = carousel.querySelectorAll('li');

    let position = 0; 
    carousel.querySelector('.prev').onclick = function() {
      position += width * count;
      position = Math.min(position, 0)
      list.style.marginLeft = position + 'px';
    };

    carousel.querySelector('.next').onclick = function() {
      position -= width * count;
      position = Math.max(position, -width * (listElems.length - count));
      list.style.marginLeft = position + 'px';
    };
 
    function kva(){
        if(x<tekst.length){
            txt.innerHTML+=tekst.charAt(x)
            x++
            setTimeout(kva,100) 
        }
        else{
            txt.innerHTML=''
            x=0
            if(x==0){
                kva()
        }
    }
    }
 kva()