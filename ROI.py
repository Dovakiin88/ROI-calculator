class Income:
    def income_sources(self):
        rental = int(input('What do you charge for rental? '))
        laundry = int(input('What do you charge for laundry? '))
        storage = int(input('What do you charge for storage? '))
        misc = int(input('What do you charge for misc? '))

        total_income = rental + laundry + storage + misc
        print(f'Your total income is {total_income}')
        return total_income


class Expenses:
    def expense(self):
        tax = int(input('Enter Tax amount: '))
        ins = int(input('Enter Insurance amount amount: '))
        utils = int(input('Enter utilities: '))
        hoa = int(input('Enter HOA fees: '))
        care = int(input('Enter maintenance expenses: '))
        vacancy = int(input('Enter Vacancy amt: '))
        repairs_capex = int(input('Enter total cost to replace items: '))
        management = int(input('Enter management Expense: '))
        mortgage = int(input('Mortgage: '))

        tot_expense = tax + ins + utils + hoa + care + vacancy + repairs_capex + management + mortgage
        print(f'Your total expenses are {tot_expense}')
        return tot_expense


class Cash_flow(Income,Expenses):
    def cf(self):
        x = Income()
        y = Expenses()
        x1 = x.income_sources() - y.expense()
        x2 = x1 * 12
        print(f'Your monthly cash flow is {x1}. This is what you have left after expenses')
        print(f'your yearly cash flow is {x2}. This is annual revenue.')

        down_payment = int(input('How much was the down payment? '))
        closing = int(input('How much was the closing cost? '))
        re_hab = int(input('How much did you have to invest for repairs or upgrades? '))
        misc = int(input('Anything else you had to invest? '))

        invest = down_payment + closing + re_hab + misc
        print(f'You have spent a total of {invest} dollars on investments')
        roi = (x2/invest) * 100
        print(f'Your return on investment is {roi}%')


def run():
    while True:
        print('Welcome to the investment calculator')
        print(
            '''This calculator will allow you to calculate whether or not a property will be worth the investment. 
            It will do so by asking a few questions about the most common things property owners have to pay for or 
            charge for'''
        )
        print('Hear are some instruction: Y = yes, N = no, Start to begin and lastly Quit to end the program')
        begin = input('Do you wish to start the program? ')
        if begin.lower() == 'y' or begin.lower() == 'yes':
            cash = Cash_flow()
            cash.cf()
        elif begin.lower() == 'n' or begin.lower() == 'no':
            print('Have a good day')
        else:
            print('Please enter a valid option')

        print('Thank you for using our calculator')
        break


run()