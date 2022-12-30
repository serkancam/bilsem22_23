from random import choice
class Araba:
    def __init__(self,marka,renk,modeli,en_yuksek_hiz):
        self.marka=marka
        self.renk=renk
        self.model=modeli
        self.en_yuksek_hiz=en_yuksek_hiz
        self.__hiz=0 # dışarı kapalı bilgi

    def gaza_bas(self):
        if self.__hiz<=self.en_yuksek_hiz-10:
            self.__hiz+=10

    def frene_bas(self):
        if self.__hiz>=5:
            self.__hiz-=5
            
    def hiz_bilgisi(self):
        return self.__hiz
        

def renk_sec():
    liste=["mavi","kırmızı","siyah","sarı","gri","bej"]
    sec = choice(liste)
    return sec

def marka_sec():
    liste = ["mercedes","bmw","fiat","peugeot","ford","ferrari"]
    sec=choice(liste)
    return sec