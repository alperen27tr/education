class User:
    
    ActiveUsers=0
    
    def __init__(self,username,name,surname,age):
        self.username=username
        self.name=name
        self.surname=surname
        self.age=age
        User.ActiveUsers+=1
        
    def usernameX(self):
        return (self.username)
    
    def logaout(self):
        User.ActiveUsers-=1
        return self.username +" sistemden cikis yapti."
        
    
    
print({User.ActiveUsers})
u1= User("alperen27tr","alperen","erdogan",20)
u2= User("dly_38","dilay","erdogan",16)
u3= User("alperen27tr","alperen","erdogan",20)
print(u1.usernameX())
print(u2.logaout())
print(User.ActiveUsers)