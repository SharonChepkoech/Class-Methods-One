class Account:
    def __init__(self,number,name):
        self.number = number
        self.name = name
        self.deposits= []
        self.withdrawals= []
        self.balance = 0
        

    def deposit(self,amount):
        self.balance+=amount
        if amount <= 0:

            return f"Deposit amount should be more than 0"
        else:
                self.balance += amount
                self.deposits.append(amount)
                print (self.deposits)
                return f"You have deposited {amount} and your balance is {self.balance}"  

    def deposits_statement(self):
         for amount in self.deposits:
             print(f"You have deposited {amount}")                   
                
 
    def withdraw(self,amount):
        if amount > self.balance:
            return f"Your balance is {self.balance} and cannot withdraw {amount}"
        elif amount <= 0:
            return f"Your balance must be greater than 0"
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            return f" You have withdrawn {amount} and your new balance is {self.balance}"

    def withdrawals_statement(self):
        for amount in self.deposits:
            print(f"You have withdrawn {amount}")


   

# Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which prints each deposit in a new line
# Add a new method called withdrawals_statement which prints each withdrawal in a new line
   
