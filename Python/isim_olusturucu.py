import random

def name_creator():
    names=["Alp","Dilay","Yağız","Bilal","Zeynep","Sude","Hasan Su","Duru","Öykü","Tayyip"]
    
    surnames=["Ciddioğlu","Topcuoğlu","Sabancı","Erdoğan","Yağcıoğlu","Bayıcı",
              "Keleş","Küpcü","Cingöz","Usta","Kaptan","Reis"]
    
    return"{} {}".format(random.choice(names)),(random.choice(surnames))

for i in range (5):
        print(name_creator())

    