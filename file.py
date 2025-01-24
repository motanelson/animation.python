import time
print("\033c\033[43;30m\n")
class simu:
    def __init__(self):
        self.name=[]
        self.text=[]
    def load(self,files):
        f1=open(files,"r")
        content=f1.read()
        f1.close()
        content=content.split("|")
        for n in content:
            try:
                m=n.split("#")
                
                m0=m[0]
                m1=m[1].replace("\\n","\n").replace("\\r","\r")
                self.name=self.name+[m0]
                self.text=self.text+[m1]
            except:
                pass
    def save(self,files):
        content=""
        l=len(self.name)
        for n in range(l):
            if n!=0:
                content=content+"|"
            content=content+self.name[n]
            content=content+"#"+self.text[n]
        f1=open(files,"w")
        f1.write(content)
        f1.close() 
                
    def ls(self):
        for n in self.name:
            print(n)
    def cat(self,files):
        r=0
        for n in self.name:
            if n==files:
                print(self.text[r])
            r=r+1
    def news(self,files,text):
        r=True
        counter=0
        l=len(self.name)
        for n in self.name:
            if n==files:
                r=False
                self.text[counter]=text
            counter+=1    
        if r:
           self.name=self.name+[files]
           self.text=self.text+[text]
    def append(self,files,text):
        r=True
        counter=0
        l=len(self.name)
        for n in self.name:
            if n==files:
                r=False
                self.text[counter]=self.text[counter]+text
            counter+=1    
        if r:
           self.name=self.name+[files]
           self.text=self.text+[text]
    def reads(self,files):
        r=True
        counter=0
        l=len(self.name)
        for n in self.name:
            if n==files:
                r=False
                return self.text[counter]
            counter+=1    
        if r:
             print("error")
             return None
         
s=simu()
s.load("fs.fs")
s.append("file5","xxxx")
s.ls()
print(s.reads("file5"))
s.save("fs.fs")

