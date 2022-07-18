# Calculate the difference between two dates in days

from datetime import date
f_year = int(input("Input First Year"))
f_month = int(input("Input first month"))
f_day = int(input("Input first day"))
s_year = int(input("Input Second Year"))
s_month = int(input("Input Second month"))
s_day = int(input("Input Second day"))
f_date = date(f_year, f_month, f_day)
s_date = date(s_year, s_month, s_day)
difference_days = s_date - f_date
print(abs(difference_days.days))
