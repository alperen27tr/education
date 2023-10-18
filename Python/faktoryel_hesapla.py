
#encapsulation -- kapsulleme 

def dis_fonksiyon(sayi1):
    print("dis fonksiyon calisti ")
    def ic_fonsiyon(sayi1):
        print("ic fonksiyon calisti ")
        return  sayi1**2
    sayi2=ic_fonsiyon(sayi1)
    print(sayi1,sayi2)
    
dis_fonksiyon(10)
    
number=input("sayi: ")
def faktoriyel(number):
    if not isinstance(number,int):
        raise TypeError("Girdiginiz  sayi tam sayi olmalidir.")
    if not number >=0:
        raise ValueError("Girdiginiz sayi 0 dan buyuk olmalidir.")
        
    def ic_faktoriyel(number):
        if number <= 1:
            return 1
        return number * ic_faktoriyel(number -1)
    return ic_faktoriyel(number) 
try:
    print(faktoriyel(number))
except Exception as e:
    print(e)
    
    