class E:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b!=0:
            return self.a/self.b
        else :
            print("Infinite")
e=E(55,7)
print(e.add())
print(e.sub())
print(e.mul())
print(e.div())
b=E(6,0)
print(b.div())