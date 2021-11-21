# link: https://www.hackerrank.com/challenges/text-wrap/problem
#Indi yazdiqim proqram dahil etdiyin sozu ya metni setirde herif sayina gore bolur(vergul dahil olmaqla),
# sayini dahil edirik ozumuz,ve alinan sozleri teze setire kocurub gosterir

text = input("Sozu ya mətni dahil edin: ")
setir=int(input("Sətirdə neçə hərf sayı olduqunu dahil et: "))

def bolme():
    global text
    global setir
    Birsetirdesoz= " "
    qalanherifler=" "
    Sozyiqma=[]
    miqdar=0
    for i in range(len(text)):
        Birsetirdesoz=Birsetirdesoz+text[i]
        if (i+1)%setir==0:
            Sozyiqma.append(Birsetirdesoz)
            Birsetirdesoz= " "
            miqdar=miqdar+1
        elif  (len(text)-(setir*miqdar))<setir:
            qalanherifler+=text[i]
    Sozyiqma.append(qalanherifler)
    for bolunentext in Sozyiqma:
        print(bolunentext)

bolme()
    

            
            
            