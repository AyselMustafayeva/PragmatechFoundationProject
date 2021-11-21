#https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

def stringnum():
    soz=" "
    num=int(input("Hansi regeme geder ekranda gosterilsin: "))
    for i in range(num):
        soz+=str(i+1)
    print(soz)

stringnum()