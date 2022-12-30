# ikinci derecen bir denklem için a,b,c sabitlerini ve x değerini alıp
# sonucu hesaplayan bir fonksiyon yazalım
import matplotlib.pyplot as plt
#1. tanımalama işlemins sonucunu bulup ekrana yazdıran fonksiyon
def fonksiyon_yol1(a:float,b:float,c:float,x:float):  
    sonuc = a*x**2 + b*x + c
    print("sonuç:",sonuc)


#2. tanımlama işlem sonucunu geriye deöndüren fonksiyon
def fonksiyon_yol2(a:float,b:float,c:float,x:float):
    sonuc=a*x**2 + b*x + c
    return sonuc


#çağırmalar
fonksiyon_yol1(3,4,3,1)
fonksiyon_yol1(3,4,3,2)
fonksiyon_yol1(3,4,3,3)

snc1=fonksiyon_yol2(5,4,1,1)
snc2=fonksiyon_yol2(5,4,1,2)

print("yol2:",snc1)
print("yol2:",snc2)


x=[i for i in range(10001)]
y=[]

for i in x:
    ys=fonksiyon_yol2(-2,7,7,i)
    y.append(ys)

print(x)
print(y)

plt.plot(x,y)
plt.show()