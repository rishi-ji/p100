class Myself:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print('My Name is '+self.name+" My age is "+self.age)
P1=Myself("Rishi",'12')
P1.myfunc()