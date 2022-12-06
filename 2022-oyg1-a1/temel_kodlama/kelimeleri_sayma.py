import re
import string

dosya = open("/home/serkan/Belgeler/yillar/2022-2023/bilsem22_23/2022-oyg1-a1/temel_kodlama/metin1.txt",mode="r",encoding="utf-8")

metin = dosya.read()
dosya.close()

metin=metin.lower()

noktalama= string.punctuation


metin=re.sub(r"[^\w\s]", "", metin)
# for kelime in metin.split():
#     print(kelime)

kelimeler = dict()

for kelime in metin.split():
    if kelime not in kelimeler.keys():
        kelimeler[kelime]=1
    else:
        kelimeler[kelime]+=1

# print(kelimeler)    

dosya = open("kelimeler.txt","w+",encoding="utf-8")
for k in kelimeler.keys():
    yaz = str(k)+" : "+str(kelimeler[k])+"\n"
    dosya.write(yaz)
dosya.close()