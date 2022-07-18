# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
Sum = 0
List = list(map(int, input("Enter the numbers \n ").split()))
if List[0] == List[1] or List[1] == List[2] or List[0] == List[2]:
    Sum = 0
else:
    Sum = List[0] + List[1] + List[2]

print(Sum)
