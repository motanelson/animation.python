import random
import time
print("\033c\033[43;30m\n")
class simu:
    def __init__(self):
        self.value=0
    def report(self,value):
        self.write(self.conv(value,1)+" "+self.conv(value,2)+" "+self.conv(value,4)+" "+self.conv(value,8)+" \n")
    def conv(self,value,divs):
        return str(value//divs)
    def write(self,s):
        print(s,end="")
    def gen(self):
        n=random.randint(0,100)
        self.report(n)


s=simu()
true=True
while true:
     s.gen()
     time.sleep(1.5)