##########tombala oyunu sözde kodu#####
#1.adım: 15 elemanlı 1-90 arası değerleri olan 2 kart tanımlayalım
#2. adım: tombalda çekilecek 1-90 arası sayıları barındıran bir torba tanımlayalım
#3. adım: torbadan bir sayı çekelim
#4. adım: çekilen sayı kartlarda var mı bakalım
#5. adım: kartlarda var ise hangi kartta olduğunu belirtip karttan o sayıyı silelim
#6. adım: eleman sayısı 0 a düşen kart varsa oyunu 8. adıma gidelim
#7. 3. adıma: git
#8. adım:  kazananları yaz
#9. adım: oyunu bitir

from random import choice #koleksiyondan rastegele bir değer seçer
from time import sleep # programı bir süre uyutur.
#1. adım:
kart1=[1,20,40,64,71,10,30,56,79,88,2,23,46,68,87]
kart2=[4,25,41,62,75,11,33,52,77,82,8,28,47,67,89]
#2. adım
torba=list(range(1,91))
# print(torba)
#3. adım
while True:#len(kart1)!=0 or len(kart2)!=0:
    cekilen=choice(torba)
    torba.remove(cekilen)
    print(cekilen,"kimde var?")
    #4. adım - 5.adım
    if kart1.count(cekilen)==1:
        print("kart1: bende var.")
        kart1.remove(cekilen)
    else:
        print("kart1: bende yok:")
    if kart2.count(cekilen)==1:
        print("kart2:bende var.")
        kart2.remove(cekilen)
    else:
        print("kart2: bende yok.")
    #6. adım
    if len(kart1)==0 or len(kart2)==0:
        break
    #7. adım
    print(30*"-")
    sleep(0.1)
print(30*"*")
#8. adım
if len(kart1)==0:
    print("kart1: Tombala")
if len(kart2)==0:
    print("kart2: Tombala")
