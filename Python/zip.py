list1=[1,2,3,4,5]
list2=["bir","iki","uc","dort","bes"]
list3=["a","b","c","d","e"]

sonuc=list(zip(list1,list2,list3))
print(sonuc)

for item in zip (list1,list2,list3):
    print(item)



for x,y,z in zip (list1,list2,list3):
    print(x,y,z)