# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 != 0:
        print("We got an odd number!", number, end=" ")
    else:
        print("We got an even number!", end=" ")

    number = int(input("Enter a number or type 0 to stop: "))