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
    def __init__(self, Brand, model):
        self.Brand = Brand
        self.model = model

car1 = Car("Toyota", "Camry")

print(car1.Brand)
print(car1.model)


# we can modified properties on objects through assiging the new values

car1.Brand = 'volswegan'
print(car1.Brand)

# we can delete the properties using del keywords

del car1.model
# print(car1.model) it delete the model form the class


# class properties vs object properties

# propeties defined inside __init__() belong to each object(instance properties)
# properties defined outside methods belong to the class itself(class properties) and are shared by all objects

class Person:
    species = "human" # class properties

    def __init__(self,name):
        self.name = name # instance property
        
p1 = Person("ayush")
p2 = Person("tobais")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# modifying class properties
# when you modify a class property, it affects all objects

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)

#add new properties
# you can add new properties to exisiting objects

class Person2:
    def __init__(self, name):
        self.name = name    
p4= Person2("tobais")

p1.age = 25
p1.city = "raipur"
print(p1.name)
print(p1.age)
print(p1.city)