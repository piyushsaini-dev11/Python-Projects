class BalanceException(Exception):
    pass

class Bankaccount:
    def __init__(self, initialbalance, acctname):
        self.balance = initialbalance
        self.name = acctname
        print(f"\n Account Name: '{self.name}' created. \n Account Balance: ${self.balance:.2f} ")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' \nBalance: ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n Deposit complete.")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n Sorry, account '{self.name}' only has balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}") 
            
    def transfer(self, amount, account):
        try:
            print(f"\n**********\n\nBeginning Transfer..😉")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer Complete!✅\n\n*********")
        except BalanceException as error:
            print(f"\nTranfer Interrupted!❌  {error}")
            
class InterestRewardsAcct(Bankaccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\nDeposit complete.")
        self.getBalance()
        
class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialbalance, acctname):
        super().__init__(initialbalance, acctname)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")