#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=false
# bu meselede bizde iki grup olacaq, inglis dili ve rus dili qrupu, ve waqirdler o qruplara yazilacaqlar
#biz yalniz onlarin ID qeyd edeciyik< sonrada baxaciyiq, nece nefer en azi birine yazilib, nece nefer ikisinede,nece nefer
#yalniz birirne

def setmeselesi():
    print("Qeyd edek ki bir insanin  id-ni bir qrupa yazilanda tekrar tezden yazmaq menasi yox!!!")
    eng=[]
    rus=[]
    engsay=int(input("Inglis dili qrupuna nece waqird yazilacaq? "))
    for i in range(engsay):
        engstudent=int(input("Inglis diline yazilan uwaqlarin ID-ni dahil edin: "))
        eng.append(engstudent)
    russay=int(input("Rus dili qruuna nece nefer yazilacaq? "))
    for i in range(russay):
        russtudent=int(input("Rus diline yazilan uwaqlarin ID-ni dahil edin: "))
        rus.append(russtudent)
    neweng=set(eng)
    newrus=set(rus)
    print("Indi baxaq nece waqird en azi bir qrupa yazilib: ")
    enazibiri=neweng.union(newrus)
    print(len(enazibiri))
    print("Bes iki qrupun ikisinede nece nefer yazilib?")
    ikisinede=neweng.intersection(newrus)
    print(len(ikisinede))
    print("Bes yalniz rus ve yalniz inglis qrupuna ?")
    yalnizinglis=neweng.difference(newrus)
    yalnizrus=newrus.difference(neweng)
    print("Yalniz rus qrupuna: ",len(yalnizrus), "ve yalniz inglis qrupuna: ", len(yalnizinglis))


setmeselesi()
    