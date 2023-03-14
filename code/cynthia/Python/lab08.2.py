#Lab 8.2 ATM

class ATM:


    def __init__(self, balance = 0) -> None:
        self.balance = balance
        self.interest_rate = .1
        self.list_transactions = []

    def check_balance(self): #returns the account balance
        return self.balance

    def deposit(self, amount): #deposits the given amount in the account
        self.balance = amount + self.balance 
        self.list_transactions.append(f'user deposited {amount}')
        return self.balance

    def check_withdrawal(self, amount): #returns true if the withdrawn amount wont put the account in the nevative
        if self.balance - amount >= 0:
            return True

    def withdraw(self, amount): #withdraws the amount from the account and returns it
        self.balance = self.balance - amount
        self.list_transactions.append(f'user withdrew {amount}')


    def calc_interest(self): #returns the amount of interest calculated on the account
        amount = self.balance * self.interest_rate
        return amount 
    
    def print_transactions(self): #returns the list of transactions
        print(self.list_transactions)
        return self.list_transactions


atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command =='transactions': #returns the list of transactions
        transactions = atm.print_transactions()
        print(f'User transactions {transactions}')

    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - see all transactions')
        print('exit     - exit the program')   
    elif command == 'exit':
        break
    else:
        print('Command not recognized') 


