def UserInfo(*args): # tuple tipinde liste alınır.
    print(type(args))

UserInfo()

def UserInfo(**kwargs):
    print(kwargs) # **kwargs sayesinde dictionary tipinde liste alınır.

UserInfo(username="alperen27")
UserInfo(username="alperen27",password="alperen0",gmail="alperen@gmail.com") #key vallue şeklinde listeler.


def KullanıcıBilgisi(**kwargs):
    for key,vallue in kwargs.items():
        print(f"{key},{vallue}")
        print("\n")                #terminalde satırlar arası boşluk bırakır.

KullanıcıBilgisi(username="alperen27",password="alperen0",gmail="alperen@gmail.com")


