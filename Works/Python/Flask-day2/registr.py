import re
class Registr:
    def __init__(registr,_name,_surname,_gmail,_phone,_password,_inform):
        user=[]
        registr.name=_name
        registr.surname=_surname
        registr.gmail=_gmail
        registr.phone=_phone
        registr.password=_password
        registr.inform=_inform
        user.append(registr)
    
    def addtodate(registr):
        file1=open("1.txt","a")
        file1.write(f"{registr.name} {registr.surname},{registr.password} ,{registr.gmail},{registr.inform}\n")




  
ad=""
soyad=""
email=""
nomre=""
parol=""
informasiya=""
    
def Geydiyat():
    global ad,soyad,email,nomre,parol,informasiya
    yoxlama = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
    print("Qeydiyattan kecin!")
    ad=input("Adinizi dahil edin(doldurulması zəruridir): ")
    soyad=input("Soyadinizi dahil edin(doldurulması zəruridir): ")
    email=input("Emailinizi dahil edin(doldurulması zəruridir): ")
    operator=input("Nomre operatorunun prefiksini qeyd edin (Bakcell(55),Azercell(50),Nar(70)):")
    nomre=input(f"Nomrenizi dahil edin. (doldurulması zəruri deyil): +994{operator}")
    parol=input("Parolunuzu qeyd edin(doldurulması zəruridir): ")
    while(True):
        if ad=="":
            ad=input("Adinizi dahil edin(doldurulması zəruridir): ")
        else:
            break
    while(True):
        if soyad=="":
            soyad=input("Soyadinizi dahil edin(doldurulması zəruridir): ")
        else:
            break
    while(True):
        if not re.fullmatch(yoxlama, email):
            email=input("Error.Emailinizi tezden dahil edin(doldurulması zəruridir): ")
        else:
            break
    while(True):
        if nomre=="":
            break
        if len(nomre)!=7:
            nomre=input(f"Error.Nomrenizi tezden dahil edin. (doldurulması zəruri deyil): +994{operator}")
        for x in nomre:
            if not x.isdigit():
                nomre=input(f"Error.Nomrenizi tezden dahil edin. (doldurulması zəruri deyil): +994{operator}")
        else:
            break
    while(True):
        saybalaca=0
        sayyeke=0
        if len(parol)>=8 and  parol.isalnum() and sum(character.isdigit() for character in parol)>=2:
            for x in parol:
                if x==x.upper():
                    sayyeke+=1
                if x==x.lower():
                    saybalaca+=1
            print(saybalaca,sayyeke)
            if (sayyeke- sum(character.isdigit() for character in parol))>=1 and (saybalaca- sum(character.isdigit() for character in parol))>=2:
                break
            else:
                parol=input("Parolunuzu yeniden qeyd edin(doldurulması zəruridir): ")
        else:
            parol=input("Parolunuzu yeniden qeyd edin(doldurulması zəruridir): ")
    informasiya=input("Oz haqda melumatnan boluw: ")
    User=Registr(ad,soyad,email,nomre,parol,informasiya)
    User.addtodate()

def dahilolmaq():
    print("Dahil ol!")
    for x in range(0,3):
        emailyoxlama=input("Emailinizi dahil edin: ")
        parolyoxlama=input("Parolunuzu dahil edin: ")
        with open('1.txt', 'r') as f:
            for line in f:
                if emailyoxlama in line.split() and parolyoxlama in line.split() :
                    print(line)
                    break
                else:
                    print("Error.Caliw yadina sal")
    Geydiyat()
    
qeydiyyatkecmek=input("Qeydiyyat kecmek istiyirsen mi?(Y/N)")
while qeydiyyatkecmek=="Y":
    Geydiyat()
    qeydiyyatkecmek=input("Qeydiyyat kecmek istiyirsen mi?(Y/N)")
dahilolmaq()






    

