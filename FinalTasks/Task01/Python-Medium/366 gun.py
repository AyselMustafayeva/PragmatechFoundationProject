#https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=false
# sıçrayış ili olub olmamiqini yoxlamaq

say=int(input("Necedene illeri yoxlamaq istiyirsen?"))

for i in range(say):
    il=int(input("Ilinizi dahil edin: "))
    if(il%400==0):
        print("sıçrayış ilidi, 366 gun")
    else:
        if(il%100==0):
            print("adi ildi, 365 gun")
        else:
            if(il%4==0):
                print("sıçrayış ilidi, 366 gun")
            else:
                print(" adi ildi , 365 gun")
            