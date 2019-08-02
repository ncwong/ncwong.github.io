#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
names = ["Rach", "Jay", "Audrey", "Ellie", "Deysey"]
lastnames = ["Smith", "Buble", "White"]
#Generates a random integer.
aRandomIndex = randint(0, len(names)-1)
print(names[aRandomIndex])

RandomIndex2 = randint(0, len(lastnames)-1)
print(lastnames[RandomIndex2])
