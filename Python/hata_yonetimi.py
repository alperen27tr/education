#! /usr/bin/env python
#! _*_coding: UTF8 _*_

from ast import Break


while True: #Döngüye aldık. Yanlış veri girilirse tekrar soracak.
    try:
        a=int(input("a: "))
        b=int(input("b: "))
        print(a/b)
        
    except ZeroDivisionError:  
        print("b sayısı 0 olamaz")
        
    except NameError as e :#as e kodu programcıya hatanın kaynagını belirtir.
        print("Sadece sayısal veri giriniz")
        print(e)

    except Exception: #yukarıdaki hatalar dışında hata oluşursa burası çalışır.
        print("Bilinmeyen bir hata oluştu")

    else:
       break
    finally:
        print("finally blogu çalıştı")    #bu blok hata alınsa da alınmasa da çalışır.
        