class point:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def make(self):
        if(self.a >0 and self.b>0):
            return "this is 1st"
        elif (self.a<0 and self.b>0):
            return "this is 2nd"
        elif (self.a<0 and self.b<0):
            return "this is 3rd"
        else:
            return"this is 4rd"
            print("its in else loop")
p=point(-1,-2)
print(p.make())
