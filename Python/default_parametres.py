


def selamlama(isim="Kullanici",mesaj="Hosgeldin"):
    print( f"{mesaj}, {isim} ")

selamlama("selam","alperen")
selamlama("mehmet") 
selamlama()



def carpma(a,b):
    aa=b-a
    bb=aa*a*b
    return bb+44

def toplama(a,b):
    return(a+b)

def islem(a,b,fn):
    return fn(a,b)

son = carpma(4,8)
print(son)

son2 = carpma(3,8)
print(son2)

sonuc=islem(10,20,carpma)
print(sonuc)



