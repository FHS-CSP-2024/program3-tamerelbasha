# More about variables #
#**Learning objectives**
#
#After this section:
#
#* You will be able to use variables in different contexts
#* You will know what kind of data can be stored in variables
#* You will understand the difference between strings, integers and floating point numbers


name="Bob"
print(name)


myString= "something"
myInt= 100
myFloat= 2.5

print(myInt/2)
MynewInt= "100"
print(int)(MynewInt/2)


num1 = input("Please enter a number")

print(int(num1)) + int(num1)

print("My int="+str(myInt))

print(num1+num1)

thing=500/6
print(thing)
print("My result is"+str(thing))
print("My result is", thing)
print(f"Theresult is {thing}") 


print("First line\nSecond line\nThird line")
print("List header")
print("\tItem1")
print("\tItem2")
print("\tItem3\n\t* Item4\n\t* Item5")


print("c:\\User\\mrJohnson\\Document\\OKDJflsjdkfalksd...")







## Live Demo ##
#
# Casing
#name = input("What is your name? ")
#Name = input("What is your name? ")
#print(name)
#print(Name)
#
# Talk about Variable Types
#   * int vs string vs float
#intNum = 75
#print(intNum/2)
#number = "100"
#print(number / 2)
#number1 = 2.5
#number2 = -1.25
#number3 = 3.62
#
#print(f"Mean: {mean}")
#mean = (number1 + number2 + number3) / 3
#
# Printing different types and Casting
#result = 10 * 25
#print("The result is " + result)
#print("The result is " + str(result))
#print("The result is", result)
#print(f"The result is {result}") # Format string {} denotes values to be printed
#name = "Mark"
#age = 37
#city = "Palo Alto"
#print(f"Hi {name}, you are {age} years old. You live in {city}.")
#
# Printing invisible things
#print("\n") # newline
#print("\t") # tab
#print("\\") # \
