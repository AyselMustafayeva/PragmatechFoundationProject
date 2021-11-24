#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=false
# в прямоугольном треугольнике,медиана делит гипотенузу пополам, и сама медиана равняется ее половине,
#  следовательно у нас получаются два равнобедренных треугольника, а значит угол MBC равняется углу C

import math
print("Bizde duzbucaqli ucbucaq var ABC, median BM hipotenuzaya çəkildi,\nalinan MBC bucaqini tap ")
AB=float(input("AB yanini dahil et: "))
BC=float(input("BC yanini dahil et: "))
AC=math.sqrt(math.pow(AB,2)+math.pow(BC,2))            #hipotenuza=(AB^2+BC^2)^(1/2)
MBC=math.degrees(math.acos((math.pow(BC,2)+math.pow(AC,2)-math.pow(AB,2))/(2*AC*BC)))  #bucaq MBC=arcos(BC^2+AC^2-AB^2)/2*AC*BC
print("MBC bucaqi: ",MBC,"°")
