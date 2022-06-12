#finding if the all numbers are present in both the list
# Also they should not be identical
a = [1,2,3,4,5]
b = [2,2,5,6,7,8]
c = []
for i in range(len(a)):
    for y in range(len(b)):
        if a[i] == b[y] and a[i] not in c:
            c.append(a[i])

print(c)