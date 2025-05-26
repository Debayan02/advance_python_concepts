class Account:
    rem_bal = 0

    def __init__(self, initial_amt):
        self.initial_amt = initial_amt

    def withdrawal(self, withdraw_amt):
        self.withdraw_amt =  withdraw_amt
        Account.rem_bal = int(Account.rem_bal) -  int(self.withdraw_amt)
        return Account.rem_bal
    
    def deposit(self, dep_amt):
        self.dep_amt = dep_amt
        Account.rem_bal = int(self.initial_amt) + int(self.dep_amt)
        return Account.rem_bal
    
    def getbal(self):
        if self.rem_bal < 0:
            print(f"{self.rem_bal} is insufficient to withdraw")
        else:
            print(f"The final balance is {self.rem_bal}")
    
    

account1 = Account("500")
rem_bal=account1.deposit("200")
rem_bal = account1.withdrawal("900")
account1.getbal()