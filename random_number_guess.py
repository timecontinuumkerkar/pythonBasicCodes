import random 

random_integer = random.randint(1,9)
user_input = int(input("Enter the value:"))
if user_input == random_integer:
    print("Exactly right")
elif user_input < random_integer:
    print("Too low")
elif user_input > random_integer:
    print("Too High")
else:
    print("Invalid Input:")

