def adin_ne():
    isim=input("Adinizi giriniz: ")
    return isim 

print("sisteme hosgeldiniz",adin_ne())



saat=14

def selamlama():
    if (saat<=12):
        return " Gunaydin",adin_ne,"Bey"
    elif (saat>=12) and (saat<18):
        return " iyi gunler", adin_ne,"Bey"
    else:
        return " iyi aksamlar",adin_ne,"Bey"

sonuc=selamlama()
print(sonuc)



    
      
    


