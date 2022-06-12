# convert a string into palindrome
x = "abccba"
y = "1233121"

x_list = list(x.strip(" "))
y_list = list(y.strip(" "))

def palindrome(abc):
    list = []
    for i in range(len(abc)-1,-1,-1):
        list.append(abc[i])
    if list == abc:
        return True
    else:
        return False


if palindrome(y_list) == True:
    print("Palindrome")
else:
    print("Not a Palindrome")
