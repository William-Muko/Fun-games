
# Bank application

class BankAccount:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited into your account. New balance: {self.balance}")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

def main():
    account = BankAccount("Keff Yrne", 0, "7890")
    attempts = 0
    while attempts < 3:
        password = input("Enter password: ")
        if password == account.password:
            while True:
                print("\nPlease select the transaction would love to do")
                print("1. Deposit")
                print("2. Withdrawal")
                print("3. Check balance")
                print("4. Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)
                elif choice == 2:
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdrawal(amount)
                elif choice == 3:
                    account.check_balance()
                elif choice == 4:
                    print("Thank you using Bank XYZ")
                    break
                else:
                    print("Invalid choice. Try again.")
            break
        else:
            attempts += 1
            print(f"Incorrect password. {3 - attempts} attempts remaining.")
    if attempts == 3:
        print("Too many incorrect password attempts. Exiting...")

if __name__ == "__main__":
    main()
