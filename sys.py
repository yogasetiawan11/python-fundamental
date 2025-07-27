calculation_to_units = 24
name_of_units = "hours"

def days_of_unit(num_of_days):
    if num_of_days > 0:
        return f'{num_of_days} is your number of days {num_of_days * calculation_to_units} {name_of_units}'
    else: 
        return 'you entered a negative number'

users_input = input("Enter the number of days: ")
users_input = int(users_input)

print(days_of_unit(users_input))

