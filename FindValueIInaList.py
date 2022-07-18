#  Write a Python program to check whether a specified value is contained in a group of values.
List = [1, 2, 3, 4, 5, 6, 7, 4, 6, 4]
count = 0
for i in range(len(List)):
    if List[i] == 4:
        count = count + 1
        print(f"The value 4 found at pos {i}")

print(count)
