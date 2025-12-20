# Import Methods and DIR function
import os
import math # To use all the math.etc functions and variables.
# from math import sqrt, floor # Importing specific math functions and variables.
# import math as m # Rename while importing a package.
# from math import * # Importing all functions and variables from math package.

print(dir(math)) # To see all the Math package functions and variables.

# Print Statemennts

print("Hello World")
print(5)
print(9*80)

# Comments, Excape Sequences

# This is a 'Single-Line Comment'
"""
Hey guys, this is a way to comment `Multi-Lines`
Author: name
"""

# This is a print statement with an escape sequence to print double quotes and a new line.
print("Hey guys I am \"name\"\nand I am learning python")
# This is a print statement with custom separator and end character.
print("Hello", 4,5,6, sep="-", end="=")
print("End")

# Variables & Data Types

a = True
b = complex(6 , 5)
number = 7980230005
name = "name"
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

dict1 = {"name": "name", "age": 18, "canVote": True}
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
b = 5

print("The value of a + b", end=" = ")
print(a + b)
print("The value of a - b", end=" = ")
print(a - b)
print("The value of a * b", end=" = ")
print(a * b)
print("The value of a ** b", end=" = ")
print(a ** b)
print("The value of a / b", end=" = ")
print(a / b)
print("The value of a // b", end=" = ")
print(a // b)
print("The value of a % b", end=" = ")
print(a % b)

# New way F-String to do the same exercise
firstNum = int(input("Enter your number: "))
secondNum = int(input("Enter your second number: "))
operation = input("Enter your operation: ")

if operation == "+": 
    print(f"The value of {firstNum} {operation} {secondNum} = {firstNum + secondNum}")
elif operation == "-": 
    print(f"The value of {firstNum} {operation} {secondNum} = {firstNum - secondNum}")
elif operation == "*": 
    print(f"The value of {firstNum} {operation} {secondNum} = {firstNum * secondNum}")
elif operation == "*8": 
    print(f"The value of {firstNum} {operation} {secondNum} = {firstNum ** secondNum}")
elif operation == "/": 
    print(f"The value of {firstNum} {operation} {secondNum} = {firstNum / secondNum}")
elif operation == "//": 
    print(f"The value of {firstNum} {operation} {secondNum} = {firstNum // secondNum}")
elif operation == "%": 
    print(f"The value of {firstNum} {operation} {secondNum} = {firstNum % secondNum}")
else:
    print(f"Invalid Operation: {operation}")


# TypeCasting

a = "1"
a = 1
b = "2"
b = 2

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

# Slicing and Operations on Strings

name = "alqama" # Strings are immutable in Python
nameLen = len(name) # Length method to find length of string which is 6 here.
print(nameLen)
print(name[0:5]) # Output: alqam, Why: Here slicing starts from index 0 to index 5-1=4.
print(name[1:5]) # Output: lqam, Why: Here slicing starts from index 1 to index 5-1=4.
print(name[:5]) # Output: alqam, Why: If we don't provide starting index it will consider it as 0.
print(name[0:-3]) # Output: alq, Why: If i we add negative values while slicing the strings python will calculate with length of the variable.
print(name[-4:-2]) # Output: qa, Why: Here -4 means 6-4=2 and -2 means 6-2=4 so it will slice from index 2 to index 4.
print(name[0:6:2]) # Output: aqm, Why: Here step value is 2 means it will take every 2nd character.
print(name[::-1]) # Output: amaqla, Why: Here step value is -1 means it will reverse the string.
print(name.upper())
print(name.lower())
print(name.rstrip("a")) # Output: alqam, Why: Because rstrip() removes the specified character from the right end of the string.
print(name.capitalize())
print(name.replace("a", "x")) # Output: xlqxmz, Why: Because all a's are replaced with x.
print("ama" in name) # Output: True, Why: Because ama is present in name.
print("xyz" in name) # Output: False, Why: Because xyz is not present in name.
print("ama" not in name) # Output: False, Why: Because ama is present in name.
print("xyz" not in name) # Output: True, Why: Because xyz is not present in name.
print(name.count("a")) # Output: 2, Why: Because a is present 2 times in name.
print(name.find("q")) # Output: 3, Why: Because q is present at index 3 in name.
print(name.find("z")) # Output: -1, Why: Because z is not present in name.
print(name.endswith("a")) # Output: True, Why: Because name ends with a.
print(name.startswith("a")) # Output: True, Why: Because name starts with a.
print(name.isalnum()) # Output: True, Why: Because name contains only alphabets and numbers.
print(name.isalpha()) # Output: True, Why: Because name doesn't contains numbers.

# If Else Conditional Statements

age = int(input("Please enter your age: "))

if age>=18:
    print("You are adult now, You can drive.")
else:
    print("You are not adult, You cannot drive.")

# Match case statements

match age:
    case 0 | 1 | 2 | 3 | 4 | 5:
        print("You are a baby.")
    case 6 | 7 | 8 | 9 | 10 | 11:
        print("You are a kid.")
    case 12 | 13 | 14 | 15 | 16 | 17:
        print("You are a teenager.")
    case _ if age >= 18:
        print("You are an adult.")
    
# For, While loops with break and continue statements
loopText = "loop"
for i in loopText:
    print(i)

loopList = ["Red", "Green", "Black", "White"]
for i in loopList:
    print(i)

for i in range(10, 100, 5):
    print(i)

i = int(input("Enter the number: "))
while(i<=28):
    i = int(input("Enter the number: "))
    print(i)
else:
    print("Done with the loop.")

# Break
for i in range(12):
    if(i == 10):
        print("Skip the loop")
        break
    print(f"5 X {i} = {i+1}")

# Continue
for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print(f"5 X {i} = {5*i}")

# Functions
def calculateGMean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

calculateGMean(7,8)

def emptyFunc():
    pass

# Lists methods and slicing 

marks = [3, 5, 6, "alqama", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

print(marks[-3]) # Negative index
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

if "6" in marks:
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
if "al" in "alqama":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

marks = [11,2,4,6,7,8,7]
ext = [9,10,11,12]
marks.append(7)
marks.sort(reverse=False)
marks.reverse()
marks.insert(1, 3)
marks.extend(ext)
print(marks.index(7))
print(marks.count(7))
print(marks)

# F Strings and Format methods
str = "Hello, My name is {} and I am from {}."
str1 = "Hello, My name is {1} and I am from {0}."
name = "Alqama"
country = "India"
num = 55.45555
# Old way to format string with variables values:
print(str.format(name, country))
print(str1.format(country, name))
# New and way to do it:
print(f"Hello, My name is {name} and I am from {country}.")
# .2f will format the float value to 2 decimal places, Which is 55.46 here:
print(f"The number is {num:.2f}")
# If I want to print as it is while using f-string:
print(f"Hello, My name is {{name}} and I am from {{country}}.") # I can use 2 brackets.

# DocStrings and PEP-8
def square(n):
    '''Takes in a number n, returns the sqaure of n'''
    print(n**2)
def square1(n):
    print(n)
    '''Takes in a number n, returns the sqaure of n'''
    print(n**2)
square(5)
print(square.__doc__)
print(square1.__doc__) # Output: none because docstring is not in the right place, it should be just after the function definition PEP-8 Standard.

# Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(6)) # Output: 720 (6 X 5 X 4 X 3 X 2 X 1 = 720)

# Function to get Fibonacci Sequence
def f(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return [0, 1]
    else:
        seq = f(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
num = int(input("Enter a number: "))
print(f(num)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Sets and Methods
s = {0,1,2} # Set is unordered (Not maintain any order) also Set not accept duplicate values.
s = set()
print(s)
print(type(s))

s2 = {4,5,6,7}
s3 = s
print(s.union(s2))
s.update(s2)
s.difference_update(s2)
s.intersection_update(s2)
s4 = s.isdisjoint(s2)
s4 = s.issuperset(s3)
s4 = s.issubset(s2)
s.add(3)
s.remove(0)
s.discard(0)
s.clear()
s4 = s.pop()
del s2
print(s4)

# Dictionaries and Methods
dicti = {
    "Name": "Alqama",
    "Country": "India"
}

print(dicti["Name"])
print(dicti.get("Name"))
print(dicti.keys())

for key in dicti.keys():
    print(f"The value corresponding to the key {key} is {dicti[key]}")

for key,value in dicti.items():
    print(f"The value corresponding to the key {key} is {value}.")

dicti2 = {
    "Profession": "Software Engineer"
}
dicti.update(dicti2)
dicti.clear()
dicti.pop("Country")
dicti.popitem()
del dicti["Name"]
print(dicti)

# For Loop with else Statement
for i in range(5):
    print(i)
else:
    print("No I.")

# Exception Handling
try:
    num = int(input("Enter a number: "))
    li = [1,2,3,4]
    print(num)
    print(li[num])
except ValueError:
    print("The provided value is not an integer.")
except IndexError:
    print("The provided index is not in list.")
except Exception as e:
    print(e)
finally:
    print("Always Executed.")

# Raising custom errors
num = int(input("Enter a number: "))

if num.strip().lower() == "quit":
    print("Quited.")
elif num < 1 and num > 10:
    raise ValueError("The entered number should be between 1 - 10!")
else:
    print("Not match.")

# Short hand If else statements
a = 300
b = 500
print(a) if a > b else print (b) if a == b else print("B")

c = 9 if a > b else 0
print(c)

# Enumerate Function
marks = [12,23,35,67,99,24,47,89,19]

for index, mark in enumerate(marks): # Index will hold the index and mark will hold the value at that index.
    print(f"Alqama has great marks, Which is: {mark}.") if index == 4 else print(mark)

# OS Module
def dirExists(path):
    return os.path.exists(path)

os.makedirs("data", exist_ok=dirExists("data"))

for i in range(20):
    # os.makedirs(f"data/day-{i+1}-of-code", exist_ok=dirExists(f"data/day-{i+1}-of-code"))
    # os.rename(f"data/day-{i+1}-of-code", f"data/Day {i+1} of Code")
    os.makedirs(f"data/Day {i+1} of Code", exist_ok=dirExists(f"data/Day {i+1} of Code"))

folders = os.listdir("data")
# print(folders)

for folder in folders:
    print(f"The {folder} folder has: {os.listdir(f"data/{folder}")} files.")

print(os.getcwd())

# Local vs Global Variables
x = 5 # Global

def variables():
    global x # Like this we can change a global variable inside function.
    x = 10
    z = 10 # Local
    print(x,z) # Output: 10, 10, also x is not a local variable here it is global and we are changing it.

variables()