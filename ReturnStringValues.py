# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.
String = input("Enter the string you want:")


def string_returning_function(x):
    if len(x) < 2:
        return x
    else:
        return x[0] + x[1]
    pass


print(string_returning_function(String))
