def sum_of_squares(a):
    return a * a


def sum_of_first_two_squares(a, b):
    sumit = a + b
    return sumit


square_input = input("Please enter the number that requires square value: \n")
square_input = square_input.split()
input_int = list(map(int, square_input)) # typecasting
square = list(map(sum_of_squares, input_int)) # square function pass as a arguement
print(square)
sumit_of = sum_of_first_two_squares(square[0], square[1])
print(sumit_of)
Sum = sum(square)
print(Sum)
