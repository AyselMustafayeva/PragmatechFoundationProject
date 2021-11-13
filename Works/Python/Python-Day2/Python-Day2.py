data=[
    
    {
        'id':1,
        'name':'Jhon',
        'surname':'Doe'
    },
     {
        'id':2,
        'name':'Ehmed',
        'surname':'Quliyev'
    },
    {
        'id':3,
        'name':'Sabir',
        'surname':'Eliyev'
    },
    {
        'id':4,
        'name':'Qulu',
        'surname':'Quliyev'
    },
    {
        'id':5,
        'name':'Sabir',
        'surname':'Memmedov'
    }

]


def adtap():
    ad2=input("Axtardiqiniz adamin adini dahil edin: ")
    for i in range(len(data)):
        if data[i]["name"]==ad2:
            print("id: ",data[i]["id"],"ad: ",data[i]["name"],"soyad: ",data[i]["surname"])

def idcox():
     for i in range(len(data)):
        if data[i]["id"]>2:
            print("id: ",data[i]["id"],"ad: ",data[i]["name"],"soyad: ",data[i]["surname"])

def idenboyuk():
    for i in range(len(data)):
        if i==(len(data)-1):
            print("id: ",data[i]["id"],"ad: ",data[i]["name"],"soyad: ",data[i]["surname"])

def scixart():
    for i in range(len(data)):
        for herif in data[i]["name"]:
            if herif=="S":
                 print("id: ",data[i]["id"],"ad: ",data[i]["name"],"soyad: ",data[i]["surname"])
            

adtap()
print("Idsini 2 den boyuk olan istifadeciler")
idcox()
print("En boyuk id ye sahib istifadecinin melumatlarini goster")
idenboyuk()
print("Adinin daxilinde s herfi olan istifadeni gosterin")
scixart()