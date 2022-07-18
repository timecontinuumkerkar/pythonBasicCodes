# Write a Python program that will return true if the two given
# integer values are equal or their sum or difference is 5.
x, y = map(int, input("Enter the numbers with a space").split())


def integer_op(a, b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False


print(integer_op(x, y))
