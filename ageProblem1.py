x = 0
sum = 0
for x in range(5):
    print('Please Enter age:')
    age = int(input())
    if age <=3:
        continue
    elif age > 3:
        sum = sum + 100
x += 1
print(sum)

# This code is for getting the sum of ticket
# all users where user's age is above 3
# Each ticket costs 100$
