yazı="Benim adım Alperen soyadım ise ERDOĞAN"
sonuc0=yazı.upper() #Bütün harfleri büyük yazar.
sonuc1=yazı.lower() #Bütün harfleri küçük yazar.
sonuc2=yazı.title() #Baş harfleri büyük yazar.
sonuc3=yazı.capitalize() #Sadece cümlenin ilk harfini büyük yazar.
sonuc4=yazı.islower() #Bütün harfler küçükmü sorusuna cevap verir.
sonuc5=yazı.isupper() #Bütün harfler büyükmü sorusuna cevap verir.
sonuc6="-".join(yazı) #Bütün harflerin arasına"-"koyar.
sonuc7=yazı.replace("i","ı").replace("Ğ","G")#Harfleri değiştirir.
#Daha fazla metot için www.w3schools.com



print(sonuc0,sonuc1,sonuc2,sonuc3,sonuc4,sonuc5,sonuc6,sonuc7)