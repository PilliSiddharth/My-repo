from time import sleep

def password():
    tries = 3
    while tries >= 0:
        pin = int(input("Please enter your pin in the screen"))
        if pin == (9180):
            print("Correct..fetching you data in few seconds...")
            return True
        else:
            print('Incorrect password please try again.')
            tries = tries + 1
    print("Incorrect password and system is self-destryoing for attempts in 3 seconds...")
    sleep(3)
    return False


def start():
    balance = 1000

    print("Hello, and welcome to your ROBUX ATM")
    if password():
        print('1: for Balance')
        print('2: for Withdrawl')
        print('3: for Deposit')
        print('4 for Exit')

        transaction = int(input("Choose which robux transaction fits your day: "))
        if transaction == 1:
            print('Your Balance is R$',balance,'\n')
            restart = input("Would you like to go back? ")
            if restart in('NO','no'):
                print('Thanks for using robux ATM..BYe!')

        elif transaction == 2:
            withdrawl = float(input("How much would you like to withdraw?\nR$80\nR$400\nR$80\nR$1000\nR$10000\nR$20000"))
            if withdrawl in [80,400,1000,10000,20000]:
                balance = balance - withdrawl
                print("Your balance is: ", balance)
                restart = input("Would you like to go back? ")
                if restart in ('NO', 'no'):
                    print('Thanks for using robux ATM..BYe!')
            elif withdrawl != [80,400,1000,10000,20000]:
                print("Invalid Amount, try again.")
                restart = ('yes')


        elif transaction == 3:
            deposit = float(input("How much robux do you want to deposit?"))
            balance = deposit + balance
            print("Your balance is R$: ",balance,'\n')
            restart = input("Would you like to go back? ")
            if restart in ('NO', 'no'):
                print('Thanks for using robux ATM..BYe!')

        elif transaction == 4:
            print("Thanks for using ROBUX ATM, hope you have a great day for you ahead.")
            print("Exiting prgoram....")



start()
