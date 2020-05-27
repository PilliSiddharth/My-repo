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
            restart =
