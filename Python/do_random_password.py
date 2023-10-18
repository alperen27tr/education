import random
import string

uzunluk=int(input("Şifreniz kaç karakterden oluşsun? "))

def password(uzunluk):
    karakter_tipi= string.ascii_letters + string.digits

    r_password=""

    for i in range(uzunluk):
        r_password+= random.choice(karakter_tipi)

    return(r_password)

r_password=password(uzunluk)
print("Şifreniz: ", r_password)
    




