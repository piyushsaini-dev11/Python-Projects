from bank_account import *

Piyush = Bankaccount(2000, "Piyush")
Nishar = Bankaccount(2500, "Nishar")

Piyush.getBalance()
Nishar.getBalance()

Piyush.deposit(5000)
Nishar.deposit(5000)

Piyush.withdraw(50)

Piyush.transfer(1000, Nishar)

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Piyush)

Bobby = SavingAcct(1000, "Bobby")

Bobby.getBalance()

Bobby.deposit(100)

Bobby.transfer(300, Piyush)