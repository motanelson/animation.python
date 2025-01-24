import time
"""
operation system simulator
"""
print ("\033c\033[43;30m\n")
class simu:
    def __init__(self):
        self.msg="operation system init....\n"
        self.write(self.msg)
    def write(self,msg):
        print(msg,end="")
    def shutdown(self):
        self.write("shutdown\n")
        time.sleep(1)
        self.write("turn pc off\n")
    def add(self,a,b):
        return a+b

s=simu()
s.write("hello world....\n")
s.write(str(s.add(10,10))+"\n")
s.shutdown()