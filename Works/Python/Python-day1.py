kitab={
    'ad': "Молчание ягнят" ,
    'yazan': "Томмас Харрис",
    'il': "1988 год" ,
    'sehifesayi': "352" 
}
a=[]
def Showbook():
    for key,val in kitab.items():
        print(key,": ",val)

Showbook()

def changebook():
    kitab["ad"]=input("Bawqa kitab adi yaz: ")
    for key,val in kitab.items():
        print(key,": ",val)
        break
    
changebook()
