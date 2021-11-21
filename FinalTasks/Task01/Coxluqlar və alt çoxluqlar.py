#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true


def coxluqlar():
    coxluq=[]
    altcoxluq=[]
    coxluqsayi=int(input("Coxluqun icinde nece element olacaq? "))
    for t in range(coxluqsayi):
        coxluqadd=int(input("Elementleri dahil et: "))
        coxluq.append(coxluqadd)
    altcoxluqsayi=int(input("Alt coxluqun icinde nece element olacaq?"))
    for x in range(altcoxluqsayi):
        altcoxluqadd=int(input("Elementleri dahil et: "))
        altcoxluq.append(altcoxluqadd)
    newcoxluq=set(coxluq)
    newaltcoxluq=set(altcoxluq)
    print("Eger dahil etdiyimiz elementler altcoxluqda var coxluqun ozunde, onda True cixacaq")
    check=newaltcoxluq.issubset(newcoxluq)
    print(check)

coxluqlar()