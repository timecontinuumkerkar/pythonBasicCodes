# Write a Python program to display your details like name, age, address in three different lines.
List = list(map(str, input("Enter name, age and address ").split()))
print(f"Your name is {List[0]}\n Your age is {List[1]} \n Your address{List[2]}")
