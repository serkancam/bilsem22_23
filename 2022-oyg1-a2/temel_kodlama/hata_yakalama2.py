# hata_yakalama2.py
# kod yapısındaki özel durum hatası

try:
    a = int(input("a değerini giriniz:"))
    b = int(input("b değerini giriniz:"))
    c=a/(b-7)
    print("c:",c)
except ValueError:
    print("girilen değer tam sayı değil.")
except ZeroDivisionError:
    print("sıfıra bölme hatası b 7 olmaz")