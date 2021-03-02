
# Example of inheritance

class  Father:

    def __init__(self,eyes):
        self.eyes = eyes


    def Greet(self):
        print("Hello i'm your father")

class Child(Father):
    def __init__(self):
        super().__init__("Green")




child = Child()
child.Greet()
print(child.eyes)






