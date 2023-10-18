print("""--------------------------------------------------------------       
       Alp Sinemalarına Hoşgeldiz!             
Sinema yetişkin: 30 TL, Sinema öğrenci: 15 TL, Tiyatro yetişkin: 50 TL, Tiyatro öğrenci:25 TL... 
""")

a1=int(input("Lütfen yaşınızı giriniz: "))
a2=input("""
sinema için: 1 
tiyatro için: 2 
""")
tutar=0

if a2 == "1":
    if a1 >= 18:
        tutar=+30
    else:
        tutar=+15

if a2 == "2":
    if a1 >= 18:
        tutar=+50
    else:
        tutar=+25

print(f'ödenecek tutar: ' ,(tutar) ,"TL")

    
