# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
month = 0
total_paid = 0.0

while principal > 0:
    month=month+1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        extra_payment = 1000
    else:
        extra_payment = 0
    #print("month is", month, "so extra is", extra_payment)
    principal = principal * (1+rate/12) - (payment + extra_payment)
    total_paid = total_paid + (payment + extra_payment)
    print(month, round(total_paid,2), round(principal,2))

print('Total paid', round(total_paid,2))
print('Months', month)