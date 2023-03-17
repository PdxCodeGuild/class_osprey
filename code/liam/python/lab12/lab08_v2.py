#v2 - Have the ATM maintain a list of transactions. 
# Every time the user makes a deposit or withdrawal, 
# add a string to a list saying 'user deposited $15' 
# or 'user withdrew $15'. 
# Add a new method print_transactions() to your class for printing out the list of transactions, 
# and add a transactions option to your REPL loop.

class ATM: 
    def __init__(self, balance=0.00, interest=0.10, transactions = []):
        self.balance = balance
        self.interest = interest
        self.transactions = transactions
        return None

    def check_balance(self) -> float:
        self.transactions.append(f'user checked balance of ${self.balance}.')
        return self.balance

    def deposit(self, amount):
        #deposits the given amount in the account
        self.amount = amount
        self.balance += amount
        self.transactions.append(f'user deposited ${amount}.')
        return round(self.balance, 2)

    def check_withdrawal(self, amount):
        #returns true if the withdrawn amount won't put the account in the negative
        self.amount = amount
        if amount <= self.balance:
            return True
        return False

    def withdraw(self, amount):
        #withdraws the amount from the account and returns it
        self.amount = amount
        self.balance -= amount
        self.transactions.append(f'user withdrew ${amount}.')
        return self.balance

    def calc_interest(self):
        #returns the amount of interest calculated on the account
        amount = round((self.balance * self.interest), 2)
        self.transactions.append(f'user accrued ${amount} in interest.')
        return amount
    
    def print_transactions(self):
        history = '\n'.join(self.transactions)
        self.transactions.append(f'user checked transaction history.')
        return history

###End class and functions

if __name__ == '__main__':

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
        elif command == 'transactions':
            print(f'{atm.print_transactions()}')
        elif command == 'help':
            print('Available commands:')
            print('balance  - get the current balance')
            print('deposit  - deposit money')
            print('withdraw - withdraw money')
            print('interest - accumulate interest')
            print('transactions - show list of history')
            print('exit     - exit the program')
        elif command == 'exit':
            break
        else:
            print('Command not recognized')