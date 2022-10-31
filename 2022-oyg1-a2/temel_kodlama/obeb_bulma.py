# obeb_bulma.py
x = int(input("bir sayı giriniz:"))
y = int(input("bir sayı giriniz:"))

bolen = min(x, y)

while True:
    if x % bolen == 0 and y % bolen == 0:
        break
    bolen -= 1  # bolen=bolen-1

print(f"{x} ve {y} ebob değeri= {bolen}")

# öklit algoritması
ks = min(x,y)
bs = max(x,y)
k=-1

while k != 0:
    k=bs%ks
    bs=ks
    ks=k

print(f"öklit-->{x} ve {y} ebob değeri= {bs}")