class Account:
    def __init__(self,balance,account_number,account_name,deposits,withdrawals):
        self.balance = balance
        self.account_number = account_number
        self.account_name = account_name
        self.withdrawals = withdrawals
        self.deposits = deposits

    def deposit(self):
        self.balance += self.deposits
        return(self.balance)

    
    def withdraw(self):
        self.balance -= self.withdrawals
        return(self.balance)
