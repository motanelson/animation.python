import random 
import time
print("\033c\033[43;30m")
class lotos:
    def __init__(self):
        self.numbers=[]
        self.pc=[]
        self.pcs=[]
        self.correct=[]
        for n in range(51):
            self.pcs=self.pcs+[n+1]
        
    def input(self):
        
        n=input("give me 5 numbers separete 1 to 50, comma ? ")
        numbers=[]
        self.numbers=n.split(",")
        if len(self.numbers)<5:
            print("error nembers")
            return None
        self.numbers=self.numbers[0:5]
        for n in self.numbers:
            numbers=numbers+[int(n)]
        self.numbers=numbers
        print(self.numbers)
        return 0
    def gen(self):
        self.pc=[]
        
        
        
        for n in range(5):
            t=random.randint(0,49)
            
               
            c=self.pcs[t]
            self.pc=self.pc+[c]    
        
        
    def play(self):
        self.gen()
        self.correct=[]
        print(self.pc)
        for n in self.pc:
            for nn in self.numbers:
                if nn==n:
                    self.correct=self.correct+[n]
        print(self.correct)
        
maxss=50
l=lotos()
if (l.input()!=None):
     for n in range(maxss):
         l.play()
         time.sleep(3)
else:
    print("error on give numbers ? ")