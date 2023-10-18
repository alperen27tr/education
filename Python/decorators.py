
def selamlama(fn):
    def inner(ad):
        print("Programa hosgeldiniz ")
        fn(ad)
        print("Gorusmek uzere ")
    return inner


@selamlama
def gunaydin(ad):
    print("Gunaydin "+ ad )
        
@selamlama
def iyigunler(ad):
    print("Iyi gunler "+ ad)
    
@selamlama 
def iyiaksamlar(ad):
    print("Iyi aksamlar " + ad)
    
iyiaksamlar("alp")    
iyigunler("eren")
gunaydin("alper")