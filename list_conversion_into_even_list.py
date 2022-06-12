#convert the given list into even number list and print it
list = [1,2,3,4,5,6,7,8,9,0]
even_list= []
for i in range(len(list)):
    if list[i] % 2 == 0 and list[i] != 0:
        even_list.append(list[i])
print(even_list)