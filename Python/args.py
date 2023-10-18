numbers=[5,10,15,20,25]

def topla (a,b):
    return a+b

def topla (a,b,c):
    return a+b+c

def topla (sayılar):
    sonuc=0
    for i in sayılar:
       sonuc +=i
    return f"sayıların toplamı:", sonuc 

print(topla(numbers))




def topla (*args): # *args sayesinde istediğimiz kadar parametre girebiliriz.
    sonuc1=0
    for i in args :
        sonuc1+=i
    return f"Sayıların Toplamı:",sonuc1
print(topla(5,10,23,45,56))



