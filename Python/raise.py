#! /usr/bin/env python
#! _*_coding: UTF8 _*_



def users(username,city):
    citys=["İstanbul","Ankara","İzmir","Kayseri"]
    if type(username) is not str:
        raise TypeError("username str tipinde olmalıdır.")
    if type(city) is not str:
        raise TypeError("city str tipinde olmalıdır.")
    if city  not in citys:
        raise ValueError("lütfen geçerli bir şehir giriniz")
    
    
try:
    users("Alperen","Kayseri")
    
except Exception as e:
    print(e)
    
else:
    print("Bilgiler başarıyla kaydedildi...")