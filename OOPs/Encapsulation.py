# encapsulation is about protecting data inside a class
# it means keeping data(properties) and methods together in a class ,while controlling how 
# the data can be accessed from outside the class

# this prevents accidental changes to your data and hides the internal details of how your class works.

# Private Properties 

# in python you can make properties private by using a double underscore __ prefix

# class a private class property named __age

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # Private Property
    
p1 = Person("Alice", 30)
print(p1.name)
# print(p1.__age) # this will cause an error because __age is private and cannot be accessed from outside the class   

# Private Properties cannot be accessed directly from outside the class, but you can provide public methods to access or modify them if needed. This is often done using getter and setter methods.

# use a getter method to access a private property

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
p2 = Person1("Bob", 25) 
print(p2.name)
print(p2.get_age())

# use a setter method to modify a private property

# the setter method allows you to control how the private property is modified, you can add validation or other logic if needed 

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0: # simple validation to ensure age is positive
            self.__age = age
        else:
            print("Age must be positive")   

p3 = Person2("Charlie", 40)
print(p3.name)
print(p3.get_age())
p3.set_age(35)
print(p3.get_age()) 

# set private property value
# to modify a private property, you can create a setter method
# the setter method can also validate the value before setting it

# use a setter method to change a private property

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

p4 = Person3("David", 50)
print(p4.name)
print(p4.get_age())
p4.set_age(45)
print(p4.get_age())

# why use encapsulation

# Encapsulation helps to protect the internal state of an object and prevents unauthorized access or modification of its properties. 
# It allows you to control how the data is accessed and modified, which can help to maintain 
# the integrity of your objects and prevent bugs or unintended consequences.  

# its provide several other benifits such as :
# 1. Data Hiding: Encapsulation allows you to hide the internal details of how your class works, which can make it easier to use and understand.
# 2. Modularity: Encapsulation allows you to break your code into smaller, more manageable pieces, which can make it easier to maintain and update your code over time.
# 3. Reusability: Encapsulation allows you to create reusable code that can be used in different parts of your program without having to worry about how it works internally.       

