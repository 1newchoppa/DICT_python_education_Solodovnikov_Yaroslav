import math

command_list = ['m','p']
loan_sum = int(input("Enter the loan principal\n>"))
option = input("What do you want to calculate?"
               "\ntype 'm' – for number of monthly payments,"
               "\ntype 'p' – for the monthly payment"
               "\n>")



def m():                             #кол-во месяцев для погашения
    m_p = int(input("Enter the monthly payment\n>"))
    months = math.ceil(loan_sum / m_p)
    print(months)

def p():                              #ежемесячный платёж
    month_number = int(input("Enter the number of months:\n>"))
    payment = math.ceil(loan_sum / month_number)
    if payment * month_number > loan_sum:
        last_payment = loan_sum - (month_number - 1) * payment
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}")
    else:
        print(f"Your monthly payment = {payment}")

if option in command_list:
    eval(option)()
else:
    print("Try again")