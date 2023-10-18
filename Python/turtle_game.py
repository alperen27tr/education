import turtle
from unittest import result


#1.kaplumbaga
player_one=turtle.Turtle()
player_one.color("blue")
player_one.shape("turtle")
player_one.shapesize(2,2,1)
player_one.penup()
player_one.goto(-200,100)

#2.kaplumbaga
player_two=player_one.clone()
player_two.color("red")
player_two.shapesize(2,2,1)
player_two.penup()

#1.kaplumbaga evi
player_one.goto(200,-20)
player_one.pendown()
player_one.circle(30)
player_one.penup()
player_one.goto(-200,0)

#2.kaplumbaga evi
player_two.goto(200,-200)
player_two.pendown()
player_two.circle(30)
player_two.penup()
player_two.goto(-200,-170)


import random
die=[1,2,3,4,5,6]
for i in range(20):
  if player_one.pos()>=(200,-20): #birinci oyuncunun ev kordinatları verildi.bu kordinatlara gelir veya geçerse kazanır.
    print("Mavi Oyuncu Kazandı!!!")
    break
else:
    player_one_turn=input("Birinci oyuncu zar atmak için Enter'a basabilir...")
    result=random.choice(die)
    print("sonuç",result)
    print("Mavi kaplumbağanın ilerleyeceği adım sayısı:",result*10)
    player_one.fd(result*10)#zarda gelen sayının 10 katı kadar ilerler

    player_two_turn=input("İkinci oyuncu zar atmak için ENTER'a basabilir.")
    result=random.choice(die)
print("Sonuç",result)
print("Kırmızı kaplumbağanın ilerleyeceği adım sayısı",result*10)
player_two.fd(result*10)









input("ENTER tuşuna basarak çıkış yapabilirsiniz...")







