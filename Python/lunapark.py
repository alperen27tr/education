print("Lunapark'a Hoşgeldiniz")

boy=input("Lütfen boyunuzu giriniz: ")
 
if int(boy)>=120:
    print("Girebilirsiniz..")
    yas=input("Yaşınız:")
    if int(yas)<12:
        print("Ücretiniz 20 TL")
    
    elif int(yas) <=18:
            print("Ücretiniz 30 TL")
    else:
            print("Ücretiniz 40 TL")


else:
    print("Boy şartımızı sağlamadığınızdan giremezsiniz.")    

