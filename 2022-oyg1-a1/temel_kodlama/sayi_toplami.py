from random import randint
sayilar=[randint(1,1000) for i in range(100)]

#########################

toplam=0
for sayi in sayilar:
    toplam=toplam+sayi
print(toplam)
