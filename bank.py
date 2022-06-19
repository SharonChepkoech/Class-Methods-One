from datetime import datetime

class Account:
    def __init__(self,number,name):
        self.number = number
        self.name = name
        self.deposits= []
        self.withdrawals= []
        self.balance = 0
        self.transaction = 100
        self.date =datetime.now().strftime("%x %X")
        self.full_statement = []
        self.loan_balance = 0
    

    def deposit(self,amount):
        if amount <= 0:
            return f"Deposit amount should be more than 0"
        else:
            self.balance += amount
            self.deposit_details={}
            self.deposits.append(amount)
            self.deposit_details["date"] = self.date
            self.deposit_details["amount"] = amount
            self.deposit_details["narration"] = f"You have deposited and your balance is {self.balance}"    
            self.full_statement.append(self.deposit_details)       
            print (self.deposits)
            return self.deposit_details

    def deposits_statement(self):
         for amount in self.deposits:
             print(f"You deposited {amount}")                   
                
    def withdraw(self,amount):     
        if amount + self.transaction > self.balance:   
            return f"Your balance is {self.balance} and cannot withdraw {amount}"
        elif amount <= 0:
            return f"Your withdrawal amount cannot be 0"
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            self.withdrawals_details = {}
            self.withdrawals_details["date"] = self.date
            self.withdrawals_details["amount"] = amount
            self.withdrawals_details["narration"] = f"You have withdrawn and your balance is {self.balance}"
            self.balance -=self.transaction 
            self.full_statement.append(self.withdrawals_details)
            
            return f" You withdrew {amount} and your new balance is {self.balance}"

    def withdrawals_statement(self):
        for amount in self.withdrawals:
            print(f"You have withdrawn {amount}")
    
    def current_balance(self):
        return f"Your current balance is {self.balance}"
    def full_statementz(self):
        for full in self.full_statement:
            time = full["date"]
            narration = full["narration"]
            amount = full['amount']
            print(f"{time}..... {narration}...... {amount}")

    def borrow(self,amount):
        deposits_total = sum(self.deposits)
        deposits_times = len(self.deposits)
        requested = 1/3* deposits_total
        interest = 0.03 * amount
        if amount <= 100:
            return f"Amount requested should be more than 100"
        elif amount >= requested: 
            return f"Your loan limit is {requested}"
        elif self.loan_balance > 0:
            return f"You have a previous loan balance"
        elif deposits_times < 1:
            return f"You must have a history of atleast 10 deposits for you to qualify for a loan"  
        elif deposits_times >= 1 and requested and self.loan_balance == 0 :
            self.loan_balance += amount + interest
            self.balance += self.loan_balance - interest
            return f"You have requested {amount} with an interest of {interest} your current loan balance is {self.loan_balance}. Your new account balance is {self.balance}"
        else:
            return "None"
        

    def loan_repayment(self,amount):
        if amount <= self.loan_balance :
            self.loan_balance -= amount
            return f"You have paid {amount} and your remaing loan is {self.loan_balance}"
        else:
            extra_pay = amount - self.loan_balance    
            self.balance += extra_pay
            return f"You have paid your loan of {self.loan_balance} with an extra amount of {extra_pay} which has been deposited to your account. Your current  balance is {self.balance}"
        
    def transfer(self,amount,account_two):
        if amount > self.balance:
            return f"You do bnot have sufficient moeney to transfer {amount}"
        elif amount <= 0:
            return f"Please enter a correct amount"
            
        else:
            self.balance -= amount
            account_two.balance += amount
            return f"You have transfered {amount} to {account_two.name} your new balance is {self.balance}"

    
   