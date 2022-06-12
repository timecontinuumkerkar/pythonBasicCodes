#finding if the input number is present in both the list
a = [1,2,3,4,5]
b = [2,5,6,7,8]
x = int(input("Please enter a value to search"))
if x in a and x in b:
    print(f"the value {x} is present in both the lists.")