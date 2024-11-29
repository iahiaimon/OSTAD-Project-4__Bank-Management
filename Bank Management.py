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
    
    def account_inquiry(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Current Balance: {self.balance}\n")

def main():

    name = "Comrad3"
    acc_no = "00127310"
    balance = 20000

    account = Bank(name , balance)

    print("Making a Bank System Using Python\n")
    
    while True:

        print("1: Account Inquiry")
        print("2: Diposite")
        print("3: Withdraw")
        print("0: Exit")

        choice = int(input("Select your option : "))

        if 0<= choice <=3 :
            if choice == 1 :
                account.account_inquiry()
            elif choice == 2 :
                amount = int(input("Enter the amount that you want to deposite : "))
                account.deposite(amount)
                print(f"After deposite your balance is {account.show_balance()} ")

            elif choice == 3 : 
                amount = int(input("Enter the amount that you want to withdraw : "))
                account.withdraw(amount)
                print(f"After withdraw your balance is {account.show_balance()} ")

            elif choice == 0 :
                break

            else:
                print("Invalid input... ")

        else:
            print("Your choise is not in option\nSelect again \n")

if __name__ == "__main__":
    main()