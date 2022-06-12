x = int(input())

def fibo(x):
    list = [0,1]
    for i in range(2,x+1):
        list.append(list[i-1]+list[i-2])
    return list

print(fibo(x))