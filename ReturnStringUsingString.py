# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.
def string_function(var):
    if len(var) >= 2 and var[:2] == "Is":
        return var
    else:
        return "Is" + var
    pass


print(string_function("Array"))
