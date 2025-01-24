import time
import datetime
import random
"""
stock simulator.....
"""
print ("\033c\033[43;30m\n")
class simu:
    def __init__(self):
        self.total=int(600.00)
        self.count=int(0)
        self.write(str(self.total)+"\n")
    def report(self):
        f=self.getmov()
        self.total=self.total+f
        self.write(self.strret(str(datetime.datetime.now()),20)+"|"+self.strret("trans."+str(self.count),15)+"|"+self.strret(str(int(f)),15)+"|"+self.strret(str(int(self.total)),15)+"\n")
        self.count+=1
    def strret(self,s,a):
       b="                                                                                                            "
       bb=s+b
       bb=bb[:a]
       return bb
    def getmov(self):
        r=random.randint(0,60000)
        f=float(r)/100
        f=f-300
        return int(f)  
    def write(self,msg):
        print(msg,end="")
    def add(self,a,b):
        return a+b

s=simu()
s.write("start....\n")
while True:
    s.report()
    time.sleep(1.5)