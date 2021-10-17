let a=(3+4*2==2*3)&&(true+false/2);
console.log(a)
//cünki (3+4*2==2*3) baxsaq ,  bu mesele iki hissəyə bölürük, 4*2=8, cünki birinci vurma ve bölmə operasiyası olur , sonra plus ve minus , sonra plus 3, alınir 11. Və burda yazılıb ki o bərsbərdir 2*3, yəni 6. Səkkiz altıya bərabər deyil. Ona gore False.
//(true+false/2) baxsaq , bu meseleni iki hissəyə bölək, false/2=0/2=0.5 , ikinsi hissə isə true+0.5=1+0.5=1.5 , ədəd kimi baxsaq 1.5-i Boolean-a döndürsək , çıxacaq True.
//Axrıncı məsələ, (False)&&(True) , 0 və 1 , çıxır 0, yəni false.