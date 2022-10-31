# ebob_bulma.py
x = int(input("sayı giriniz:"))
y = int(input("sayı giriniz:"))
bolen = 0
if x < y:
    bolen = x
else:
    bolen = y

# bolen=min(x,y)

while True:
    if x % bolen == 0 and y % bolen == 0:
        break
    bolen = bolen-1

print(f"{x} ve {y} değerlerinin obebi= {bolen}")

bs = max(x,y)
ks = min(x,y)
k=-1 # 0 dan farklı her sayı olur

while k!=0:
    k=bs%ks
    bs=ks
    ks=k

print(f"{x} ve {y} değerlerinin obebi= {bs}")