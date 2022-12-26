#sinif_ve_nesne.py

# Insan sınıfı
class Insan:
    def __init__(self,ad,soyad,sinif) :# nesne türeten method
        self.ad=ad
        self.soyad=soyad
        self.sinif=sinif
        self.kilo=0
        self.boy=0
    def yemek_ye(self,miktar:float):
        self.kilo=self.kilo + miktar*0.08
    def kos(self, mesafe:float): 
        self.kilo = self.kilo-mesafe*0.005  



# Nesneler 

metehan  = Insan("meteha","özen",7)# nesne türetme.
ada = Insan("ada","akgün",7)# bu çalışan methoda yapıcı method
zahid= Insan("muhammed zahid","bilik",7)
metehan.boy=1.63
metehan.kilo=55
ada.boy=1.68
ada.kilo=49
zahid.kilo=45
zahid.boy=1.48

print(type(metehan))
print(type(5))
print(ada.ad,ada.soyad,ada.sinif)
print(zahid.ad,zahid.soyad,zahid.sinif)
print(metehan.ad,metehan.soyad,metehan.sinif)

serkan =Insan("serkan","çam",9)
serkan.kilo = 80
serkan.boy=1.74

print("yemekten önce kilo:",serkan.kilo)
serkan.yemek_ye(0.5)
print("yemekten sonra kilo:",serkan.kilo)
serkan.kos(2)
print(serkan.kilo)


