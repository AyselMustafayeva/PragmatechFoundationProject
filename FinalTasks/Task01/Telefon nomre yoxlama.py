#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=false
#nomre 10 regemnen ibaret olmalidi ve evveli 7,8 ya 9 dan bawlamalidi ve 

def nomreyoxlama():
    sayi=int(input("Yoxlamaq ucun nomrelerin sayini dahil edin: "))
    array=[]
    for i in range(sayi):
        nomre=input("Nomreni dahil et:")
        array.append(nomre)
    for nomr in array:
        if nomr[0]!="7" and nomr[0]!="8" and nomr[0]!="9":
            print(nomr,"- bu duzgun nomre deyil")
        elif len(nomr)!=10:
            print(nomr,"- bu duzgun nomre deyil")
        else:
            print(nomr,"- bu duzgun nomre di")



nomreyoxlama()