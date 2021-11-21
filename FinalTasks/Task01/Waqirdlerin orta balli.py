#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
#Bi yazdiqim program saqird haqda informasiyani dahil edir ve ekrana cixardir
# sonra ise ballarin orta ededini tapir

from collections import namedtuple

student=namedtuple("student","ad,qiymeti,idsi,sinif")
array=[]
summa=0
studentsayi=int(input("Student sayini dahil edin: "))
for i in range(studentsayi):
    name=input("Adinizi dahil edin: ")
    schoolclass=input("Sinifinizi dahil edin: ")
    mark=int(input("Balinizi dahil edin "))
    array.append(student((i+1),mark,schoolclass,name))
print("Id   Marks  Class   Name")
for t in range(studentsayi):
    summa+=array[t][1]
    print(array[t][0],"   ",array[t][1],"   ",array[t][2],"   ",array[t][3])
print("Studentlerin orta qiymeti: ", summa/studentsayi)
