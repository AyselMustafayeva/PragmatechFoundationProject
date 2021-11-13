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

q=len(adlar[0])
c1=[]
c2=[]
c3=[]
c4=[]
c5=[]
def sozderinleni():
   global c1
   global c2
   global c3
   global c4
   global c5
   for ad in adlar:
       if len(ad)==q:
           c1.append(ad)
       if len(ad)==(q+1): 
             c2.append(ad)
       if len(ad)==(q-1):
            c3.append(ad)
       if len(ad)==(q+2): 
             c4.append(ad)
       if len(ad)==(q-2):
            c5.append(ad)
   print(c1)
   print(c2)
   print(c3)
   print(c4)
   print(c5)
           


     
 
        


sozderinleni()