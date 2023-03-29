class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance: {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
            
    def check_balance(self):
        print(f"Account balance for {self.name}: {self.balance}")
        

def main():
    print("Welcome to Karan's_DOPE_Bank!")
    name = input("Please enter your name: ")
    account = BankAccount(name)
    
    while True:
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = int(input("Please enter your choice (1-5): "))
        
        if choice == 1:
            name = input("Please enter your name: ")
            balance = float(input("Please enter your initial balance: "))
            account = BankAccount(name, balance)
            print(f"Account created for {account.name} with an initial balance of {account.balance}")
            
        elif choice == 2:
            amount = float(input("Please enter the amount to deposit: "))
            account.deposit(amount)
            
        elif choice == 3:
            amount = float(input("Please enter the amount to withdraw: "))
            account.withdraw(amount)
            
        elif choice == 4:
            account.check_balance()
            
        elif choice == 5:
            print("Thank you for using Karan's_DOPE_Bank!")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
