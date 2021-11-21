#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=false
#Bu proqramda biz dahil edeciyik  marka sayini, sonra ise olkelerin adlarini qeyd edeciyik
#proqram ise ekrana gosterecek olke sayini , cunki tekrar olduqu markalar ola biler

def marka():
    markasayi=int(input("Marka sayini dahil et: "))
    markayiqma=[]
    for i in range(markasayi):
         markaad=input("Markalarin hansi olkeden olduqunu dahil edin :  ")
         markayiqma.append(markaad)
    newmarkayiqma=set(markayiqma)
    print(len(newmarkayiqma))


marka()