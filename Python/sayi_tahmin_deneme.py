import random

sayi=random.randint(0,100)
tahmin=int(input("Tahmın: "))


def tahminn():
    global tahmin
    if sayi>tahmin:
       tahmin= int(input("Arttir"))

    if sayi<tahmin: 
        tahmin=int(input("Azalt"))

    if sayi==tahmin:
        print("...Tebrikler...")
        return   
    tahminn()

tahminn()

