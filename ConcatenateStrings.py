# Write a Python program to concatenate all elements in a list into a string and return it.
List = [1, 2, 3, "karan", 4, 5, 6, "ABCD"]
x = ""
for i in range(len(List)):
    x = x + str(List[i])
print(x)
