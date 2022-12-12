from random import choice

def kelime_sec(kelimeler:list)->str:
    secilen = choice(kelimeler)
    return secilen
sorular =["ankara","edirne","muş","izmir","hatay"]

soru = kelime_sec(sorular)
harfler=list(set(soru))
girilen_harfler=list()
bilinen_harfler=list()
hak=8

while hak>0:
    harf=""
    #harf al
    while True:
        harf=input("\nharf giriniz:")
        if len(harf)==1 and harf not in girilen_harfler and harf.isalpha():
            girilen_harfler.append(harf)
            break
    # harf kelimede var mı yokmu=
    if harf in harfler:
        bilinen_harfler.append(harf)
    else:
        hak=hak-1
        print(f" {hak} hakkınız kaldı.")      
        
    # metni yazdır
    for i in soru:
        if i in bilinen_harfler:
            print(i,end=" ")
        else:
            print("_",end=" ")
    # kazanma durumu
    if len(harfler)==len(bilinen_harfler):
        print("\ntebrikler!")
        break
    








