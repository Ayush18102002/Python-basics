# class properties 
# properties are variables that belonds to a class. They store data for each object
# created from the class



class Person: # class creation
    def __init__(self, name, age):   # class properties 
        self.name = name
        self.age = age  

p1= Person("emily", 26)  # object creation
print(p1.name,p1.age)



# access properties 
# we can access object properties using Dot notation '.'

class Car:
    def __inti__(self, Brand, model):
        self.Brand = Brand
        self.model = model

Car1 = Car("Toyota", "Camry")
print(Car1.Brand)
print(Car1.model)




