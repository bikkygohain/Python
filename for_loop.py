# Looping
# To execute logic multiple times
# Python has 2 loop commands
# List
#   -   To store multiple items in a single variable
# For Loop
# Is used for iterating over a sequence (like a list)
# So we can execute smth for each item in a list
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
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_element in user_input.split(","):
        validate_and_execute()
