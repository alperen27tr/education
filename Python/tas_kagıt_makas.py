import random

tas = "Taş"
kagit = "Kağıt"
makas = "Makas"


def pc_secim():
    n = random.randint(1, 3)

    if n == 1:
        return tas
    elif n == 2:
        return kagit
    else:
        return makas


secim_user = input("Taş? Kağıt? Makas? ")

secim_pc = pc_secim()
print(secim_pc)

if secim_user == secim_pc:
    print("Berabere ")

if secim_user == tas and secim_pc == kagit:
    print("Bilgisayar Kazandı ")

if secim_user == tas and secim_pc == makas:
    print("Tebrikler Kazandınız! ")

if secim_user == kagit and secim_pc == tas:
    print("Tebrikler Kazandınız! ")

if secim_user == kagit and secim_pc == makas:
    print("Bilgisayar Kazandı ")

if secim_user == makas and secim_pc == tas:
    print("Bilgisayar Kazandı ")

if secim_user == makas and secim_pc == kagit:
    print("Tebrikler Kazandınız! ")
