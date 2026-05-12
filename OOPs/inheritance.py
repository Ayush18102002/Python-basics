# pyhton inheritance

# inheritance allows us to define a class that inheritance all the methods
# and properties from another class 

# parent class is the  class being inherited from , also called base class

# child class is the class that inherits from another class , also called derived class

# create a parent class

# any class can be a parent class, so the syntax is the same as creating any other class


# create a class named Person with firstname and lastname properties and a printname methods

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname 

    def printname(self):
        print(self.firstname,self.lastname)

x = Person("ayush","kumar")
x.printname()

# create a child class
# to create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class


# create a class named student which will inherits the properties and method from the Person class

class student(Person): # use inheritance to borrow the pearameter and methods from the parents
    pass

x = student("ayush", "kumar")
x.printname()

# use the pass kaywords when you do not want to add any ohter properties or methods to the class

# now the student class has the same properties and methods as the person class

# use the Student class to create an object, and then execute the printname methods

x = student("mike","olsen")
x.printname()

# add the __init__() function

# we wanted to add the __init__() function to the child class(instead of the pass keywords)

# the __init__() function is called automatically every time the class is being used to create  a new object

class student(Person):
    def __init__(self,fname,lname):
        # add properties etc.

# when you add the  __init__() function, the child class will no longer inherit the pernts __init__() function

# the child __init__() function, the child class will no longer inherits the parent __init__() function

# the child __init__() function overrides the inheritance of the parents __init__() function

# to keep the inheritance of the parents __init__() function add a call to the parents __init__() function


        Person.__init__(self,fname,lname)

x = student("ayush","kumar")
x.printname()

# WE HAVE SUCESSFULLY ADDED THE __init__() function and kept the inheritance of the 
# parent class and we are ready to add functionality in the __init__() function

# use the super() function

# pyhton also has a super() function that will make the child inherits all the methods and properties from its parents


class student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

x = student("ayush","kumar",2025)
print(x.graduationyear) 


# add methods

# add a method called welcome to the student class

class student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print(f"welcome {self.firstname} {self.lastname} to the class of  {self.graduationyear}")


x = student("ayush","kumar",2025)
x.welcome()

