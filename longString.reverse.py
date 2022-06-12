#reverse an input long string.
# print the exact words in reverse order

#input string
x = input("Please enter the input string\n")

# converting into list to get different words in indexes
list_x = x.split(" ")

#print
print(list_x)

#empty list for filtering
list_y = []

#for loops for reversing indexes
for i in range(len(list_x)-1,-1,-1):
        list_y.append(list_x[i])


#Joining and adding in string    
y = " ".join(list_y)

#print
print(y)
