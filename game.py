import time
print("\033c\033[43;30m\n")
class simu:
    def __init__(self):
        self.player=[]
        self.x=[]
        self.y=[]
    def add_player(self,s):
        self.player=self.player+[s]
        self.x=self.x+[0]
        self.y=self.y+[0]
    def play(self):
        for n in range(len(self.player)):
            self.x[n]+=1
            self.y[n]+=1
            self.write(self.player[n]+"="+str(self.x[n])+","+str(self.y[n])+" ")
        self.write("\n")
    def write(self,s):
        print(s,end="") 


counter=0
s=simu()
true=True
while true:
     time.sleep(1.5)
     s.add_player("player"+str(counter))
     s.play()
     counter+=1
     if counter>5:
         true=False
true=True
counter=0
while true:
     time.sleep(1.5)
     s.play()
     counter+=1
     if counter>20:
         true=False
        