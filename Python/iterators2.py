
class Counter:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
        
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
        
        
#for i in Counter(1,10):
#    print(i)

iterator=iter(Counter(20,40))  

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
        
        
        
        