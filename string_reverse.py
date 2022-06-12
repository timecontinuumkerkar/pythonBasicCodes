x = "karan"
# To reverse a string

def rev(x):
    list_1 = list(x.strip(" "))
    rev_list=[]
    for i in range(len(list_1)-1,-1,-1):
        rev_list.append(list_1[i])
    return rev_list

def string_rev(y):
    str1 = ""
    return (str1.join(y))

y = rev(x)
print(y)
print(string_rev(y))


