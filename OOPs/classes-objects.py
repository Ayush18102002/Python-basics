# pythons is a oops
# almost everything in python is an aboject, with its properties and methods
# A class is like an object constructor, or a " blueprint" for creating objects

# to create a class , use the keyword class

class MyClass:
    x = 5

# now create an object 

p1 = MyClass()
print(p1.x)

# you can delete objects by using the 'del' keyword

del p1

# Multiple Objects
# you can create multiple objects from the same class

# create three objects from the MyClass class

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x)
print(p3.x)

# Each object is independent and has its own copy of the class properties

# the pass statement 
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the
# pass statement to avoid getting an error

class Person:
    pass

#__init__() method

# All classes have a function called __init__(), which is always executed when the class is being initiated.
# It is used to assign values to object properties or to perform operation that are necessary when the object us being created 

# use case for __init__()

# create a class named person , use the __init__() method to assign values for names and age 

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age


p1 = Person("ayush", 23)
print(p1.name)
print(p1.age)


p2 = Person("me",23)
print(p2.name)
print(p2.age)

# so the __init__() method is called automatically every time the calss is being used to create new object
# without this method we need to set properties manually for each object

# suppose to create a class without __init__()

class Person:
    pass


p3 = Person()
p3.name = " ayush"
p3.age = 23

print(p3.name)
print(p3.age)

# using __init__() makes it easier to create objects with initial values.

class Person1:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

p4 = Person1("ayush",24)
print(p4.name)
print(p4.age)

# we can also set default values in __init__() methods

class Person2:
    def __init__(self, name, age = 25):
        self.name = name
        self.age = age


p5 = Person2("ayush")
p6 = Person2("tobais",26)


print(p5.name,p5.age)
print(p6.name,p6.age)

# if we do not mention the age value so it takes the default one and if we assign then it overwrites the cureent with default

# multiple parameters 

# the __init__() methods can have as many parameters as you need

# suppose a person class with multiple parameters

class Person3:
    def __init__(self, fname, lname, age, country, city, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.country = country
        self.city = city
        self.gender = gender

p7 = Person3("ayush","kumar",23,"india","raipur","male")
print(p7.fname,p7.lname,p7.age,p7.country,p7.city,p7.gender )

class Person4:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"hello, my name is {self.name} and i am {self.age} ")


p8 = Person4("ayush",23)
p8.greet()


