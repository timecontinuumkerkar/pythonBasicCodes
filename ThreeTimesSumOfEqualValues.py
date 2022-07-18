#  Write a Python program to calculate the sum of three given numbers,
#  if the values are equal then return three times of their sum
def sum_of_thrice(x, y, z):
    Sum = x + y + z

    if x == y == z:
        Sum = Sum * 3

    return Sum


print(sum_of_thrice(1, 2, 3))
print(sum_of_thrice(3, 3, 3))


