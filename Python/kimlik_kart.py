

class kimlik():
    def __init__(self,TCno,isim,soyisim):
        self.Tcno=TCno
        self.isim=isim
        self.soyisim=soyisim

list=[]


while True:
    
    istenen_islem=input("""
Yeni kayıt için: 1
Tüm kayıtları görüntülemek için: 2
TC numarasınsa göre isim sorgulamak için: 3
Kayıtlı kişi sayısını görmek için: 4
Tüm kayıtları silmek için: 5
Çıkış yapmak için: 6
""")

    if istenen_islem=="1":
        try:
            isim=input("İsim: ")
            soyisim=input("Soy İsim: ")
            Tcno=int(input("TC NO: "))
            yeniKisi = kimlik(Tcno,isim,soyisim)
            list.append(yeniKisi)
        except ValueError:
            print("Lütfen rakamlardan oluşan bir değer girin! ")
        else:
            print("Yeni kişi oluşturuldu..")
        
    if istenen_islem=="2":
        for kayit in list:
            print(kayit.isim,kayit.soyisim,kayit.Tcno)

    if istenen_islem=="3":
        arama=input("TC: ")
        bulundu =0
        for kayit in list:
            if kayit.Tcno == arama:
                print(kayit.isim)
                bulundu = 1

                break
        if bulundu!=1:
           print("Kayıt bulunamadı..")

    if istenen_islem=="4":
        a= len(list)
        
        print(f'Kayıtlı kişi sayısı: {a} ')


    if istenen_islem=="5":
        list.clear()
        print("Kayıtlar Silindi..")

    if istenen_islem=="6":  
        print("Çıkış Yapıldı..")  
        break
        
        

       
        
            
