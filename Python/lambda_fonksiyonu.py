
us_alma= lambda a:a**3
sonuc=us_alma(2)
print(sonuc)



toplama= lambda a,b,c: a+b+c
sonuc=toplama(4,10,16)
print(sonuc)



ters_cevir=lambda x: x[::-1]
sonuc=ters_cevir("Alperen Erdoğan")
print(sonuc)


def fn1(n):
    return lambda a:a ** n

us_alma= fn1(2)
sonuc=us_alma(5)
print(sonuc)