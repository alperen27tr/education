
city="istanbul"
def dıs_fonksiyon(): #fonksiyon içinde tanımlanan değişken sadece fonksiyn içinde geçerlidir.
                     #dıs_fonksiyonda tanımlanan izmir stringi ic_fonksiyonda tanımlanmaz.
    city="izmir"

    def ic_fonksiyon():
        city="ankara"
        print(city)

    ic_fonksiyon()
    print(city)

dıs_fonksiyon()
print(city)

