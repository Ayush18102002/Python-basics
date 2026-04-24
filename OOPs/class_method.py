# class Method
# methods are functions that belong to a class. they define the behaviour of 
# objeccts created from the classs

class Person:
    def __init__(self,name):
        self.name =  name
    
    def greet(self):
        print(f"hello, my name is {self.name}")

p1 = Person("ayush")
p1.greet()  


# methods with parameters
# methods can accept parameters just like regular functions

class Calculator:
    def add(self,a, b):
        return a+b

    def sub(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        return a/b
    
    def mod(self,a,b):
        return a%b
    
calc = Calculator()
print(calc.add(2,3))
print(calc.sub(2,3))
print(calc.mul(2,3))
print(calc.div(2,3))
print(calc.mod(2,3))


# methods accessing properties
# methods can access and modify object properties using self


class Person1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"
    
p1 = Person1("ayush",23)
print(p1.get_info())    


# method modifying properties
# method can modify the properties of an object

class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def cleberate_birthday(self):
        self.age += 1
        print(f"happy birthday! you are now {self.age}")

p2 = Person2("ayush",23)
p2.cleberate_birthday()
p2.cleberate_birthday()
p2.cleberate_birthday()

# the __str__() method
# the __str__() method is a special method that controls what is returned when the object is printed

class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p3 = Person3("ayush",23)
print(p3)  # using str we can control what is returned when the whole object is printed



# Multiple Method
# create multiple methods in a class

class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)
        print(f" Added: {song} ")

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f" Removed: {song}")

    def show_songs(self):
        print(f"PLayalist '{self.name}' ")
        for song in self.songs:
            print(f"- {song}")  

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()
my_playlist.remove_song("Bohemian Rhapsody")
my_playlist.show_songs()


# delete methods
# you can delete methods from a class sing the del keywords

class Person4:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"hello, my name is {self.name}")

p4 = Person4("ayush")
p4.greet()

del Person4.greet
# p4.greet() --- after deleting the methods it gives error object hhas no attribut 'greet'

   