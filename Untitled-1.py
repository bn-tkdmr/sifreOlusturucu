import random

karakterler ="dfghjklgr5678kgy789o"
sifreUzunlugu = int(input("uzukuğu gir"))

sifre = ""

for i in range(sifreUzunlugu):
    sifre += random.choice(karakterler)

print("Şifreniz: ",sifre)    