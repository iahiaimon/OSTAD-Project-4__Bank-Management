class Bank:

    def __init__(self , name , balance ):
        self.name = name 
        self.balance = balance
    

    def deposite(self , amount):
        if amount>0:
            self.balance += amount
        return amount
    
    def show_balance(self):
        return self.balance
    
    def withdraw(self , amount):
        if amount < self.balance:
            self.balance -= amount
            return amount

        else:
            print("Insuffient Balance")
            



bank = Bank("Comrad3" , 20000)

print(f"Your account name is : {bank.name}")
print(f"Your account balance is : {bank.balance}")

print(f"Your deposite amount is : {bank.deposite(2000)}")
print(f"After deposite your current balance is : {bank.show_balance()}")
print(f"Your withdraw amount is : {bank.withdraw(5000)}")
print(f"After withdraw your current balance is : {bank.show_balance()}")
