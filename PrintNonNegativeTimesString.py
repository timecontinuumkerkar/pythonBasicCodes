#  Write a Python program to get a string which is n (non-negative integer) copies of a given string
# Output = abcabc or .test.test.test
def printing_string(String, num):
    res = ""
    for i in range(num):
        res = res + String
    return res


print(printing_string(".test", 3))
print(printing_string("abc", 2))
