def remove_duplicates(list):
    new_list = []
    for i in range(len(list)):
        if list[i] not in new_list:
            new_list.append(list[i])

list = [1,2,2,2,3,3,4,4,5,6,6,6,7,7,8,8,9,9,9,9,9]
print(remove_duplicates(list))
