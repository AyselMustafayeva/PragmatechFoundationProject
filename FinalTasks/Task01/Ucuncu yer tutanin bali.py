#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=false
#amma ucuncu yer tutan waqirdin balini cixardacam

saqirdsayi=int(input("Nece saqird istrak edib idman olimpiadasinda: "))
array=[]
for i in range(saqirdsayi):
    yiqdiqiballar=int(input("Nece bal yiqdiqini dahil et (max:10) : "))
    array.append(yiqdiqiballar)
array.sort()
newarray=set(array)
array=[]
for t in newarray:
    array.append(t)
array.reverse()
print("Ucuncu yer tutan waqirdin bali: ",array[2])