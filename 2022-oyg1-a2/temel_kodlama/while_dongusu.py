# başlangıç bitiş değişim

# 1 den 5 e kadar birer birer döngü ile yazalım

d = 1 # başlangıç
while d<=5: # döngü şartı,bitiş
    print(d)
    d=d+1 # değişim

print("döngü sonu")
# 10 dan 0 a kadar birer eksilen
for t in range(10,-1,-1):
    print(t)
print("döngü sonu")
s=10
while s>=0:
    print(s)
    s=s-1
print("döngü sonu")
# while 1==1:
#     print("selamlar!")

# aşağıdaki şekli döngü ile çizelim
# *
# **
# ***
# ****
# *****
a = 1
while a<=5:
    print("*"*a)
    a=a+1

print("döngü sonu.")

q=1
x=1
while q<=5:
    x=1
    while x<=5:
        print("q=",q,"x=",x)
        x=x+1
    q=q+1