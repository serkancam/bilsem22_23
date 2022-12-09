from random import choice
pc=["taş","kağıt","makas"]

secim_pc=choice(pc)

while True:
    secim_insan =input("taş kağıt makas birini yazınız:")
    if secim_insan.lower()  in pc:
        break

print("insan:",secim_insan)
print("pc:",secim_pc)

if secim_insan=="taş" and secim_pc=="kağıt":
    print("\n pc kazandı")
elif secim_insan=="taş" and secim_pc=="makas":
    print("insan kazandı")
elif secim_insan=="kağıt" and secim_pc=="taş":
    print("insan kazandı.")
elif secim_insan=="makas" and secim_pc=="taş":
    print("pc kazandı.")
elif secim_insan=="makas" and secim_pc=="kağıt":
    print("insan kazandı.")
elif secim_insan=="kağıt" and secim_pc=="makas":
    print("pc kazandı.")
else:
    print("beraberlik")