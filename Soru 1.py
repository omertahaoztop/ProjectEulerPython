# -*- coding: utf-8 -*-
#Soru 1: 3'ün veya 5'in 1000 den küçük tüm katlarının toplamını bulunuz
toplam=0
for i in range(0,1000): #1000 den küçük sayılar olduğu için for döngümüzü 1000 e kadar ayarladık
    if i % 3 == 0 or i % 5 == 0: #Gerekli olan şartlar girildi.
        toplam+=i
print(toplam)        
        
    
    
"""
Alternatif Çözüm 2:
 x=[]
for i in range(1,1000):
    if i % 3 ==0:
        x.append(i)
    elif i % 5 == 0:
        x.append(i)
print(sum(x))
"""        
        