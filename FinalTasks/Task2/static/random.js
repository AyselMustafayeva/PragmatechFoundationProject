tekst4 = `Cool, I'm glad you decided to play with me. There are no rules in this game. 
My creator wrote a program by which I guess a random number. 
If your number is greater than mine,
 then you won, but if on the contrary, 
 then the code worked in my favor. Heh.
 In addition, the numbers must be in the range from 0 to 1000.`

let txt6 = document.querySelector(".text6")
t = 0;


function sozyazma4() {
    if (t < tekst4.length) {
        txt6.innerHTML += tekst4.charAt(t);
        t++;
        setTimeout(sozyazma4, 60);
    } else {
        txt6.innerHTML = ''
        t = 0
        if (t == 0) {
            sozyazma4()
        }
    }
}


sozyazma4()