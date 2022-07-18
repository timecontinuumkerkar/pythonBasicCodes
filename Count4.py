# Count the occurrence of number 4 in a given list
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 4, 7, 6, 7, 8, 9, 5, 4, 4, 4]
count = List.count(4)
counter = 0
for i in range(len(List)):
    if List[i] == 4:
        counter = counter + 1

print(count)
print(counter)
