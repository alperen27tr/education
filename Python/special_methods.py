
class urun:
    def __init__(self,UrunKodu,UrunAdi,UrunFiyati):
        self.UrunKodu=UrunKodu
        self.UrunAdi=UrunAdi
        self.UrunFiyati=UrunFiyati
    
    def __len__(self):
        return self.UrunFiyati
    
    def __str__(self):
        return self.UrunAdi 
    
    def __repr__(self):
        return self.UrunKodu
    
    def __del__(self):
        print("urun silindi.")
   
    
    
urun1=urun("2394994032","PC",20000) 

print(len(urun1))
print(str(urun1))
print(repr(urun1))
del urun1        