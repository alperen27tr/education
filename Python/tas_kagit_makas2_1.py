import random

tas="tas"
kagit="kagit"
makas="makas"


def pc_secimi_uret():
    n=random.randint(1,3)
    if n==1:
        return(tas)
    elif n==2:
        return(kagit)
    else:
        return(makas)

skor_user=0
skor_pc=0

while True:
    u_secim=input("tas? kagit? makas? ")
    pc_secim=pc_secimi_uret()
    print("Bilgisayar: ",pc_secim)

    if pc_secim==u_secim:
        print("Berabere")
    elif pc_secim==tas and u_secim==kagit:
        skor_user += 1
        print("Raund'u kazandın")
    elif pc_secim==kagit and u_secim==makas:
        skor_user += 1
        print("Raund'u kazandın")
    elif pc_secim==makas and u_secim==tas:
        skor_user += 1
        print("Raund'u kazandın")
    else:
        skor_pc += 1
        print("Raund'u kaybettin")

    
    if skor_user==3 or skor_pc==3:
        break

if skor_pc>skor_user:
    print("Oyunu Kaybettin :( )")
else:
    print("Tebrikler Oyunu Kazandın :) ")

print("Siz: ",skor_user," VS Bilgisayar: ",skor_pc)
