
# 1 ---> ans - car_2
# 2 ---> ans - float
# 3 ---> ans - tuple
# 4 ---> ans - 2
# 5 ---> ans - list,tuple,set
# 6 ---> ans - is
# 7 ---> ans - 2
# 8 ---> ans - set
# 9 ---> ans - key-value
# 10 ---> ans - list,
# 11 ---> ans - aaa
# 12 ---> ans - ^
# 13 ---> ans - 1
# 14 ---> ans - {}
# 15 ---> ans - string,list,tuple

# ---- section B --------
# ans1
# varible is used to assign or store the value
# 3 rule --
# we cannot use special characters to name the variable 
# we cannot use space in naming the variable
# and number not use in front of naming variable

# ans 2
# list is used to store multiple data in orderd manner
# it is mutable
# it represent os []


# ans 3
# list --
# it is mutable ,orderd, indexed
# it allows duplicate 
# it represent using []
# we can perform slicing 
# we can add and remove the item from the list 

thislist = [1,2,3,4,5,6]
print(thislist)
print(thislist[:])
print(thislist[0])
thislist2 = [9,8,7,5]
thislist.extend(thislist2)
print(thislist)



# tuple---
# it is immutable , orderd , indexed
# it also allows duplicate
# it represent as ()
# we can perform slicing 
# we cannot ass or remove item from the tuple but we can convert tuple into the list so we can perform add and remove


# ans 4

# dictionary is represent as {key: value}
# keys is immutable but values will be mutable 

# example

dict1 = {
    "name":"ayush",
    "age":23,
    "country":"india"
    }

print(dict1)
# print name
print(dict1["name"])

# print keys 
print(dict1.keys())

# print values
print(dict1.values())

# print itmes
print(dict1.items())

# add item 

dict1["city"] = "raipur"
print(dict1)

# remove item 
dict1.pop("age")
print(dict1)


# assign different values 
dict1["name"] = "shobhit"
print(dict1)

# nested dict

parent = {
    "child1":{
        "name":"harry potter ",
        "age":23
    },
    "child2":{
        "name":"ron weasely",
        "age ":23
    },
    "child":{
        "name":"harmonie",
        "age ":20
    }

}

print(parent)
print(parent["child1"]["name"])






# ans 5
# set is used to store multiple data 
# it is unorederd , unchangable, unindexed
# it is immutable but we can perform add and remove operation on sets
# it is represent as {}
# sets included sets operation like union , intersection
# the opposite of sets is frozen set it is also immutable but in frozenn set we cannot add ore remove item 

# ans 6

# AND -- if both values is true then only it execute 

x = True
y = True
print(x and y)

# OR | -- if one value is true then it exeute 

x = True
y = False
print(x | y)

# not ! -- it is compliment of true and false 

x = True
print(not x)



### --------------- section C ----------------###

# ans 1 -- 25

# ans 2 -- [1,2,3,4]

# ans 3 -- [2]

# ans 4 -- {1,2,3}

# ans 5 -- 10

# ans 6 -- [1,2,3,1,2,3]

# ans 7 -- HiPython

# ans 8 -- True

# ans 9 -- True

# ans 10 -- True


### ---- section D ----- ###

# ans 1
x = 50
y = 100

print(x+y) # addition
print(x-y) # substraction
print(x*y) # multiplication
print(x/y) # division
print(x%y) # modulus


# ans2

list1 = [1,2,3,4,6,7,8,9]
print(list1)

# add element 

list2 = [10,11,12]
#list1.append(list2)
print(list1)

list1.extend(list2)
print(list1)

# remove list

list1.pop()
print(list1)

list1.remove(2)
print(list1)

## sort element

list3 = [4,3,9,9,7,15,3,7]
list3.sort()
print(list3)


list3.reverse()
print(list3)


# ans 3 
tuple1 = (1,5,6,7,9,1,6)
print(tuple1[1])
print(tuple1[-1])


# ans 4

list1 = [1,2,3,4]
list2 = [3,4,5,6]

set1 = set(list1)
set2 = set(list2)

# union

set3 = set1. union(set2)
print(set3)

# intersection

set4 = set1.intersection(set2)
print(set4) 


# ans 5 

dict1 = {
    "name":"ayush",
    "age":23,
    "country":"india"
    }


# update value

dict1["age"] = 24
print(dict1)

dict1.update({"name":"max"})
print(dict1)
