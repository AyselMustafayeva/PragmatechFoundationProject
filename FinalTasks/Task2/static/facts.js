var tekst3 = `Please enter the name of the capital
 of a certain country and I will tell 
 you an interesting fact about it.`

let txt4 = document.querySelector(".text4")
n = 0;


function sozyazma3() {
    if (n < tekst3.length) {
        txt4.innerHTML += tekst3.charAt(n);
        n++;
        setTimeout(sozyazma3, 60);
    } else {
        txt4.innerHTML = ''
        n = 0
        if (n == 0) {
            sozyazma3()
        }
    }
}


sozyazma3()