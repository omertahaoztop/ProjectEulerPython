# -*- coding: utf-8 -*-
# Soru 6 : İlk 100 doğal sayının toplamlarının karesi ile karalerinin toplamı arasındaki farkı bulunz:


toplam1 = 0
for i in range(1,101): #100 dahil olduğu için döngü 101 ile bitirildi.
    toplam1 +=i**2 
toplam2=0
for j in range(1,101):
    toplam2 += j
toplam2 = toplam2**2 
print(toplam2-toplam1)
