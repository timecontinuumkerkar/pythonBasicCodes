# n number of elements in list
# find top K elements with length specified in n

a = [1,1,2,3,5,8,13,21,34,55,89]
n = 11
k = 3
sum = 0
for i in range(n):
    sum = sum + a[i]

mean = int(sum / n)

list = []
for i in range(n):
    if a[i] > mean:
        list.append(a[i])
