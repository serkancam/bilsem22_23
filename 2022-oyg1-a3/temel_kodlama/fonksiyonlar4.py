#tanımlama

#geriye değer döndürmeyecek
# ax+b
def fonksiyon_yol1(a:float,b:float,x:float):
    sonuc= a*x+b
    print("sonuc:",sonuc)

#geriye değer döndüren 
def fonksiyon_yol2(a:float,b:float,x:float):
    sonuc =  a*x+b
    return sonuc
#çağırmalar
fonksiyon_yol1(3,4,2)#3*2+4
fonksiyon_yol1(2,1,-2)#2 * -2 + 1

snc1=fonksiyon_yol2(2,4,2)#2*2+4
print(snc1)

isim1="ahmet furkan"
isim2="furkan"
isim3="utku"
isim4="doruk taha"
print("en çok karakter olan:",max(len(isim1),len(isim2),len(isim3),len(isim4)))

#len(isim1)  --> isim1-->"ahmet furkan" --> karakter sayısı

print("en az karakter olan:",min(len(isim1),len(isim2),len(isim3),len(isim4)))