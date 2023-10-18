#! /usr/bin/env python
#! _*_coding: UTF8 _*_


yaslar=[5,8,18,23,45,64]
def yetiskinmi(x):
    if x<18:
        return False
    else :
        return True

sonuc= list(filter(yetiskinmi,yaslar)) #filter sayesinde 18den küçükleri listeye almadık.
print(sonuc)

#----------------------------------

sayılar=[2,5,6,13,34,45]
sonuc=list(filter(lambda x: x%2==1,sayılar)) #tek sayıları aldık
print(sonuc)

#-----------------------------------

isimler=["alperen","ismet","sinem","ahmet","cafer"]
sonuc=list(filter(lambda n: n[0]=="a",isimler))
print(sonuc)

#-----------------------------------

users= [ 
    {"username" : "alperen.27.tr", "posts":["post1"]},
    {"username" : "alperen_erdogan", "posts":[]}

]
sonuc=list(filter(lambda u: len(u["posts"])>0,users))
print(sonuc)