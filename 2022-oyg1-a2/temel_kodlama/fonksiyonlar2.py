# varsayılan değer
#tanımlama
def daire_alani_bul(yaricap,pi=3.14):
    alan = pi * yaricap ** 2
    print("daire alanı:",alan)

#çağırma
daire_alani_bul(20,3)
daire_alani_bul(20)

# geri değer döndürme(return)

def ucuncu_aci_hesapla(aci1,aci2):
    aci3 = 180-(aci1+aci2)
    return aci3


a = ucuncu_aci_hesapla(10,25)# buraya return ile döndürülen değer gelecek
print(a)
print(ucuncu_aci_hesapla(45,62))
