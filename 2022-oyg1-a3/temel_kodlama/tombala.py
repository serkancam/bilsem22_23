######tombala######

#1. adım: içinde 1-90 arası rastgele 15 farklı sayı bulunan 2 kart tanımla
#2. adım: içinde 1-90 arası bütün sayılar olan bir torba tanımla
#3. adım: torbadan rastgele bir sayı çek ve torbadan sil
#4. adım: çekilen sayı kartlarda varsa her kart bende var desin yoksa bende yok desin
#5. adım: içinde çekilen sayı olan kartlardan çekilen sayıyı sil
#6. adım: *kartlardan biri 0 elemanı kaldıysa 8.adıma git
#7. adım: 3. adıma git
#8. adım: kazan kart(lar)ı ekrana tombala yazssın
#9. adım: bitir 
from random import choice,randint
from time import sleep

#1. adım
kart1=set()
while len(kart1)<15:
    kart1.add(randint(1,90))

kart2=set()
while len(kart2)<15:
    kart2.add(randint(1,90))

kart1=list(kart1)
kart2=list(kart2)

#2. adım
torba = list(range(1,91))
# print(torba)
#3. adım
while True:    
    cekilen=choice(torba)
    torba.remove(cekilen)
    #4. adım
    print(cekilen,"kimde var?")
    if kart1.count(cekilen)==1:
        print("kart1: bende var.")
        kart1.remove(cekilen)
    else:
        print("kart1: bende yok")
    

   