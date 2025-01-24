import time
print("\033c\033[43;30m\n")

class simu:
    def __init__(self):
        self.ground=1100
        self.speed=110
    def simulates(self):
        self.ground-=100
        self.speed-=10
        print(str(self.ground)+" KM from ground")
        print(str(self.speed)+" motor mode")
        if self.ground==0:
             print(" model landing....")
             return False
        else:
             return True


s=simu()
true=True
while true:
    true=s.simulates()
    time.sleep(1)
