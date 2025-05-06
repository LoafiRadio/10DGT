# Demonstrate how variables are created and how they work
# Author: Samuel Lee
# Date: 2023-10-01
# Version: 1.0.0
# Description: This script demonstrates the creation and usage of variables in Python.
# It covers variable assignment, naming conventions, and basic operations.
# It also includes examples of using variables in functions and classes.
# It is designed to be run in a Python environment.

# There are different types of variables
# Store a number
my_number = 80 # assigning 80 to my_number
print(my_number) 

my_number2 = 7 # have reassigned my_number (variable)
print(my_number2)

# Store a string
name_1 = "Samuel"
print(name_1)

# assign the value of one variable to another
my_number = name_1 # Don't assign values to variables that are not

# creating a new variable
num_1 = 5
num_2 = 17

''' Do not calulate with variabes and store the results in
another variable I can now
press
enter
as
many times
 as I want'''

sum1 = 5 + 17 # this is not good practice
print(sum)

# better way to do it
sum1 = num_1 + num_2
print(sum)

sumstring1 = "17" # This stores a string
sumstring2 = "5"

# adding strings together is called concatenation
sum = sumstring1 + sumstring2
print(sum)
print(sum1)

print(f"My calculation for {sumstring1} + {sumstring2} = {sum1}")

