# -*- coding: utf-8 -*-
#Soru 5: 1'den 10 kadar bütün sayılara kalansız bölünen en küçük sayı 2520'dir
# 1'den 20'ye kadar bütün sayılara kalansız bölünen en küçük pozitif sayı kaçtır?
from math import gcd as ebob
import functools

def ekok(x,y):
    return x * y // ebob(x,y)
liste=range(1,21)
sonuc=functools.reduce(ekok,liste)
print(sonuc)

"""
Alternatif çözüm:
   i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print i
""" 