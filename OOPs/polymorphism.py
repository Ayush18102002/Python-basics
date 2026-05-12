# polymorphism means many forms and in programming it refers to methods/function/operators 
# with the same name that can be execute on many objets or classes

# function polymrphism

# an example of a python that can be used on different obkect is the ;en() function

# string 
x = "hello world"
print(len(x))

# list 
y = [1,2,3,4,5]
print(len(y))

#tuple
z = (1,2,3,4,5)
print(len(z))

#dictonary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
    }

print(len(thisdict))


# class polymorphism

# it is often used in class methods, where we can multiple classes with the same method name 

# suppose we have three classes : Car, Boat and Plane, and they all have a method called move()

class Car:
    def __init__(self,brand,model):
        self.brand =  brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("Ford","Mustang")
boat1 = Boat("Ibiza","Touring 20")
plane1 = Plane("Boeing","747")

for x in (car1,boat1,plane1):
    x.move()


# inheritance class polmorphism 

# what about clasees with child classes with the same name ? can we use pollymorphism there ?

# yes if we use the above code and make a parent class called Vechicle and make car, boat, plane child
# classes of vechicle the child classes inherits the vechicle methods but can ovverride them

class Vechicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("move")

class car(Vechicle):
    pass

class boat(Vechicle):
    def move(self):
        print("sail")

class plane(Vechicle):
    def move(self):
        print("fly")

car1 = car("Ford","Mustang")
boat1 = boat("Ibiza","Touring 20")  # object creation 
plane1 = plane("Boeing","747")

for x in (car1,boat1,plane1):
    print(x.brand)
    x.move()
    print(x.model)
    

# child class inherits the properties and methods from the parent class
# # in the above you see the car class is empty but dtilss it print brand model,and move through the help of inheritance
## the boat and plane classes also inherits brand , model and move() from Vechicle but they both ovverride the move() method

# because of polymorphism we can execute the same method for all classes



