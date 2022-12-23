# isimli parametre ve varsayılan değer

# a^3 + b^2 + c
import math
def f(a,b,c):
    sonuc=a**3 + b**2+c
    print("sonuc:",sonuc)

def daire_alani_bul(yaricap,pi=math.pi):
    alan=pi* yaricap ** 2
    print("daire alanı:",alan)

f(3,4,5) # pozisyona dayalı gönderme

f(b=8,c=3,a=2) # isimli gönderme

# f(3,b=8,a=8) # hatalı
# f(b=2,3,5) # hatalı
daire_alani_bul(5)
daire_alani_bul(5,3)

r = float(input("yarıçap giriniz:"))
daire_alani_bul(r)
daire_alani_bul(r,3)
print("pi :",math.pi)
