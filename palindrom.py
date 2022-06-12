#palidrome for input string 

def palindrome(x):
    # converting to list for traversing
    list_x = list(x)
    #empty list to return reversed list
    list_y = []
    #list length
    n = len(list_x)
    #traversing in reverse
    for i in range(n-1,-1,-1):
        #appending reversed traversed list to list of Y
        list_y.append(list_x[i])
    # comparison
    if list_x == list_y:
        return True
    else:
        return False

x = input("Bhai tera string enter kar \n")

if palindrome(x) == True:
    print("Palindrome")
else:
    print("Not a palindrome")



