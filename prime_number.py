# get a number from the input from the user 
# and ask the print the prime number within the range
# starting from one

class prime_number:
    def prime(self,n:int):
        list = []
        for i in range(1,n+1):
                if i % 1 == 0:
                    list.append(i)
        return list


user_input = int(input())

meta = prime_number()
x = meta.prime(user_input)
print(x)


