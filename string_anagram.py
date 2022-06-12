#String anagram / to find matching letters
# step 1 convert into a list both string 
# then sort them
# then compare 
# if true return anagram
# if false return false
string1 = "I am beautiful"
string2 = "beautiful I am"

#converting into lower case letter
string1 = string1.lower()
len1 = len(string1)
string2 = string2.lower()
len2 = len(string2)

# Converting into string
list1 = list(string1.strip(""))
list2 = list(string2.strip(""))

#sortting
list1.sort()
list2.sort()


#removing spaces
x= string1.replace(" ","")
y= string2.replace(" ","")


if x == y:
    print("Anagram")
else:
    print("Not a anagram")