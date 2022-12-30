#hata_yakalama1.py

#1. kullanıcı girişi hatası
#2. kodun kendine özgü değer hatası
#3. sistem kaynağı(internet,disk vb.) hatası(örneğin olmayan dosyaya bağlanma)


try:#hatalı olabilme ihtimali olan kodlar buraya
    sayi1 = int(input("sayı giriniz:"))
    print(sayi1)
except Exception as ex:#hatalı duurumda yapıalcakalr
    print("hata var",ex)
else:#hata olmadan yapıalcakler
    print("hata yokmuş.")
finally:# hata
    print("ben her türlü çalışırım.")
#şu noktdan sonra devam eder
print("hatadan kurtuldum.")