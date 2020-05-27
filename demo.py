def password():
    tries = 3
    while tries >= 0:
        pin = int(input('Please enter you pin in the screen please'))
        if pin == (8585):
            print("Correct... One moment please, we are fetching your inquired amount of data")
            return True
        else:
            print("Incorrect Password, please try again")
            tries += 1
    print("Incorrect Password, you have no remaining attempts to input your pin")
    return False


def start_menu():
    balance = 400

    print('Welcome to your Roblox ATM where you can perform viewing your balance, withdrawing your robux, and depositing your robux')


    if password():
        print('1  for Balance\n')
        print('2 for Withdrawal\n')
        print('3 for Deposit\n')
        print('4 To Exit\n')

        transaction = int(input('Choose which Robux transaction best fits your needs today:'))
        if transaction == 1:
            print('Your Balance is R$', balance, '\n')
            restart = input('Would You you like to go back? ')
            if restart in ('NO', 'no'):
                print('Okay, please continue on.')

        elif transaction == 2:

            withdrawl = float(input('How Much Would you like to  withdraw? \nR$80 R$400 R$800 R$1000 R$10000 R$20000 :'))
            if withdrawl in [80, 400, 800, 1000, 10000, 20000]:
                balance = balance - withdrawl
                print('\nYour Balance is now R$', balance)
                restart = input('Would You you like to go back? ')
                if restart in ('NO', 'no'):
                    print('Okay, please continue on')

            elif withdrawl != [80, 400, 800, 1000, 10000, 20000]:
                print('Invalid Amount, Please Re-try\n')
                restart = ('yes')

        elif transaction == 3:
            deposit = float(input('How much Robux do you want to deposit?'))
            balance = balance + deposit
            print('Your Balance is $', balance, '\n')
            restart = input('Would You you like to go back? ')
            if restart in ('NO', 'no'):
                print('Thank You, enjoy the remainder of your day type start_menu() ')

        elif transaction == 4:

            print('Thanks for using Robux ATM \n')

    print("Exiting Program...")


start_menu()

