# Write a Python program to test whether a passed letter is a vowel or not.
List = ['a', 'e', 'i', 'o', 'e']

n = 5
for i in range(n):
    Input = input("Enter a value")
    if Input in List:
        print(f"{Input} is present in the list")
    else:
        print(f"{Input} not present in the loop")
