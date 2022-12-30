import kutuphane

import kutuphane as ktp # ktp takma adı verdik

from kutuphane import renk_sec,marka_sec

from kutuphane import Araba

marka1 =kutuphane.marka_sec()
renk1 = kutuphane.renk_sec()

marka2=ktp.marka_sec()
renk2=ktp.renk_sec()

marka3=marka_sec()
renk3=renk_sec()

araba1 = Araba(marka1,renk1,2017,180)
araba1.__hiz=100#bu mantıklı değil. pythonun azizliği
araba1.gaza_bas()
araba1.gaza_bas()
araba1.gaza_bas()
araba1.frene_bas()
print("araba hızı:",araba1.hiz_bilgisi())
print("yok olan hız",araba1.__hiz)
print(marka1,renk1)
print(marka2,renk2)
print(marka3,renk3)