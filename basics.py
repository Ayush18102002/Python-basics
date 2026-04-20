"""
x=5
y="john"
print(x)
print(y)

#casting 

v = int(5)
z= str(3)
l = float(3)

print(v)
print(z)
print(l)

#type of 
print(type(v))
print(type(z))
print(type(l))


"""
"""
#multi-values or multi variable 
x,y,z = "oranges","bananna","cherry"
print(x)
print(y)
print(z)

#onr value and multi variable 
l=m=p= "strawberry"
print(l)
print(m)
print(p)

#list 
fruits = ["apple","bananan","cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

"""
"""
x ="python is awsome"
print(x)

y = "python"
z = "is"
v = 'awsome'

print(y,z,v)
print(y  + z  +  v )


x  = 5
y = 'john'
print(x+y) # it will give the error because the + operator will not add two different type operatos

#insted of use comma(,) in place of + so it support different data types

print(x,y)

"""

"""
x = "awsome " # global variable 

def myfun():
    print("python is" +  x)

myfun()


x = "awsome "

def myfun():
    x = "fantistcs "
    print("python is" +  x)

myfun()

print("python is " + x)


# we can use global key word to make it global scope 




def myfun():
    global x
    x = "awsome "
    

myfun()
print("python is" +  x)

"""

"""
x = "Hello World" #string 
print(x)
print(type(x))

x = 20 #int 
print(x)
print(type(x))

x = 20.5 #float
print(x)
print(type(x))


x = ['aaple','banana','cherry'] #list
print(x)
print(type(x))

x =("apple","banana","cherry") #tuple
print(x)
print(type(x))

x = range(10) # range
print(x)
print(list(x))
print(tuple(x))
print(type(x))

x ={"name":"ayush", "age":36} #dictionary
print(x)
print(type(x))

x = { 'apple','bananan','cherry'} # sets
print(x)
print(type(x))

x = frozenset({'apple','banana','cheery'}) #frozenset
print(x)
print(type(x))

x = True #boolean
print(x)
print(type(x))

x = b"hello" #bytes
print(x)
print(type(x))

x = bytearray(5) #bytearray
print(x)
print(type(x))

x = memoryview(bytes(5)) #memoryview
print(x)
print(type(x))

x = None
print(x)
print(type(x))

"""


"""
## python numbers 
# int
# floaat
# complex 

x = 1    #int 
y = 2.5  #float
z = 1j   #complex

print(type(x))
print(type(y))
print(type(z))

#integer - whole no., negative , without decimal , unlimeted length
x = 1
y = 1815151654891651654411
z = -2479412167241672

print(type(x))
print(type(y))
print(type(z))

#float -- decimal with positive negative and containing one and more decimal
x = 1.10
y = 1.10
z = -3491.91

print(type(x))
print(type(y))
print(type(z))

#float also contains e,E it indicate the powers of 10
x = 35e3
y = 12E4 
z = -18.8489e410

print(type(x))
print(type(y))
print(type(z))

#comples - it is imiginary no. written as "j"

x = 10j+1
y = 20 + 1j
z = 31j

print(type(x))
print(type(y))
print(type(z))



#type converion

x = 1
y = 20.5
z = 5j+1

#convet from int to float
a = float(x)

#convert float to int
b =  int(y)

#convert int to complex
c = complex(x)

# and you can convert vice versa

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


## random number 
#python does not have randome function ut have a random module that can called and random and it is biult in module

import random

print(random.randrange(1,50))  #diaplay and no. in between the range of 1 to 50


"""

#python string

"""
a = "hello world"
print(a[1])


for x in "bananananan": #it print the character of the sring
    print(x)


print(len(a)) # to find the length of the string 

#check if the certain phrase or character present in the string 
txt = ' the best things in life are free values and you like you get it'
print("free" in txt) # it find the free present in the sentense or not 

# using the if statement 

if "free" in txt:
    print("yes, 'free' is present " )

#check if not
print("expensive" not in txt)

if "expensive" not in txt:
    print("yes, 'expensive' is not present ")

"""

"""
#slicing 

b =  ' hello, worlds '
print(b[2:5]) 
print(b[:5])
print(b[2:])
print(b[-5:-1])

#upper case
print(b.upper())

#lower case
print(b.lower())

# remove white spaces
print(b.strip()) 

#replace the string with other string 
print(b.replace('h','b'))

# split method -- it return the list and the seperated item will we the new element 
print(b.split(","))

"""

"""
##string concatenation
# to cincatenated or combine two string you can use '+' operator

a = 'hello'
b = "wolrld"
c = a + b
print(c)

# for space between the hello and worlds
c = a + "  " + b
print(c)


## format - string 

# string format 

age = 23
# this wiil produce and error 
#txt =  " my name is ayush, I am " + age 
#print(txt)

# because we cannote combine the two differnt data type with using the + operator 
# so for combining we use format() method in string 

txt = f" my name is ayush, I am {age} "
print(txt)

#placeholders and modifiers
#placeholders -- it contain variable, operation, function 
# moifier -- it use to format the value 

# add a placeholder for the price variable 

price = 59
txt = f"the price is {price} dollars"
print(txt)

#place holder with modifier 
#like using 2f so it put the decimal after the 2 digit 
# so use :2f it use with ':' 

txt = f" the price is  {price:2f} dollars"
print(txt)

# we can use math operation inside the placeholder
txt = f" the price is  {20*50} dollars"
print(txt)


## Escape Character
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash '\' followed by the character you want to insert.

txt = " we are so-called\"viking\" from the north "
print(txt)

"""
"""
#String -- method 
a = 'hello words'
txt  = " IM THE BEST you know. "

# capitalize () - canverts the first character to upper case

x = a.capitalize()
print(x)

# casefold() -- convert string into lower case
print(txt.casefold())

#centre - return a centered string
print(a.center(20))

#count() -- returns the no. of times a speified value occurs in a string
print(a.count('h'))

#encoded() -- return an encoded version of the string
print(a.encode())

#endswith() -- return true if the string ends with the specified value
x = txt.endswith(" ")
print(x)
x = txt.endswith("know. ")
print(x)
x = txt.endswith("you know. ",10,25)
print(x)

#expandtabs() -- sets the tab size of the string 
print(txt.expandtabs())

#find() -- searched the string for a specifieed value and returns the position ofwjere it was found
print(txt.find("BEST"))
print(txt.find("best")) #if the find mthod not found the  value in string then it return -1
#print(txt.index("best")) # but in case of indes if it not found then ut makes a exception

# isalnum() -- Returns True if all characters in the string are alphanumeric
print(a.isalnum())

#isalpha() -- Returns True if all characters in the string are in the alphabet
print(a.isalpha())

#isacii() --Returns True if all characters in the string are ascii characters
print(a.isascii())

#isdecimal() -- Returns True if all characters in the string are decimals
print(a.isdecimal())

#isdigits() --	Returns True if all characters in the string are digits
x = "123648411"
print(x.isdigit())

#isidentifier() -- 	Returns True if the string is an identifier
l="MYfold"
k="Demo456"
S="2bringer"
d="my demo"
print(l.isidentifier())
print(k.isidentifier())
print(S.isidentifier())
print(d.isidentifier())

#islower()-- return true if all the character is in lower case
print(a.islower())

#isupper() --- ---------------//-------------------upper case
print(a.isupper())

#isnumeric() -- return true if all the characters in strings is numeric
x = "123648411"
print(a.isnumeric())
print(x.isnumeric())

"""

"""

#bitwise operator
# bitwise AND '&'
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
print(6 & 3)

#bitwise OR '|'
#The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
print(6 | 3)

#bitwise XOR '^'
#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
print(6^3)

#bitwise NOT '~'
# The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
print(~3)

#bitwise left shift ' << '
# The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:
print(3 << 2 )

#bitwise right shift ' >> '
# The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
print(8 >> 2)

"""

"""

##list method
# append() -- Adds an element at the end of the list
# clear() -- Removes all the elements from the list
# copy() -- Returns a copy of the list
# count()--	Returns the number of elements with the specified value
# extend()-- Add the elements of a list (or any iterable), to the end of the current list
# index() -- Returns the index of the first element with the specified value
# insert() -- Adds an element at the specified position
# pop() -- Removes the element at the specified position
# remove()-- Removes the item with the specified value
# reverse()-- Reverses the order of the list
# sort()-- Sorts the list

#List
mylist =  ["apple","banana","cherry"]
print(mylist)

# In the list we can store order item so we tell that list is oredered list
# It can be changeable it means we can add, remove items in a list after it has been created 
#its allow duplicates

#using len() to find length of list 
print(len(mylist))

# cahnge range item

mylist[1] = "oranges"
print(mylist)

#change with a range of itm value
mylist[0:2] = ["kiwi", " watermelon"]
print(mylist)


# add list items

#using apppend() we can add item at end of the list
#using insert() we can add item at any specified index
#using extend() we can append elements from anothher list
#also extend() append tuples , set , dictionaries etc


# we can use insert() it an inserts an item at the specified index 
# also it insert without replacing any item
mylist.insert(2,"mango")
print(mylist)



#append() -- to add an item to the end of the list

mylist.append("chiku")
print(mylist)

#extend() -- to append element from another list to the current list 

tropical = [ "apple", " pineapple", "papaya"]
mylist.extend(tropical)
print(mylist)

thistuple = ("rose","lily")
mylist.extend(thistuple)
print(mylist)



# remove list item

# remove() -- it removes the specified item 
# if the item have multiple duplicate then it remove their first occurence

mylist.remove("mango")
print(mylist)

# pop() - it removes the specified index
# if we not specified the index it default remove the last index 

mylist.pop(4)
print(mylist)

# del() -- it is also remove the specified index
del mylist[1]
print(mylist)

# clear() -- it empty the list
mylist.clear()
print(mylist)


#loop

thislist = ["mango", "bananna", "cherry"]
for x in thislist:
    print(x)


#loop through the index number
 ## use range() or len() function to create a suitable iterable

for i in range(len(thislist)):
    print(thislist[i])


# using while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1


# list comprehension


# looping using list comprehension

# List Comprehension offers the shortest syntax for looping through lists:

# a short hand for loop tht will print all item in a list
 
[print(x) for x in thislist]


# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#conditional based looping

# only accept items that are not apple

newlist = [x for x in fruits if x!= "apple"]
print(newlist)

#with no if statement 

newlist = [x for x in fruits]
print(newlist)


#using range
newlist = [x for x in range(10)]
print(newlist)

#accept only no.
newlist = [x for x in range(10) if x < 5]
print(newlist)

#set the values in the new list to upper case

newlist = [x.upper() for x in fruits]
print(newlist)

# set all values in the new list to  'hello'

newlist = ['hello' for x in fruits]
print(newlist)

#return orange insted of banana

newlist = [x if x!= "banana" else "orrange"  for x in fruits]
print(newlist)

#python -- sort list

thislist2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
numberlist = [1,8,6,4,7,9,15,2,48,9,31,4,61]
thislist.sort()
numberlist.sort()
print(thislist2)
print(numberlist)

# sort descending
# we use reverse = True to sort  decending 
numberlist.sort(reverse=True)
print(numberlist)

# customize srt function
def myfunc(n):
    return abs(n-20)

numberlist.sort(key=myfunc)
print(numberlist)

#reverse order

thislist2.reverse()
print(thislist2)

#copy list

#copy() -- it use to copy the list

list3 = ["apple", "bananan", "cherry"]
mylist = list3.copy()
print(mylist)

# Another way to copy list is use list() 

mylist = list(list3)
print(mylist)

# the slice operator

# you can also make a copy of list by using the ' : ' (slice) operator
mylist = thislist2[:]
print(mylist)


# join list

# there are many way to join or conccatenate two list in python

# + 

list1 = ["a", "b", "c"]
list2 = [1,2,3]

list4 = list1 + list2
print(list4)

# another way to join two list is by appending all the itme from list 2 into list1 one by one

for x in list2:
    list1.append(x)

print(list1)

#extend()

list1.extend(list2)
print(list1)

"""
"""

## pyhton -- Tuples
# tuple item are ordered, unchangeable and allow duplicate
#also tuple can contain different data types

mytuple = ("apple" , " banana", "cherry")
print(len(mytuple))
print(type(mytuple))


# access tuple items 
print(mytuple[1])
print(mytuple[-1])

if "apple" in mytuple:
    print("yes, it is present in the tuple")


# update tuples

#once a tuple is created , you cannot change its value tuple are unchengable or immutable as also is called

# but if you wanted to make some changes so you have to convert the tuple into the list so you can change the tuple

x = ("pineapple", "kiwi", "oranges")
y = list(x)
y[1] = "apple"
print(type(y))
x = tuple(y)

print(x)
print(type(x))
#add item so you have to convert into the list

z = ("pinelapple", "kiwi", "oranges")
l = list(z)

l.append("guava")
print(type(l))
z = tuple(l)
print(z)
print(type(z))


# we can add tuple it is allowed
thistuple = ("apple", "oranges", "cheery")
y = ("oranges",)
thistuple += y
print(thistuple)

# if you wanted to remove so first you convert the yuple into the list
# use  remove() , del () but first convert 

#unpack tuple

# when we create a tuple , normally assign vallue ti it. this is called "packing" a tuple

fruits = ("apple", "banana", "cherry")

#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#using asterisk *

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# add list of value in the "tropic" variable
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#loop tuples

for x in thistuple:
    print(x)


for i in range(len(thistuple)):
    print(thistuple[i])

i=0
while i < len(thistuple):
    print(thistuple[i])
    i = i+1


# join tuple

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# tuple method

# count()--Returns the number of times a specified value occurs in a tuple
# index()--Searches the tuple for a specified value and returns the position of where it was found

"""


"""
## Sets
# sets are used to store multiple items ina single variable
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set items are unchangeable, but you can remove items and add new items.
# do not allow duplicate

#syntax

mysset = {"apple", "banana", "chiku"}
print(mysset)

# the True and 1 is considered the same value 
# same as for False and 0
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

print(len(thisset))
print(type(thisset))

# set constructor
thisset1 = set(("ball", "bat", "stump"))
print(thisset1)


# access items

for x in thisset1:
    print(x)

# check if  " bananan " is present in the set
print("banana" in thisset)

# check if not
print("banana" not in thisset)

# Add items in set

# to add one item to a set use the add() method

thisset.add("oranges")
print(thisset)

# add sets

#To add items from another set into the current set, use the update() method.

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# add any iterable 
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

thisset3 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

mylist.append("oranges")

thisset3.update(mylist)

print(thisset3)


# remove items 
# To remove an item in a set, use the remove(), or the discard() method.


 # Note: If the item to remove does not exist, remove() will raise an error
thisset3.remove("banana")
print(thisset3)

# Note: If the item to remove does not exist, discard() will NOT raise an error.

thisset3.discard("cheery")
print(thisset3)


# sets union 
# The union() and update() methods joins all items from both sets.
# Return a set that contains all items from both sets, duplicates are excluded:
# in union we can join as many set you wants using commas ,
# if duplicates of items presents in more than one sets but in the result it only occurs in one time
# set.union(set1, set2...) -- syntax
# set | set1 | set2 ... -- shorter syntax 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)
print(z)

s = x | y 
print(s)

# intersection() 
# in this method it keeps ONLY the duplicate
# syntax
# set.intersection(set1, set2 ... etc.) 
# set & set1 & set2 ... etc. --- sorter one
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

s = x & y
print(s)

# difference()
# in this method it keeps the ite from the first set that are note in the ohter set(s)
# syntax 
# set.difference(set1, set2 ... etc.)
# set - set1 - set2 .... etc. -- shorter syntax

# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)
print(z)

myset  = x - y
print(myset)

# symmetric_difference()
# it is method keeps all itmems EXPECT the duplicate
# syntax
# set.symmetric_difference(set1)
# set ^ set1 - shorter

z = x.symmetric_difference(y)
print(z)

s = x ^ y
print(s)

# python - frozenset

#v frozenset is an immutable version of a set.

# Like sets, it contains unique, unordered, unchangeable elements.

# Unlike sets, elements cannot be added or removed from a frozenset.

# Use the frozenset() constructor to create a frozenset from any iterable.

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

"""

"""
# python dictonaries
# dictionaries arre used to stored the data values in key:value paires 
# it is a collection which is oredered , changable and do not allow duplicates

thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))


# dist( ) constrictors
# it is possible to use the dict() constructor to make a dictonary

thisdict1 = dict(name = "john", age = 36, country = "norway")
print(thisdict1)


# access dictonary items

x = thisdict1["name"]
print(x)
y= thisdict.get("model")
print(y)


# the keys() method will return a list of all the keys in the dictonary

z = thisdict.keys()
print(z)

# add new items 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys() # before the change

print(x) 

car["color"] = "white"

print(x) # after the changed


# values() method will return a list of all the values in the dictonary
x = thisdict.values()
print(x)

x = car.values()

print(x)

car["year"] = 2020

print(x)

# item()  method will return each itme in a dictonary as tuple in a list

x = thisdict1.items()
print(x)

thisdict1["year"] = 2020

print(x)

# check if key exist or not
if "model" in thisdict:
    print("yes, it is avalibale ")
else:
    print("no, not found")


# change the values
print(thisdict)
x = thisdict["year"] = 2018
print(x)
print(thisdict)


# using update() to change the dict
thisdict.update({"year":2020})
print(thisdict)


# add dictonary items 

#adding an item to the dictonary is done by using a new key index and assign a value to it
print(thisdict)
thisdict["color"] = "red"
print(thisdict)

# ny update you can add new itmes
thisdict.update({"origin":"volkswagen"})
print(thisdict)

# remove items on a list 

# using pop() -- it removes with the specified key name 
thisdict.pop("model")
print(thisdict)

# using popitem() - method to remove the last inserted item
thisdict.popitem()
print(thisdict)

# usng del() - it remove the specified item with key name 
# it cannot delete the dictonary completely
del thisdict["color"]
print(thisdict)


# using clear -- it empty the dict

thisdict.clear()
print(thisdict)

## loops throught dictonaries

# print all the key 
for x in thisdict1:
    print(x)

# print all the values
for x in thisdict1:
    print(thisdict1[x])


# using values() methos to retun values of the dict

for x in thisdict1.values():
    print(x)


# same as for keys()

for x in thisdict1.keys():
    print(x)


# same for the items but we have to take two varibale keys and values

for x,y in thisdict1.items():
    print(x,y)


# copy the dictonaries

# make a copy of the dictonaries with the copy() method

mydict = thisdict1.copy()
print(mydict)

# another way to make a coy is to use the built- in function dict()

mydict1 = dict(thisdict)
print(mydict1)


# nestead dictonaries

#A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])


# loop through nestead dictonaries

# you can loop through a dictonaries by using the items() metod like this

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print( y + ":", obj[y])

"""

"""

# python match 


#Instead of writing many if..else statements, you can use the match statement.

#The match statement selects one of many code blocks to be executed. 

#match expression:
#  case x:
#    code block
#  case y:
#    code block
#  case z:
#    code block


day = 4
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")  
    case _:
        print(" default case ")


# while loops

#With the while loop we can execute a set of statements as long as a condition is true.
n = 0
i = 10
while n < i:
    
    n += 1
    if( n== 7):
        continue #With the continue statement we can stop the current iteration, and continue with the next:

    print(n)

    if( n == 9):
        break  # With the break statement we can stop the loop even if the while condition is true:
    



"""

"""
# python function

def my_func():
    print(" hello from the function")

my_func()

# argument in function

def my_Func( fname ):
    print(fname + " hello from the function")

my_Func(" from my side to all ")


# using *args to accept any number of argument 

def my_function(*kids):
    print("type :  " , type(kids))
    print(" the yougest child are : ", kids[0])
    print(" the yougest child are : ", kids[1])
    print(" the yougest child are : ", kids[2])


my_function(" tobais ", "lupin", " maxie")

# using *args with regular arguments
# you can combine rqgular paramenters with *args
#regular parameters must come before *args

def my_function1(greeting, *names):
  for name in names:
    print(greeting, name)

my_function1("Hello", "Emil", "Tobias", "Linus")



# finding the maximunm value

def my_max(*numbers):
   if len(numbers) == 0:
      return None

   max_num = numbers[0]
   for num in numbers:
      if num > max_num:
         max_num = num
   return max_num

print(my_max(3, 7, 2, 9, 1))


#Arbitrary Keyword Arguments - **kwargs
#If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name


def my_finction2(**kid):
   print(" his lst name is : " + kid["lname"])

my_finction2(fname = " ayush", lname = "kumar")


#The **kwargs parameter allows a function to accept any number of keyword arguments.
#isdide the function , kwargs becomes a dictonary cantaiing all the keywords arguments

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


# combining both *args and **kwargs

def my_function2(title , *args, **kwargs):
   print("Title : ", title)
   print("positional argument : " , args)
   print("keyword arguments : ", kwargs)

my_function2("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#unpacking  list with *
# If you have values stored in a list, you can use * to unpack them into individual arguments:

def my_function3(a,b,c):
   return a+b+c

numbers = [1,2,3]
result = my_function3(*numbers) #same as : my_function(1,2,3)
print(result)

#Unpacking dictonaries with **
#If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

def my_function4(fname, lname):
   print("hello : " ,fname, lname )

person = {"fname": "emily", "lname":"refsnes"}
my_function4(**person) # same as : my_function4(fname="emily",lname="refsnes")


# python decorators
# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.


##Define the decorator first, then apply it with @decorator_name above the function.

def changecase(func):
   def myinner():
      return func().upper()
   return myinner

@changecase
def myfunction():
   return " hello india "

@changecase
def otherfunction():
   return " you can call multiple decorater function"


print(myfunction())
print(otherfunction())


# arguments in the decorator function

# Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:

def changecase(func):
   def myinner(x):
      return func(x).upper()
   return myinner
      
@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))


##Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

# decorator with arguments
# Decorators can accept their own arguments by adding another wrapper level.
# A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

# multiple decorator 

# You can use multiple decorators on one function.
# This is done by placing the decorator calls on top of each other.
# Decorators are called in the reverse order, starting with the one closest to the function.

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

## Preserving Function Metadata

# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

# Normally, a function's name can be returned with the __name__ attribute:

def myfunction():
   return " have a good and beautiful day !!!!"

print(myfunction.__name__)

# But, when a function is decorated, the metadata of the original function is lost.

#  Try returning the name from a decorated function and you will not get the same result:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# to fix this , pyhton has a built in function called functools.wraps that cab be used to preserve the original function
# name and docstring

# Import functools.wraps to preserve the original function name and docstring.

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# python lambda

# lambda functions is a small anonymous function
# a lambda function can take any no. of arguments, but can only have one expression
# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

# it can take any no. of arguments

y =  lambda a, b : a*b
print(y(5,6))


z = lambda a, b, c : a + b + c
print(z(5, 6, 2))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
   return lambda a : a*n

mydoubler = myfunc(2)
print(mydoubler(11))

# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# using map()  function applies a function to every item in an iterable

numbers = [1,2,3,4,5,6]
doubled = list(map(lambda x : x*2, numbers))
print(doubled)

# The filter() function creates a list of items for which a function returns True:

numbers = [1,2,3,4,5,6,7,8,9]
odd_numbers = list(filter(lambda x : x % 2 != 0 , numbers))
print(odd_numbers)

# The sorted() function can use a lambda as a key for custom sorting:

students = [("emily",25),("tobais",23),("linus",28)]
sorted_students = sorted(students, key = lambda x : x[1])
print(sorted_students)

words = ["apple","pie","banana","cherry"]
sorted_words = sorted(words, key= lambda x : len(x))
print(sorted_words)


# recursion 

def countdown(n):
   if n <= 0:
      print("done")
   else:
      countdown(n-1)
      print(n)

countdown(6)


# factorial 


def facctorial(n):
   #base case
   if n==0 or n==1:
      return 1
   #recursive call
   else:
      return n * facctorial(n-1)

print(facctorial(6))


# fibbonacci sequence

def fibonacci(n):
   #base case
   if n<=1:
      return n
   else:
      return fibonacci(n-1)+fibonacci(n-2)
   
print(fibonacci(6))

# calculate the sum of all elemets in a list

def sum_list(n):
   if len(n)==0:
      return 0
   else:
      return n[0] + sum_list(n[1:])
   
my_list = [1,2,3,4,5,6]
print(sum_list(my_list))

#find the maximum value in a list

def fin_max(n):
   if len(n)==1:
      return n[0]
   else:
      max_of_rest = fin_max(n[1:])
      return n[0] if n[0] > max_of_rest else max_of_rest
   
my_list = [3, 7, 2, 9, 1]
print(fin_max(my_list))


# recursive depth limit 

# Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.

import sys
print(sys.getrecursionlimit())

# we can change the depth limit but we need to carefully beause it cuse the crash

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

# generattors

#Generators are functions that can pause and resume their execution.
# When a generator function is called, it returns a generator object, which is an iterator.
# The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generato

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

# Generators allow you to iterate over data without storing the entire dataset in memory.
# Instead of using return, generators use the yield keyword.

# generator yield numbes

def count_up_yo(n):
   count = 1
   while count <=n:
      yield count
      count+=1

for num in count_up_yo(5):
   print(num)

# Unlike return, which terminates the function, yield pauses it and can be called multiple times.


# generator saves memory

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

#You can manually iterate through a generator using the next() function

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  # This will raise StopIteration

# When there are no more values to yield, the generator raises a StopIteration exception:

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))


# sum with generator
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)

# Generators can be used to create the Fibonacci sequence.

# It can continue generating values indefinitely, without running out of memory:


def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))


# generators methods

# send method

# The send() method allows you to send a value to the generator:

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")

# close() methods

# it can stops the gererators

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

"""
"""

# python range

# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
# This set of numbers has its own data type called range.

# syntax --  range(start, stop, step)


# we call the range with one argument then it is call as the stop value
# and the  default value wiil be 0 in case we not specified

x = range(10)
print(x)
print(list(x))


# and with two arguments it shown as one is start and other one is stop

x = range(3,10)
print(x)
print(list(x))

# the range function is called with three arguments, the third argument represents the step value.

# The step value means the difference between each number in the sequence. It is optional, and if not provided, it defaults to 1.

# range(3, 10, 2) returns a sequence of each number from 3 to 9, with a step of 2:

x = range(3, 10, 2)
print(x)
print(list(x))


# we can use range on for so we can iterate ove over the list

# Slicing Ranges
# Like other sequences, ranges can be sliced to extract a subsequence.

r = range(10)
print(r[2])
print(r[2:])
print(r[:6])

# Membership Testing
# Ranges support membership testing with the in operator.

r = range(0, 10, 2)
print(6 in r) # true
print(7 in r) # false

# anges support the len() function to get the number of elements in the range.

r = range(0, 10, 2)
print(len(r))



# python array 

# Python does not have built-in support for Arrays, but Python Lists can be used instead.

# array methods  -- append(), clear(), Copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()

"""
"""
# pyhton iterator

## so iterator is an object that countain a countable no. of values
# in pyhton the iterator contain two  methods  __iter__() and __next__().


# Iterator vs Iterable

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple","banana","cheery")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# using for loop
for x in mytuple:
    print(x)


# Create an Iterator

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a+=1
        return x
    
    
myclass = MyNumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration  # it use to stop the iterator because if we not do then will go forever

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

"""
"""
# python module 
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# create module 
# first we Save this code in a file named mymodule.py

## use this through importing the file into current file

import mymodule

mymodule.greeting("jonathan")

# When using a function from a module, use the syntax: module_name.function_name.

# variables in module
# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):



a = mymodule.person1["age"]
print(a)


# naming a module
# You can name the module file whatever you like, but it must have the file extension .py

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

a = mx.person1['age']
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.

# import ans use platform moduels

import platform

x = platform.system()
print(x)

# Using the dir() Function

#There is a built-in function to list all the function names (or variable names) in a module. The dir() function:

x = dir(platform)
print(x)

# The dir() function can be used on all modules, also the ones you create yourself.


# Import From Module
# You can choose to import only parts from a module, by using the from keyword.

from mymodule import person1

print(person1['age'])

"""
"""
# python date and time


# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime
x = datetime.datetime.now() # use now to display the current time
print(x)

print(x.year) # return the year
print(x.strftime("%A")) # return the weekday name


# creating date object

x = datetime.datetime(2020,5,18)
print(x)


# strftime() method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

x = datetime.datetime(2020,6,1)
print(x.strftime("%B"))

"""
"""
# python maths

# python has a built-in maths function , including an extensive math module , that allows you to perform mathematical tasks on numbers

import math
x = min(5,13,12)
y = max(21,100,87)
print(x)
print(y)

"""
"""
# python json

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.

import json
# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse 
y= json.loads(x)

# the result is a pyhton dictionary 

print(y["age"])


# convert python to json 

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# converts into json

y = json.dumps(x)

# the result is a json string 

print(y)

# so we can convert the python object of following type into json string
# dict, list, tuple, string, int, float, True, False, None

# Convert Python objects into JSON strings, and print the values:

print(json.dumps({"name":"john","age":13}))
print(json.dumps(["apple","banananas"]))
print(json.dumps(("apple","bananan")))
print(json.dumps("helllo"))
print(json.dumps(62))
print(json.dumps(32.65))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# pyhton -- jason
# dict -- Object
# list -- Array
# tuple -- Array
# str -- String
# int -- Number
# float -- Number
# true --  true
# False -- false
# None -- null


# Convert a Python object containing all the legal data types:

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# format the result

# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

# The json.dumps() method has parameters to make it easier to read the result:
# Use the indent parameter to define the numbers of indents:

y= json.dumps(x,indent=4)
print(y)

# You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

# Use the separators parameter to change the default separator:

y= json.dumps(x, indent= 4, separators=(".","="))
print(y)


# order the result

#  The json.dumps() method has parameters to order the keys in the result:

# use the sort_key parameters to specify if the result should be sorted or not

y = json.dumps(x, indent=4, sort_keys = True)
print(y)

"""
"""
# python RegEx

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# regex module 
# pyhton has a built in package called re , which can be used to work with regular expression

# import the  " re " module

import re

txt = "the sun is burining like a dead start"
x = re.search("sun",txt)
if x :
    print(" yes it is present ")
else:
    print("oops not getting in")

# regex function
# findall() -- return the list containing all matches
# search() -- return a match object if there is a match anywhere in the string4
# split() -- return a list where the string has been split at each match
# sub() -- replaces one or many matches with a string


# Print a list of all matches:

x = re.findall("i",txt)
print(x)

# the list contains the matches in the order they found 
# if no matches are found , an empty list is returned

x = re.findall("portugal",txt)
print(x)

# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:

x = re.search("\s",txt)
print(" the first white-space character is located in position:",x.start())

# If no matches are found, the value None is returned:

# The split() function returns a list where the string has been split at each match:

x = re.split("\s", txt)
print(x)

# x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

# The sub() function replaces the matches with the text of your choice:

x = re.sub("\s", "9", txt)
print(x)

# You can control the number of replacements by specifying the count parameter:
x = re.sub("\s", "9", txt, 2)
print(x)

# A Match Object is an object containing information about the search and the result.

# Note: If there is no match, the value None will be returned, instead of the Match Object.

x = re.search("ar", txt)
print(x) #this will print an object

# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+", txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())

"""

"""
# PIP
# it is a package manager for python packages or modules if you like
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

"""
"""
# python try except 

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# exception handling 

try:
    print(x)
except NameError:
    print(" variable x is not defined")
except:
    print(" an exception occured")



# you can use the else keyword to define a block of code to be excuted if no error were raised
try:
    print("hello")
except:
    print("something went wrong")
else:
    print(" nothing went wrong")

# finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")

try:
    f  = open("demofile.txt")
    try:
        f.write("lorum ispum")
    except:
        print("something went wrong when writing to the file ")
    finally:
        f.close()
except:
    print("something went wrong when opening the file")


# raise an exception

# as a python developer you can choose to throw an exception if conditon if a condition occurs
# to throw (or raise) an exception, use the raise keywords

x = -1

if x < 0:
  raise Exception("sorry , no number below zero")


# the raise keword is used to raise an exception
# you can define what kind of error to raise and the text to print to the user.

# example supoose -- raise a typeerror if x is not an integer 

x = " hello"

if not type(x) is int:
    raise TypeError(" only integers are allowed")

"""

"""
# python string formatting
# F-string 
# it is allow you to format selected parts of a string 
# to specify a string as an f-string simple put an f in front of the string literal

txt = f"the price is 49 dollars"
print(txt)

# Placeholders and Modifiers 

# to format vallues in a f string add placeholders {}, a place holders can contains variables,
# operation , function and modifiers to format the values

price = 59
txt = f"the price is {price} dollars"
print(txt)

txt = f"the price is {price:.2f} dollars"
print(txt)


txt = f"the price is {20*40} dollars"
print(txt)

price2 = 59
tax = 0.25
txt = f"the price is {price2 +(price2*tax)} dollars"
print(txt)


# we can perform if else inside the formater and inside the place holder 

price3 = 49
txt = f"it is very { 'Expensive' if price3>50 else 'Cheap'}"
print(txt)

fruit = "apples"
txt = f" I love {fruit.upper()} "
print(txt)

# The function does not have to be a built-in Python method, you can create your own functions and use them:

def myconverter(x):
    return x * 0.3045

txt = f"The plane is lying at a {myconverter(-3000)} meter depth "
print(txt)

price4 = 590000
txt = f"The price is {price4:,} dollars"
print(txt)

# add a plceholder where you want to display the price

price5 = 49
txt = " the price is {} dollars"
print(txt.format(price5))

# you can add parameters inside the curly bracktes to specify how to convert the value

# format the price to be displayed as a number with two decimals

txt = " the price is {:.2f} dollars"
print(txt.format(price5))


# multiple values 
# if you want to use more value, just add more values to format() method
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(price, itemno, price))

# index number
# you can use index number(a number inside the curly bracket {0}) to be sure the values are placed in the correct placeholders

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(price, itemno, price))

# if you want to refer to the same value more then once, use the index no.

age = 36
name = " john"
txt = " His name is{1}. {1} is {0} year old "
print(txt.format(age,name))

# we can use the name index but we have to assign the value with them 

myorder = " i have a {carname}, it is a {model}"
print(myorder.format(carname = "ford", model="Mustang"))

"""
"""

#python None
# it is a special constant in python that represent the absence of  value
# its data type is NOneType and Node is the only instance of a NoneType object

# none value indicate " no value" or " not set"

# assign and display a None value

x = None
print(x)
print(type(x))


# comparing to None
# to compare a value to None, use the identity operator is or is not

result  = None
if result is None:
    print("no result yet")
else:
    print("result is ready")

# is not case

result  = None
if result is not None:
    print("no result yet")
else:
    print("result is ready")


# none evaluates to false in the boolean context

print(bool(None))

# function returning None

# function without and return or do not return any value is return None by defalut

def myfunc():
    x =5

x = myfunc()
print(x)

"""
"""

# user input

print(" enter your name ")
name = input()
print(f" hello {name}")

# Note = pyhton stops execution when it comes to input() function and continues when the user has given some inout
x = input(" enter  the name brother ")
print(f" the name is {x} llalalallalalalallaal")

# inpur on the no.
import math
x = input("enter the number: ")

# find the square root of the no.
y = math.sqrt(float(x))

print(f" the square root of {x} is {y}")

# validate the input-- we can use this to check whether the given input data typw is write or not or it may be different if it is the code will reject it 

y = True
while y == True:
    x = input("Enter a number: ")
    try:
        x = float(x);
        y = False
    except:
        print(" wrong input, please try again.")

print(" thank you!")

"""
"""

# set Isdisjoint -- it return true and false if no common element found

set1 = {1,2,3}
set2 = {4,5,6}
set3 = {set1.isdisjoint(set2)}
print(set3) # no common elemnt found so it is true

set4 ={1,2,3}
set5 ={3,4,5}
set6 = {set4.isdisjoint(set5)}
print(set6) # found common elemt it is false 

"""