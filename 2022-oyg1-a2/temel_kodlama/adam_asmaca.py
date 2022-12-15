########## sözde kodu##########
# 1. adım: soru listesi oluştur
# 2. adım: listeden soru seç
# 3. adım: sorudaki harfleri bul
# 4. adım: bilinen_harfler boş listesi oluştur
# 5. adım: soylenen_harfler boş istesi oluştur
# 6. adım: hak sayısını belirle
# 7. adım: hak sayısana bak 0 sa bitir
# 8. adım: kullanıcıdan bir harf iste
# 9. adım: girilen 1 harf ve soylenen harflerde yoksa 8. adıma dön
# 10. adım: harf sorudaki kelimede varsa bilinen harflere ve söylenen harflere ekle  yoksa hak sayısını 1 azalt ve sadece söylenen harflere ekle
# 11. adım: sorudaki kelimede bilenen harflari yazdır bilimnmeyenlerin yerine _ koy
# 12. adım: sorudaki kelimede ki bütün harfler bilindi ise  13. adıma git, hakkı varsa 7. adıma git
# 13. adım: eğer bütün harfler bilindi ise hak sayısı 0'dan büyükse tebrikler! yaz 
# 14. adım bitir
from random import choice

################adam çiz#################

def ciz(hak:int):
    print("\n\n")
    if hak==5:
        print("  O  ")
    elif hak==4:
        print("  O  ")
        print("  |   ")
        print("  |  ")
    elif hak==3:
        print("  O  ")
        print(" /|   ")
        print("  |  ")
    elif hak==2:
        print("  O  ")
        print(" /|\ ")
        print("  |  ")
    elif hak==1:
        print("  O  ")
        print(" /|\ ")
        print("  |  ")
        print(" /   ")
    elif hak==0:
        print("  O  ")
        print(" /|\  ")
        print("  |  ")
        print(" / \\")
#########################################



#1. adım:
kelimeler =["kedi","köpek","tavşan","fil","kaplumbağa","kanguru","inek"]
#2. adım:
soru = choice(kelimeler)
#3. adım:
harfler = list(set(soru))
#4. ve 5. adım:
bilinen_harfler=list()
soylenen_harfler=[]
#6. adım:
hak=6
#7. adım
while hak>0:
    #8. adım
    harf=""
    while True:
        print(f"\n{hak} hakkınız kaldı")
        harf = input("harf giriniz:")
        #9. adım
        if len(harf)==1 and harf not in soylenen_harfler and harf.isalpha():            
            break   
    #10. adım:
    if harf in harfler:
        bilinen_harfler.append(harf)
        soylenen_harfler.append(harf)
    else:
        soylenen_harfler.append(harf)
        hak=hak-1
    #11. adım
    for h in soru:
        if h in bilinen_harfler:
            print(h,end=" ")
        else:
            print("_",end=" ")
    ciz(hak)
    if len(bilinen_harfler)==len(harfler):
        print("\nTebrikler!")
        break

if hak==0:
    print(f"bilemedin kelime {soru}")    



