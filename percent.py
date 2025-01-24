import time
print("\033c\033[43;30m\n")

class perc:
    def __init__(self,size,s):
        self.size=size
        self.prog=0
        self.char=s
        self.tsizes=float(size/100)
    def progress(self,prog):
        if prog<=100:
            if self.prog<=prog:
                nn=prog
                self.prog=prog
                nnn=int(nn*self.tsizes)
                c=self.char*nnn
                print(c)
                print(str(self.prog)+" % ")
            else:
                print("error")
        else:
            print("error")
            return False

        if prog>=100:
            return False
        else:
            return True
true=True
p=[0,10,20,30,40,50,60,70,80,90,100,100]
percs=perc(50,".")
print("")
for n in p:
    print("\033c\033[43;30m")
    percs.progress(n)
    time.sleep(2)