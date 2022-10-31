s1=12
s2=20.45
s3=int()
s1=s1+1
print(f"merhaba {s1} günü saat {s2} den başlayarak dersimiz var.")
print("merhaba",s1,"günü saat",s2,"den başlayarak dersimiz var.",sep="_",end="\n")

# kullanıcıdan adını yaşını boy ve kilosunu alarak
# ekrana bki indeks değerini hesaplayıp yazdırdan kodu yazınız
# boy metre, ağırlıkta kg cinsinden olmalı
# bki(boy/kilo indeksi) değeri ağırlık değerinin boy değerinin karesine bölünerek khesaplanır.

ad=input("adınızı giriniz:")
boy=float(input("boy uzunluğunuzu metre cinsinden giriniz:"))
agirlik=float(input("ağırlık değerinizi kg cinsinden giriniz:"))
bki=agirlik/(boy*boy)
print(f"sayın {ad} bki değeriniz={bki}")

