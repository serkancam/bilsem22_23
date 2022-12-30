

#tanımlama(1kere)
def ilk_fonksiyon():
    print("ben ilk fonksiyonum")

def kareler_farki(s1,s2):
    hesap = s1**2 - s2**2
    print(hesap)

def dikdortgen_alani_bul(kk,uk):
    alan = kk*uk
    print("alan:",alan)

def diktortgenprizma_hacmi_bul(at1,at2,at3):
    hacim = at1*at2*at3
    print(hacim)
#çağırma(sınırsız)
ilk_fonksiyon()
ilk_fonksiyon()
ilk_fonksiyon()

kareler_farki(2,3)
kareler_farki(10,5)
kareler_farki(100,55)

dikdortgen_alani_bul(3,5)
dikdortgen_alani_bul(13,45)
dikdortgen_alani_bul(38,52)
#isimle çağırma
diktortgenprizma_hacmi_bul(at2=5,at3=10,at1=8)
diktortgenprizma_hacmi_bul(3,5,8)
diktortgenprizma_hacmi_bul(3,at3=5,at2=8)
#diktortgenprizma_hacmi_bul(at3=3,5,8)# yasak işlem isimle gönderme başlarsa sağdakilere de isimle gitmeli

