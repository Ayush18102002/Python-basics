# python self parameter is a refrence to the current instance of the class
# it is used to access properties and methods that belong to the class

class Person:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello my name is {self.name} and my age is {self.age}")

p1 = Person("ayush",20)
p1.greet()

# self parameter must be the first parameter of any method in the class

# why use self ?
# without self , python would not know which object's poperties you want to access

class Person1:
    def __init__(self,name):
        self.name = name

    def PrintName(self):
        print(self.name)

p2 = Person1("maxxxu")
p3 = Person1("jojo")
p2.PrintName()
p3.PrintName()


# note -- it does not have to be named self you can call it wahtever you like 
# but it has to be the first parameter of any method in the class

# use the words myobject and abc instead of self:




