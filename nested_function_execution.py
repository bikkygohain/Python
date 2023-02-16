#Set
#   -   Another built-in data type of python
#   -   as with Lists, used to store multiple items of data
#   -   does NOT allow duplicate values
calculation_to_units = 24 * 60
name_of_unit = "hours"


def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered a 0, Please enter a valid positive number")
        else:
            print("You have entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user. enter a number of days as a comma separated list and I will convert it to hours\n")

    list_of_days = user_input.split(", ")

    print(type(list_of_days))
    print(type(set(list_of_days)))

    print(list_of_days)
    print(set(list_of_days))

    for num_of_days_element in set(list_of_days):
        validate_and_execute()

# Nested Function Execution
# print(type(set(list_of_days)))
# 1. set(list_of_days)
#     => Input: the user input array
#     => Output: returns the converted set
#
# 2. type(return_value_of_previous_func)
#     => Input: the converted set
#     => Output: returns the data type of the set
#
# 3. print(return_value_of_previous_func)
#     => Input: the data type
#     => Output: prints the value to console
