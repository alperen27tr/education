import os
#dizin degistirme
os.chdir("..")
sonuc= os.getcwd()#os_module.py'den masaustune gectik.
print(sonuc)

os.chdir("../..")#iki dizin kaydik.
sonuc0= os.getcwd()
print(sonuc0)

os.chdir("//users")#dogrudan users klasorunun icine girdik.
sonuc1=os.getcwd()
print(sonuc1)

#os.makedirs("deneme/python_kurs")

sonuc2=os.listdir("//users")#sadece users icindekileri listeler.
print(sonuc2)

for dosya in os.listdir("PYTHON"):
    if dosya.endswith(".py"):
        print(dosya)
        
sonuc3=os.stat("hesap_makinesi.py")
sonuc3=sonuc3.st_size/1024
print(sonuc3)