import math

command_list = ['n','a','p']
option = input("What do you want to calculate?"
               "\ntype 'n' for number of monthly payments,"
               "\ntype 'a' for annuity monthly payment amount,"
               "\ntype 'p' for loan principal:"
               "\n>")

def a():
    principal = float(input("Enter the loan principal: "))
    periods = float(input("Enter the number of periods: "))
    interest_rate = float(input("Enter the loan interest: "))

    monthly_interest_rate = interest_rate / 100 / 12
    payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-periods))

    print(f"Your monthly payment = {round(payment, )}")

def p():
    annuity_payment = float(input("Enter the annuity payment: "))
    periods = int(input("Enter the number of periods: "))
    interest_rate = float(input("Enter the loan interest: ")) / 100 / 12

    loan_principal = annuity_payment / (
                (interest_rate * math.pow(1 + interest_rate, periods)) / (math.pow(1 + interest_rate, periods) - 1))

    print(f"Your loan principal = {round(loan_principal, 0)}!")
def n():
    principal = float(input("Enter the loan principal: "))
    monthly_payment = float(input("Enter the monthly payment: "))
    interest_rate = float(input("Enter the loan interest: ")) / 100 / 12
    n = math.log10(monthly_payment / (monthly_payment - interest_rate * principal)) / math.log10(1 + interest_rate)
    n_ceiled = math.ceil(n)

    years = n_ceiled / 12
    months = n_ceiled % 12

    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif years == 1 and months == 0:
        print(f"It will take 1 year to repay this loan!")
    elif years == 1 and months > 0:
        print(f"It will take 1 year and {months} months to repay this loan!")
    elif years > 1 and months == 0:
        print(f"It will take {years} years to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan")

if option in command_list:
    eval(option)()
else:
    print("Try again")
