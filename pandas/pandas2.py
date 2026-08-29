# installing pakages 

# pip install pandas

import pandas

mydataset = {
    'cars' : ["BMW","VOLVO","FORD"],
    'passings' : [3,7,2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

import pandas as pd

myvar2 = pd.DataFrame(mydataset)
print(myvar2)

# checking panda s verion use  __version__

print(pd.__version__)

