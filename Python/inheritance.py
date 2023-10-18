
class Person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname=surname
        self.age=age
        print("person nesnesi olusturuldu.")
    
    def info(self):
        print(self.name,self.surname,self.age)
        

class Student(Person): # "(Person)" sayesinde person class'indaki bilgileri Student class'inda kullanabilecez.
    def __init__(self,name,surname,age,number):
        Person.__init__(self,name,surname,age)
        self.number=number
        print("Student nesnesi olusturuldu.")
        

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        Person.__init__(self,name,surname,age)
        self.branch=branch
        print("teacher nesnesi olusturuldu")

p1=Person("alperen","erdogan",20)
p1.info()

s1=Student("dilay","erdogan",16,9876543210)
s1.info()
print(s1.number)

t1=Teacher("yagiz","erdogan",35,"Math")
t1.info()
print(t1.branch)