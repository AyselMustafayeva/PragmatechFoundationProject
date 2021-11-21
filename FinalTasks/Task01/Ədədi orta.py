#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def edediorta():
    sayi=int(input("Regem sayini dahil et: "))
    array=[]
    eyniolan=0
    summa=0
    newarray=[]
    for i in range(sayi):
        regemler=int(input("Regemi dahil et: "))
        array.append(regemler)
    newarray=set(array)
    for regem in newarray:
        summa=summa+regem
    print("Cavab: ",summa/len(newarray))

print("Bu program reqemlerin ededi ortasini tapir,\namma regemler tekrarlananda, o regemnen birini sahliyir")
edediorta()