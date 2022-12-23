# parametre/arguman

# tanımlama bir kere
def ilk_fonksiyon():
    print("ben ilk fonskiyon")

def kare_farki_bul(a,b):
    kf = a**2 - b**2
    print(kf)

def dikdortgen_alani_bul(kk,uk):
    alan = kk*uk
    print("dikdörtgen alanı:",alan)

def ucgen_ucuncu_acisi_bul(aci1,aci2):
    aci3=180-(aci1+aci2)
    print("3. açı:",aci3)
# çağrılma sonsuz kere yapılabilir

ilk_fonksiyon()
ilk_fonksiyon()
ilk_fonksiyon()
ilk_fonksiyon()

kare_farki_bul(5,2)
kare_farki_bul(15,12)
kare_farki_bul(51,22)

dikdortgen_alani_bul(8,3)
dikdortgen_alani_bul(81,13)

ucgen_ucuncu_acisi_bul(50,75)
