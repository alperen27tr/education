from datetime import datetime

simdi= datetime.now()
print(simdi)

sonuc=datetime.now()
sonuc0=simdi.year
sonuc1=simdi.day
sonuc2=simdi.month
sonuc3=simdi.hour
sonuc4=simdi.minute
sonuc5=simdi.second


print(sonuc,sonuc0,sonuc1,sonuc2,sonuc3,sonuc4,sonuc5)

birthday= datetime(2002,6,14,6,30,45)
simdi=datetime.now()
sonuc=datetime.timestamp(birthday)

sonuc= simdi - birthday 
print(sonuc)