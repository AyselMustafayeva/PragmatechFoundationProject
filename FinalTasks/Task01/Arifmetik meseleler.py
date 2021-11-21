#https://www.hackerrank.com/challenges/python-loops/problem
# Ve ondan bawqa Fibonaççi reqemlerini yazdim 
import math
def regeminkvadrati():
    sayi=int(input(("Hansi regeme geder regemlerin kvadrati tapilsin: ")))
    for i in range(sayi):
        print(int(math.pow(i,2)))


def fibonachi():
    x=1
    y=0
    sayi2=int(input("Fibonççi regeminin uzunluqunu ver : "))
    for i in range(sayi2):
        x=x+y
        y=x-y
        print(x)
        
regeminkvadrati()
fibonachi()

