adlar=[
    'Fezail',
    'Rehman',
    'Elmar',
    'Sebuhi',
    'Aysel',
    'Murad',
    'Vesile',
    'Ravi'
]



def name():
    for i in range(len(adlar)):
        print(i,adlar[i])
def cut():
    for i in range(len(adlar)):
        if i%2==0:
            print(i,adlar[i])

def siralamaq():
    adlar.sort()
    name()

def icindeeolan():
  #  for ad in adlar:
      #  for x in ad:
           # if x=="e":
              #  print(ad)
    for ad in adlar:
        if ad.find('e')!=-1:
            print(ad+ " sozunde e herfi var")
        else:
            print(ad+ " sozunde e herfi yoxdu ")

def  axriiolan():
    for ad in adlar:
        if ad[(len(ad)-1)]=="i":
            print(ad + " bu adlarin axrinda i herifi var ")     
 
        

x=0
c=[]
def biryerde():
    global c
    global x
    for i in range(20):
        for t in range(len(adlar)):
            if len(adlar[t])==x:
                c.append(adlar[t])
        if len(c)>0:
            print(c)
        x=x+1
        c=[]
        
biryerde()