#String
myString="This is my String"
print(myString)
print(type(myString))

print(myString+" is of data type "+str(type(myString)))

firstString="Water"
secondString="Fall"
thirdString=firstString+secondString

print(thirdString)

#Input

name=input("What is your name? ")
color=input("What is your fav color? ")
animal=input("What is your fav animal? ")
print(name)

print("{}, you like a {} {}!".format(name,color,animal))