liste=[12,125,36,45,58,58]

toplam = 0 #int()
i=0
uzunluk=len(liste)
while i<uzunluk:
    toplam+=liste[i] # toplam=toplam+liste[i]
    i+=1#i=i+1
print(toplam)
print(30*"*")
toplam1=0
for d in liste:
    toplam1+=d
print(toplam1)

# 30 dan 3 kadar (30 ve 3 dahil) üçer üçer geri sayarak her adımdaki sayıları ekrana yazdıran python kodunu yazınız.
print(30*"*")
s=30

while s>=3:
    print(s)
    s=s-3
print(30*"*")
for t in range(30,2,-3):
    print(t)