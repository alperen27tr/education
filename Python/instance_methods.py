class User:
    def __init__(self,username,name,surname,birthday):
        self.username=username
        self.name=name
        self.surname=surname
        self.birthday=birthday
        
         
    def info(self):
        return "Alperen" + self.name +"Alp"
    
    
        
u1=User("alperen.27.tr","Alperen","Erdogan","2002")


print(u1.info())


        