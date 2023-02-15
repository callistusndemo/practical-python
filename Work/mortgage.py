# mortgage.py
#
# Exercise 1.7
"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.

Here is a program that calculates the total amount that Dave will have to pay over the life of the mortgage:
"""

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

while principal > 0:

    print(total_paid, month)

    if month > 12:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    else:
        principal = principal * (1+rate/12) - (payment + 1000)
        total_paid = total_paid + payment 

    month += 1 
    
print('Total paid', total_paid)


