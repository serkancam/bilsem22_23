x = int(input("sayı giriniz:"))
y = int(input("sayı giriniz:"))

bolen = min(x, y)
adim1=0
adim2=0
while True:
    adim1+=1
    if x % bolen == 0 and y % bolen == 0:
        break  # break komutu kendine üstten en yakın while veya for döngüsünü sonlandırır
    bolen -= 1  # bolen=bolen-1

print(f"{adim1}-->{x} ve {y} değerlerinin obebi= {bolen}")

#öklit
bs=max(x,y)
ks=min(x,y)
k=-1

# while True:
#     k=bs%ks
#     bs=ks
#     ks=k
#     if k==0:
#         break
while k!=0:
    adim2+=1
    k=bs%ks
    bs=ks
    ks=k
print(f"{adim2}-->{x} ve {y} değerlerinin obebi= {bs}")
