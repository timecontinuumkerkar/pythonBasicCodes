print('Enter your weight')
weight = int(input())
print('Enter your height')
height = float(input())
x = 0
count = weight / (height**2)
while x < 4:
    if count <= 18.5:
        print('Underweight')
    elif count >= 18.5 and count <=25:
        print('Normal')
        break
    elif count > 25 and count < 30:
        print('Overwight')
        break
    elif count >=30:
        print('Obesity')
        break
    else:
        print('Invalid')
        break
x += 1