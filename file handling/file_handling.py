# it is a importat part of any web application
# python has several functions for creating, reading , updating, and deleting files

# the main function is open() it takes two parameters filename and mode.

# four different modes are available for opening a file
# "r" - read mode which is used when the file is only being read
# "w" - write mode which is used to edit and write on the file
# "a" - append mode which is used to add new data to the end of the file; that is new information is automatically amended to the end
# "r+" - read and write mode which is used to handle both actions when working with a file
# "x" - create mode which is used to create a new file
# "t" - text mode which is used to handle files in text format
# "b" - binary mode which is used to handle non-text files (like images or executable files)

# f = open("demofile.txt")


f= open("demofile.txt", "rt")

# because r for read and t for text are the default value
# and make sure the file exists or else you will get an error

print(f.read())

# we can put the different file location in the open() function

# use the with statement 
# you can also use the with statement when opening a file

with open("demofile.txt", "r") as f:
    print(f.read())

# in the wth statement you do not have to worry abput closing your files , the with statement take care of that


# close file

g = open("demofile.txt")
print(g.readline()) # it read only the first line of the file
g.close()

# read only parts of the file

# by default the read() method return whole text , but you can also specify how many characters you wants to return 

with open("demofile.txt", "r") as s:
    print(s.read(5)) # it will return the first 5 characters of the file    


g = open("demofile.txt")
print(g.readline()) # it read only the first line of the file
print(g.readline()) # by calling the readline two times it print first two line from the files


# by looping through the lines oof the file , you can read the whole file, line by line

with open("demofile.txt") as f:
    for x in f:
        print(x) # it will print the whole file line by line




# write to an existing file
# to write a existing file you have to write a parameter to the open() function

# "a" - append mode which is used to add new data to the end of the file
# "w" - write mode which is used to edit and write on the file


# open the file "demofile.txt" and append content to the file

with open("demofile.txt", "a") as f:
    f.write("now the file has more content")


# open and red the file after appending 

with open("demofile.txt", "r") as f:
    print(f.read())


# overwriting the existing content 

with open("demofile.txt", "w") as f: # the " w " method will overwrite the entire file
    f.write("woops i deletaed the content because of chiku chamcham masti")


with open("demofile.txt","r") as f :
    print(f.read())


# create a new file 
# to create a new file in pyhton use open() method with one parameter

# "x" - create - will create and return error if file exists


# create a new file 
f = open("myfile.txt", "x")


with open("myfile.txt","a") as f:
    f.write("i create d a new file watch it for me ")

with open("myfile.txt","r") as f:
    print(f.read())


# python delete file 
 # through the os.remove() you can delete a file 

import os 
os.remove("demofile.txt")


# check if file exists 

import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print(" the file does not exists")


# delete a folder 

# for delete the entire folder use os.rmdir() 

import os 
os.rmdir("myfolder")