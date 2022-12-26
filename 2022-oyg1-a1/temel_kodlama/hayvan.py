class Hayvan:
    def __init__(self,ad,kilo) :
        self.ad=ad
        self.kilo=kilo
        print("Hayvan init çalıştı.")
    def yemek_ye(self,miktar):
        self.kilo += miktar*0.05

class Kedi(Hayvan):
    def __init__(self,ad,kilo,ayak_adedi):
        super().__init__(ad,kilo)
        self.ayak_sayisi=ayak_adedi
        print("Kedi init çalıştı.")
    def ses_cikar(self):
        print("miyav")

class Balik(Hayvan):
    def __init__(self, ad, kilo,pul_rengi):
        super().__init__(ad, kilo)
        self.pul_rengi=pul_rengi
        print("Balik init çalıştı.")
    def ses_cikar(self):
        print("gluk gluk")



h1 = Hayvan("hayvan",10)
b1 = Balik("pıtır",0.5,"sarı")
k1 = Kedi("pıncır",8,4)

b1.ses_cikar()
k1.ses_cikar()

