########## sözde kodu##########
# 1. adım: soru listesi oluştur
# 2. adım: listeden ratgele soru seç
# 3. adım: sorudaki harfleri bul
# 4. adım: bilinen_harfler boş listesi oluştur
# 5. adım: soylenen_harfler boş istesi oluştur
# 6. adım: hak sayısını belirle
# 7. adım: hak sayısana bak 0 sa bitir
# 8. adım: kullanıcıdan bir harf iste
# 9. adım: girilen 1 harf ise ve soylenen harflerde yoksa 10. adıma git değilse 8. adıma git
# 10. adım: harf sorudaki kelimede varsa bilinen harflere ve söylenen harflere ekle  yoksa hak sayısını 1 azalt ve sadece söylenen harflere ekle
# 11. adım: sorudaki kelimede bilenen harflari yazdır bilimnmeyenlerin yerine _ koy
# 12. adım: sorudaki kelimede ki bütün harfler bilindi ise  13. adıma git, hakkı varsa 7. adıma git
# 13. adım: eğer bütün harfler bilindi ise hak sayısı 0'dan büyükse tebrikler! yaz 
# 14. adım bitir

from random import choice
from adam_asmaca_cizim import adam_asmaca_ciz
#1. adım
sorular = ["adana","urfa","edirne","izmir","ankara"]
#2. adım
soru = choice(sorular)
#3. adım
harfler=list(set(soru))
# 4. ve 5. adım
bilinen_harfler=list()
soylenen_harfler=[]
#6. adım
hak=6
#7. adım
while hak>0:
    harf=""
    while True:
        #8. adım
        print(f"\n{hak} hakkın var.")      

        harf=input("\n harf giriniz:")
        #9. adım
        if len(harf)==1 and harf not in soylenen_harfler and harf.isalpha():
            break
    #10. adım
    if harf in harfler:
        bilinen_harfler.append(harf)
        soylenen_harfler.append(harf)
    else:
        hak=hak-1
        soylenen_harfler.append(harf)
        adam_asmaca_ciz(hak)
    #11.adım
    for h in soru:
        if h in bilinen_harfler:
            print(h,end=" ")
        else:
            print("_",end=" ")
    #12. adım
    if len(harfler)==len(bilinen_harfler):
        print("\nTebikler!")
        break

if hak==0:
    print("\nHakkın bitti.")