# program that asks the user for a number and then prints out a list of all the divisors of that number.
num = int(input())
listRange = list(range(1,num+1))
divisorList = []
for i in listRange:
    if num % i == 0:
        divisorList.append(i)

print(divisorList)