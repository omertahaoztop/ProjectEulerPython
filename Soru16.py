# -*- coding: utf-8 -*-
#Soru 16: 2 üzeri 1000'in basamak sayıları toplamı
sayi=2**1000
toplam=0
for i in str(sayi):
    toplam+=int(i)
    print(toplam)


"""
Alternatif çözüm 2:
    toplam=0
    for n in str(2**1000):
        toplam+=int(n)
        print(toplam)
        """