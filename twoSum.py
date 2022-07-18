"""Get a list of integers and find sum of largest two values"""
List = []
n = int(input("Enter the range number"))
for i in range(n):
    Input = int(input("Enter for list append"))
    List.append(Input)
List.sort()
Sum = List[n-1] + List[n-2]
print(Sum)
