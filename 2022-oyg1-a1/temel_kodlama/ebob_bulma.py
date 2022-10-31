x = int(input("bir sayı giriniz:"))
y = int(input("bir sayı giriniz:"))
bolen = min(x, y)
print(bolen)
adim1=0
adim2=0
while True:
    adim1+=1
    if x % bolen == 0 and y % bolen == 0:
        break
    bolen -= 1  # bolen=bolen-1
print(f"{adim1}--> adım {x} ve {y} ebob değeri={bolen}")
#öklit
kucuk=min(x,y)
buyuk=max(x,y)
kalan=-1
while kalan!=0:
    adim2+=1
    kalan=buyuk%kucuk
    buyuk=kucuk
    kucuk=kalan

print(f"{adim2}--> adım {x} ve {y} ebob değeri={buyuk}")