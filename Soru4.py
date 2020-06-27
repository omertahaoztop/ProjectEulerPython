# -*- coding: utf-8 -*-
#Soru 4: İki yönden de aynı şekilde okunan sayılara palindromik sayılar denir. 2 haneli 2 sayıdan oluşturabilecek en büyük palindrom değeri 9009'dur.
# 3 haneli iki sayıdan oluşturulabilecek en büyük palindromik sayıyı bulunuz.

palindromSayilar=list()
for x in range(100,1000):
    for y in range(100,1000):
        carpim=x * y
        if str(carpim) == str(carpim) [::-1]:
            palindromSayilar.append(carpim)

print(max(palindromSayilar))            
        
 

""" 
Alternatif Çözüm:
mars = []
venus = list(range(1, 1000))
for i  in venus:
    for v in venus:
        d = v * i
        res = [int(x) for x in str(d)]
        des = res[::-1]
        if res == des:
            if d not in mars:
                mars.append(d)

print(max(mars))


"""       
