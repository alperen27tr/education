#Demetlerin(tuples) içindeki elemanlar değiştirilemez.

from itertools import count


thistuples=(2,3,"beş",4,True,4)
thistuples2=(1,3,"yedi",4,False,4)

print(type(thistuples))

print(thistuples[3])

print(len(thistuples))#len=listenin kaç elemanlı olduğunu gösterir.
print(thistuples.count(4))#.count=Listenin içinde kaç tane 4 var onu yazar.
print(thistuples+thistuples2)#İki demeti birleşik yaz.

list1=tuple([1,2,3,4,5,6])#Listeyi tuple çevirme.
print(type(list1))#17.satırın sağlaması.


