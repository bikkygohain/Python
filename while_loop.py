def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered a 0, Please enter a valid positive number")
        else:
            print("You have entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")

# while True:
#     user_input = input("Hey user. enter a number of days and I will convert it to hours\n")
#     validate_and_execute()

user_input = ""
while user_input != "exit":
    user_input = input("Hey user. enter a number of days and I will convert it to hours\n")
    validate_and_execute()
