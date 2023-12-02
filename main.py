# First Python Program

print("Hello World", 5)
print(5)
print(9*80)

# Comments, Excape Sequences & Print Statemennt

"""
Hey guys, this is a way to comment `Multi-Lines`
Author: Alqama
"""
print("Hey guys I am \"Alqama\"\nand I am learning python")

print("Hello World")
# This is a 'Single-Line Comment'
print("This is a print statement.")
print("Hello World !!!") # Printing Hello World!

print("Hello", 4,5,6, sep="/", end="=")
print("Alqama")

# Variables & Data Types

a = True
b = complex(6 , 5)
number = 7980230005
name = "Alqama"
number1 = 9
number2 = 7.2
print(b)
print(number)
print(name)
print(number + number1)

# # Check the type of a variable
print("The type of Name is:", type(name))
print("The type of Number is:", type(number))
print("The type of Number is:", type(number2))
print("The type of A is:", type(a))
print("The type of B is:", type(b))

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name": "Alqama", "age": 18, "canVote": True}
print(dict1)

# Operators & Exercise: Calculator

print(5+7) # Addition
print(15-7) # Subtraction
print(15*7) # Multiplication
print(2**4) # Exponential
print(15/7) # Division
print(15//7) # Floor Division
print(15%7) # Modulus

# Exercise

a = 5
b = 2

print("The value of", "'", a, "+", b, "'", "is:", a + b)
print("The value of", "'", a, "-", b, "'", "is:", a - b)
print("The value of", "'", a, "*", b, "'", "is:", a * b)
print("The value of", "'", a, "/", b, "'", "is:", a / b)
print("The value of", "'", a, "//", b, "'", "is:", a // b)
print("The value of", "'", a, "%", b, "'", "is:", a % b)


# TypeCasting

a = "1"
# a = 1
b = "2"
# b = 2

print(int(a) + int(b))

# Explicit TypeCasting
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

# Implicit TypeCasting
c = 1.8
d = 7

print(c + d)

# User Input

a = str(input("Please enter your name: "))
print("Hi, Nice to meet you", a)

x = int(input("Enter you number: "))
y = int(input("Enter you second number: "))
print(x+y)
print(int(x)+int(y))