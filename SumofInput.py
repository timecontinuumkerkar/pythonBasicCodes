# Print the following sum 5 + 55 + 555. The answer is 615.
n = int(input("Enter any number"))
FirstValue = int("%s" % n)
SecondValue = int("%s%s" % (n, n))
ThirdValue = int("%s%s%s" % (n, n, n))
Sum = FirstValue + SecondValue + ThirdValue
print(Sum)
