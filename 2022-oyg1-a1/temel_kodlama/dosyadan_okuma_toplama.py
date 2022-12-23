# kullanıcının adını girdiği ve program ile aynı dizinde olan dosyadaki
# var olan sayıların hepsinin toplamını bulan kodu yazalım

import os

dosya_adi =input("dosya adını giriniz:")

su_andaki_konum=os.getcwd()

dosya_yolu = os.path.join(su_andaki_konum,"temel_kodlama",dosya_adi)

try:
    #dosyaya bağlantı kur
    dosya = open(dosya_yolu,mode="r",encoding="utf-8")# r w a r+ w+ a+
    # dosyadaki verileri oku
    metin = dosya.read()
    print(metin)
except FileNotFoundError:
    print("dosya yok")
else:
    # dosyayı kapat
    dosya.close()
    print("dosya kapandı.")

degerler=metin.split(" ")
print(degerler)

toplam=0

for d in degerler:
    if d.isnumeric():
        toplam=toplam+int(d)

print(toplam)
