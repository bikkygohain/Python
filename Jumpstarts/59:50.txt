# Simple Print
print("-------------------------------------------------------")
print("Basic Introdcution Datatypes")
print("-------------------------------------------------------")
print("200 is a great number")
# Number and Strings
print(3.5) # => Float
print(3) # => Integer
# Arithmetic Operations
print(20 * 24 * 60)
# String concatenation (Add strings together)
print("20 days are " + str(20 * 24 * 60) + " minutes")
print(20 * 24 * 60)
# Here "f" stands for format
print(f"20 days are {20 * 24 * 60} minutes")
# another tricky way! works on latest python versions
# Variables in python
# Use descriptive variable names as it helps in future maintenance
print("-------------------------------------------------------")
print("Variables")
print("-------------------------------------------------------")

calculation_to_units = 24
name_of_unit = "hours"

print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
print(f"35 days are {35 * calculation_to_units} {name_of_unit}")
print(f"50 days are {50 * calculation_to_units} {name_of_unit}")
print(f"110 days are {110 * calculation_to_units} {name_of_unit}")

# Variables are container for storing values
# Python is dynamically typed
# to_seconds = 24 * 60 * 60
# Vs Static Typing:
# int to_seconds = 24 * 60 * 60
# String some_string = "static typed"
# NAMING CONVENTIONS
# Naming convention is a convention (generally agreed scheme) for naming things
#     - Use lowercase with words separated by underscores
# Reserved words (also called keywords) are defined with predefined meaning and
# syntax in the language.

# Functions
# To avoid repeating the same logic
# A function is defined using the def keyword
# A block of code which only runs when it is called
# Calling a function = to execute the function
print("-------------------------------------------------------")
print("Functions")
print("-------------------------------------------------------")
# Always read other developers code for better understanding of coding styles
# Always add two blank lines before defining a function helps in better understanding


def days_to_units():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
    print("All good!")


days_to_units()
# Function parameters
# Information can be passed into functions as parameters
# Parameters are also called arguments
print("-------------------------------------------------------")
print("Functions with Parameters")
print("-------------------------------------------------------")


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)


days_to_units(20, "Awesome!")   # Less code
days_to_units(35, "Looks Good!")   # reduced code duplication
days_to_units(50, "Yupiee!")   # more descriptive
days_to_units(110, "cool!")

# Scope
# A variable is only available from inside the region it is created
#   - Global Scope = variable available from within any scope
#   - Local Scope = variables created inside function can only be used inside that function
print("-------------------------------------------------------")
print("Scope")
print("-------------------------------------------------------")

global_variable = "example"


def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_unit) # Global scope
    print(num_of_days) # Local scope
    print(my_var)

scope_check(7)
