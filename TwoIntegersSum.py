#  Write a Python program to sum of two given integers. However, if the sum is between 15 and 20 it will return 20.
x, y = map(int, input().split())
Sum = x + y
if 15 < Sum < 20:
    Sum = 20
    print(Sum)
else:
    print(Sum)
