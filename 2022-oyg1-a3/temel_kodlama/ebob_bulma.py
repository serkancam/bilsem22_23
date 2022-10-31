#ebob_bulma.py

x=int(input("bir sayı giriniz:"))  
y=int(input("bir sayı giriniz:")) 
adim1=0
adim2=0 

bolen= 0 # min(x,y)
if x<y:
    bolen=x
else:
    bolen=y

while True:
    adim1=adim1+1
    if x%bolen==0 and y%bolen==0:
        break
    bolen=bolen-1
    #bolen-=1

print(f"{adim1}-->{x} ve {y} değerlerinin ebobu={bolen}")

# öklit algoritması

bs = max(x,y)
ks = min(x,y)
k=-1

while k != 0:
    adim2=adim2+1
    k = bs%ks
    bs=ks
    ks=k

print(f"{adim2}-->{x} ve {y} değerlerinin ebobu={bs}")
# 9967, 9973

