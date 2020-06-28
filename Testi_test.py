import math

credit_principal = input('''What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal:''')
if credit_principal == 'n':
    money = int(input('Enter credit principal:'))  # P
    monthly_payment = int(input('Enter monthly payment:'))  # A
    credit_interest = int(input('Enter credit interest:'))  # i  процент
    i = (0.01 * credit_interest / 12)
    n = math.log((monthly_payment / (monthly_payment - i * money)), 1 + i)
    n = round(n, 1)
    if (str(n))[-1] >= '5':
        n = math.ceil(n)
    else:
        n = math.floor(n)
    year = n // 12
    month = n - year * 12
    if year > 1:
        year = str(year) + " " + "years"
    elif year == 1:
        year = "1 year"
    else:
        year = ''

    if month > 1:
        month = str(month) + " " + "months"
    elif month == 1:
        month = "1 month"
    else:
        month = ''
    if month != 0 and year != 0:
        final = "You need {} and {} to repay this credit!".format(year, month)
    else:
        final = "You need {}{} to repay this credit!".format(year, month)
    print(final)
elif credit_principal == "p":
    monthly_payment = float(input('Enter monthly payment:'))  # A
    periods = int(input("Enter count of periods:")) # n
    credit_interest = float(input('Enter credit interest:'))  # i
    i = (0.01 * credit_interest / 12)
    P = int(monthly_payment /((i * ((1 + i) ** periods))/(((1 + i) ** periods) - 1)))
    print('Your credit principal = ' + str(P) + '!')