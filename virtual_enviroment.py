# python virtual env
# it is use to isolate your python project so that it run and test your code without interrupting the different project
# it was like a seperate container for ech python project

# has it own python intrepreter
# has it own set of installed packages
# is isolated from other virtual enviroments
# can have diff. version of the same package 

# -- using virtual enviroments is important bacause: 

# it prevents package version conflicts between projects
# makes projects more portable and reproducible 
# keep your system python installation clean
# allows testing with different python versions



# python -m venv myfirsttrai -- run this command into the termnal to create a myfirstproject folder 
# and after executing it create a folder and inside this we have subfolders 
# folder structure -- myfirsttrai
#-- include
# -- Lib
# -- scripts
#.gitignore
# pyvenv.cfg

# after that activate it throught this command
# myfirsttrai\scripts\activate

# After activation, your prompt will change to show that you are now working in the active environment:

# install packages 
# using pip install we can downolads packages

# cowsay packages -- pip install cowsay

# now we use the cowsay package
# first import the cowsay 

import cowsay
cowsay.cow("mowwwwwwwwwwwwwwwwwwwwwww!")

# for run this code we use python virtual_enviroment.py


# for deactivate the virtual enviroment use ' deactivate '

# for delete the virtual eviroment 
# use this command -- rmdir /s /q myfirsttrai