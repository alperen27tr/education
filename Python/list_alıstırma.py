name=["Alp","eren","alper","zeynep","dilay","yağız","tarık"]
numbers=[1,3,5,7,9,11,13,15,17,17,17]

name.append("Selma")
print(name)

numbers.append(19)
print(numbers)

numbers.pop(4)
print(numbers)

numbers.insert(0,-1)
print(numbers)

name.insert(0,"tr") 
print(name)

#name.clear()
#print(name)

name.copy()
print(name)

sonuc=numbers.count(17) #kaç defa 17 geçiyor
print(sonuc)

name.extend(numbers) #listeleri birleştir
print(name)


