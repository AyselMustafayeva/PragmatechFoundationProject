#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=false
#biz bir soz vereciyik ve regem, o regeme gore bu soz bolunecek ve coxlu kombinasiyalar yaradacaq herif arasi.
#combinationun permutationdan fergi var, indi ikincini yaziriq

from itertools import permutations
def permutation():
    c=" "
    soz =input("Sozunu dahil et: ")
    say=int(input("Nece herif sayindan kombinasiya olsun? "))
    nese=permutations(soz,say)
    for i in list(nese):
        for t in i:
            c+=t
        print(c)
        c=" "
permutation()
