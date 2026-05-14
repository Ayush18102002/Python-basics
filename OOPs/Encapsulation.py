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

class student:
    def __init__(self,name):
        self.name = name
        self.__grade = 0

    def set_grade(self,grade):
        if 0<= grade <= 100:
            self.__grade = grade
        else:
            print(" Grade must be between 0 and 100")
    
    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "passed"
        else:
            return "Failed"
        
Student = student("Alice")
Student.set_grade(85)
print(Student.name)
print(Student.get_grade())
print(Student.get_status())

# Protected Propperties

# python also has a convention for protected properties using a single underscore _ prefix

class Person4:
    def __init__(self, name, age):
        self.name = name
        self._age = age # Protected Property

p5 = Person4("Eve", 28) 
print(p5.name)
print(p5._age) # can access, but shouldn't be accessed from outside the class as it is a convention to indicate that it is protected and should not be accessed directly.


# private methods
# you can also make methods private by using a double underscore __ prefix

class Calculator:
    def __init__(self):
        self.result = 0
    
    def __validate(self,num):
        if not isinstance(num, (int, float)):
            return False
        return True
    
    def add(self,num): 
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid input, please enter a number")
        

calc = Calculator()
calc.add(10)
print(calc.result)
calc.add("abc") # this will cause an error because "abc" is not a number and the __validate method will return False, preventing the addition from happening.


# just like private properties, private methods cannot be accessed directly from outside the class, but you can provide public methods to access or call them if needed. This is often done to keep the internal workings of your class hidden while still allowing users to interact with it in a controlled way.

# name mangling
# name mangling is how pyhton implments private properties and methods'
# when you use double underscores __. python automatically renames it internally by adding _ClassName in front

# for example , __age becomes _Person__age internally, this is done to prevent accidental access to private properties and methods from outside the class.

class Person5:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private Property

p6 = Person5("Frank", 35)
print(p6.name)
print(p6._Person5__age) # Accessing private property using name mangling
# print(p6.__age) # this will cause an error because __age is private and cannot be accessed directly from outside the class, even though it can be accessed using name mangling.

# While you can access private properties using the mangled name, it's not recommended. It defeats the purpose of encapsulation. Private properties are meant to be hidden and protected, and accessing them directly from outside the class can lead to
# unintended consequences and can make your code more difficult to maintain. It's best to use public methods (getters and setters) to access and modify private properties, as this allows you to control how the data is accessed and modified while still keeping it protected.