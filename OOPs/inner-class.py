# python inner classes
# an inner class is a class defined inside another class . the inneer class can access the properties and methods of the outer class
# inner classes are useful for grouping classes that are only used in one place, making your code more organized

class Outer:
    def __init__(self):
        self.name = "Outer Class"
    class Inner:
        def __init__(self):
            self.name = "Inner Class"
        
        def display(self):
            print("This is the inner class")
            
outer = Outer()
print(outer.name)

# Accessing inner class from the outside 
# to access thee inner class , create an object of the outer class and then crate an object of the inner class

# Access the inner class and create an object 

class Outer1:
    def __init__(self):
        self.name = "Outer Class"

    class Inner1:
        def __init__(self):
            self.name = "Inner Class"

        def display(self):
            print("This is the inner class")

outer1 = Outer1()
inner1 = outer1.Inner1()
inner1.display()
print(inner1.name)
print(outer1.name)

# Accessing outer class from inner class
# inner classes in python do not automatically have access to the outer class instance
# if you want the inner class to access the outer class, you need to pass the outer class instance as a parameter

# pass the outer class instance to the inner class

class Outer_instance:
    def __init__(self):
        self.name = "Outer Class"

    class Inner2:
        def __init__(self, outer_instance):
            self.outer = outer_instance
            self.name = "Inner Class"

        def display(self):
            print(f"This is the {self.name}")
            print(f"Accessing: {self.outer.name}")

outer2 = Outer_instance()
inner2 = outer2.Inner2(outer2)
inner2.display()


# accessing outer class from inner class
# inner classes in python do not automatically have access to the outer class instance
# if you want the inner class to access the outer class, you need to pass the outer
# class instance as a parameter

"""
class outer:
    def __init__(self):
        self.name = "emily"
    
    class inner:
        def __init__(self,outer):
            self.outer = outer

        def display(self):
            print(f" outer class name : {self.outer.name}")
    
Outer3 = outer()
inner = outer.inner(outer)
inner.display()


"""

# use an inner class to represent a car's engine

class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.engine = self.engine()

    class Engine:
        def __init__(self):
            self.status = "off"

        def start(self):
            self.status = "Running"
            print("engine Started")

        


