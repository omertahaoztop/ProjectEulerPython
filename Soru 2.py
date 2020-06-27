# -*- coding: utf-8 -*-
#Soru 2: Fibonacci serisnide her sayı, kendisinden önce gelen iki sayının toplamıdır. 1 ve 2 başlayan serinin ilk 10 sayısı:
#1,2,3,5,8,13,21,34,55,89,.. Dört milyondan küçük tüm çift sayılarının toplamını bulunuz.

toplam=0
x=1 #ilk sayı 1 
y=2 # ikinci sayı da 2
while x < 4000000:
    if x % 2 == 0:
        toplam += x
    x,y=y,x+y
print(toplam)

"""
Alternatif Çözüm:
s1 = 2
s2 = 1
n = s1 + s2
top = 2 
while n < 4000000:
    n = s1 + s2
    if n % 2 == 0:
        top = top + n
    s2 = s1
    s1 = n
print(top)    
 """
    