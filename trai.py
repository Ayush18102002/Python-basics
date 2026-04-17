"""
x = ("pineapple","kiwi","oranges")
y = list(x)
y[1] = "apple"
print(y)
print(type(y))

print(type(x))

txt = " we are so-called \"viking\" from the north "
print(txt)
"""

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