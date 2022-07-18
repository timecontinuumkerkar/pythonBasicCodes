# To display first and last value of the colors list
List = []
n = int(input("Enter Number of Colors"))
for i in range(n):
    String = input("Enter a Color:")
    List.append(String)
print(List[0])
print(List[n-1])
print(f"The first color is {List[0]} and the last color is {List[n-1]}")

