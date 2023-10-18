a=10
b=20
c=30

a,b,c=10,20,30 
a,b=b,a #a'yı b'ye, b'yi a'ya eşitliyoruz.
print(a,b,c)


a=a+5 
#veya
b+=5 #bu yöntem daha sık kullanılır.
print(a,b,c)

a-=10
b*=3
c/=3
print(a,b,c)

a**=2 #üssü
b//=5 #tam bölme
c%=3 #bölümünden kalan
print(a,b,c)

sayılar=(1,2,3,4,5,6)
a,b,*c=sayılar #a ve b'ye ilk iki index, devamı liste şeklinde c'ye tanımlanır.
print(a,b,c)

sayılar0=(10,11,12,13,14,15)
a,*b,c=sayılar0 #a baştaki indexe c sondaki indexe tanımlanır. Ortada kalanlar b'ye tanımlanır.
print(a,b,c)

sayılar1=(10,20,30,40,50,60)
*a,b,c=sayılar1 #b sondan bir önceki indexe, c sondaki indexe tanımlanır. a ise ilk 4e tanımlanır. 
print(a,b,c)
