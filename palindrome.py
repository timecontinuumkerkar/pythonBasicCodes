"""Here we have created a function called palindrome
it returns reversed string. if the string matches then
it prints palindrome else it prints not a palindrome"""


def palindrome(abc):

    list1 = list(abc)
    list2 = []
    for i in range(len(list1) - 1, -1, -1):
        list2.append(list1[i])

    string_op = ''.join(list2)
    return string_op


string_input = input("Please Enter something:")
boolean_text = palindrome(string_input)
if boolean_text == string_input:
    print("Palindrome")
else:
    print("Not a palindrome")
