import random

tas="Taş"
kagit="Kağıt"
makas="Makas"

secim_user=input("Taş? Kağıt? Makas? ")

def pc_secim():
    n= random.randint(1,3)

    if n==1:
        return("Taş")
    elif n==2:
        return("Kağıt")
    else:
        return("Makas")
    
def h_pc_secim(secim_user):

    if secim_user== "Taş":
        return "Kağıt"

    elif secim_user=="Kağıt":
        return "Makas"
    
    else :
        return "Taş"
    
secim_pc=h_pc_secim(secim_user)
print(secim_pc)

pc_puan=0
user_puan=0

while True:

    if secim_user==secim_pc:
        print("Berabere ")

    elif secim_user==tas and secim_pc==kagit:
        pc_puan+=1
        print("Bu turu bilgisayar Kazandı ")


    elif secim_user==tas and secim_pc==makas:
        user_puan+=1
        print("Bu turu siz kazandınız ")

    elif secim_user==kagit and secim_pc==tas:
        user_puan+=1
        print("Bu turu siz kazandınız ")

    elif secim_user==kagit and secim_pc==makas:
        pc_puan+=1
        print("Bu turu bilgisayar Kazandı ")

    elif secim_user==makas and secim_pc==tas:
        pc_puan+=1
        print("Bu turu bilgisayar Kazandı ")

    else:
        user_puan+=1
        print("Bu turu siz kazandınız! ")

    #print("Sizin puanınız: ", user_puan "VS Bilgisayar Puanı:  ", pc_puan)

    if user_puan==3 or pc_puan==3:
        break 

if user_puan>pc_puan:
    print("Tebrikler ")
else :
    print("Hahahhahahaha Tekrar Dene")