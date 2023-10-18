#! /usr/bin/env python
#! _*_coding: UTF8 _*_

import math

sonuc=dir(math)
print(sonuc)
sonuc1= help(math.copysign)#fonksiyon nasıl kullanılır bilgi verir.
print(sonuc1)

sonuc2=math.sqrt(36) #karekök alır.
print(sonuc2)


sonuc3=math.factorial(5) #faktöryel alır.
print(sonuc3)

import math as islem # math yerine artık islem yazabiliriz.

sonuc4=islem.copysign(9,4)
print(sonuc4)
