import random
print("\033c\033[43;30m\n")

class rnds:
    def __init__(self):
        self.numbers=[]
    def gen(self,mins,maxs,counts):
        for n in range(counts):
            nn=random.randint(mins,maxs)
            self.numbers=self.numbers+[nn]
    def report(self):
        print(len(self.numbers))
        for n in self.numbers:
            print(n)


r=rnds()
r.gen(0,100,100)
r.report()