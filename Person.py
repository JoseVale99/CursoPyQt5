class Person:
    # Constructor

    def __init__(self,eyes,hair,gender):
        self.eyes = eyes
        self.hair = hair
        self.gender = gender

    def __str__(self):
        return "This is an object of type person"


person1 = Person("Green","Brown","Male")
print(person1.hair)



