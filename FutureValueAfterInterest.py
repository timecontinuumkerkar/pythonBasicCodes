# Write a Python program to compute the future value of a
# specified principal amount, rate of interest, and a number of years.
amount = int(input("Enter the amount"))
interest_rate = float(input("Enter the interest rate"))
years = int(input("Enter the years"))
Actual_value = amount * ((1 + (0.01 * interest_rate)) ** years)
months = years * 12
EMI = Actual_value / months
print(f"The actual value after to be paid is {Actual_value} at an interest rate {interest_rate} \n"
      f"and EMI is {EMI} monthly")
