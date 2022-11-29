from random import randint,choice
import time

kart1 = [1,20,40,64,71,10,30,56,79,88,2,23,46,68,87]
kart2 = [4,25,41,62,75,11,33,52,77,82,8,28,47,67,89]
kart3 = [randint(1, 90) for i in range(15)]

# 1-90 arası sayıların olduğu listeyi oluşturdum.
torba = list(range(1,91))


#1. adım: 1-90 arası sayı tut(aynı sayı tutulmasını engelle)
#2. adım: kartlarda bu sayı var mı diye kontrol et
#3. adım: tutulan sayıyı olan kartlardan sil
#4. adım: kartlardan 0 elemanı olan varsa oyunu bitir. ve kazanan kartı yazdır.
#5. adım 1. adıma git

while len(torba)!=0:
    # time.sleep(0.5)
    # 1. adım rastyge daha önce tutulmamış sayı bul 1-90
    cekilen = choice(torba) # torba listesinden rastegele bir sayı seç ve cekilen değişkenine aktar
    print(f"{cekilen} kimde var?")
    torba.remove(cekilen) # cekilen sayıyı torbadan sil
    #2. ve 3. adım
    if kart1.count(cekilen)>0:
        kart1.remove(cekilen)#3. adım
        print("kart1: bende var.")
    if kart2.count(cekilen)>0:
        kart2.remove(cekilen)#3. adım
        print("kart2: bende var.")    
    if kart3.count(cekilen)>0:
        kart3.remove(cekilen)#3. adım
        print("kart3: bende var.")
    
    #4. adım
    if len(kart1)==0:
        print("kart1 oyunu kazandı.")
    if len(kart2)==0:
        print("kart2 oyunu kazandı.")
    if len(kart3)==0:
        print("kart3 oyunu kazandı.")
    

    if len(kart1)==0 or len(kart2)==0 or len(kart3)==0:
        break

print(kart1)
print(kart2)
print(kart3)