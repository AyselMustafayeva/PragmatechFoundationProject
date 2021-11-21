#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
#indi ise permutation etdiyimiz cure combination edirik, ferginide gore bilerik
from itertools import combinations

def combination():
    c=" "
    soz =input("Sozunu dahil et: ")
    say=int(input("Nece herif sayindan kombinasiya olsun? "))
    nese=combinations(soz,say)
    for i in list(nese):
        for t in i:
            c+=t
        print(c)
        c=" "
combination()