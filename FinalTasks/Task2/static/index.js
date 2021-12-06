var tekst = `Hi.I want to show you many insteresting facts and play game with you.
Do you want it too?`

let txt = document.querySelector(".text")
var knpk = document.querySelector("#knopka")
var i = 0;


function click() {
    window.addEventListener('click', function (event) {
        knpk.style.left = (event.clientX - knpk.clientWidth / 2) + 'px';
        knpk.style.top = (event.clientY - knpk.clientHeight / 2) + 'px';
    })
}

function sozyazma() {
    if (i < tekst.length) {
        txt.innerHTML += tekst.charAt(i);
        i++;
        setTimeout(sozyazma, 60);
    } else {
        txt.innerHTML = ''
        i = 0
        if (i == 0) {
            sozyazma()
        }
    }
}

sozyazma()
click()