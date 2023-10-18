
tas="1"
kagit="2"
makas="3"

puan=0

while True:
    
    secim=input("1-Tas? 2-Kagıt? 3-Makas?")
    
    
    if secim==tas:
        print("Bu Raund'u Kaybettin! Bilgisayar seçimi :",kagit)
        puan += 1

    if secim==kagit:
        print("Bu Raund'u Kaybettin! Bilgisayar seçimi :",makas)
        puan += 1

    if secim==makas:
        print("Bu Raund'u Kaybettin! Bilgisayar seçimi :",tas)
        puan += 1
    
    if puan==3:
        print("HAHAHAHAHAHHAA ulan 1 Raund kazanaydın bari..")
        break