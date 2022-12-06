from random import choice

dosya = open("/home/serkan/Belgeler/yillar/2022-2023/bilsem22_23/2022-oyg1-a1/temel_kodlama/sehirler.txt","r", encoding="utf-8")

sorular = dosya.read().split()

dosya.close()

soru = choice(list(sorular))
print(soru)







