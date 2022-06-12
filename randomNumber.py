#generate a random number in the range 0 to 999 which is divisible by 5
import random
n = 3
for i in range(n):
    random_int = random.randrange(0,999,3)
    while random_int > 100:
        print(random_int)
        break