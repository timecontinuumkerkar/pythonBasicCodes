

def maximum(list1):
    list1.sort()
    n = len(list1)
    for i in range(n):
        if list1[i] == list1[n-2]:
            return list1[i]

def minimum(list2):
    y = min(list1)
    return y

list1 = [1,200,2000,225,325,4000,12345]
print(minimum(list1))
print(maximum(list1))
