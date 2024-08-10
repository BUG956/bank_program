class Account:
    def __init__(self, owner, balance=0):
        """
        This method initializes the account with the owner's name and an optional starting balance.
        
        Parameters:
        owner (str): The name of the account owner.
        balance (float): The initial balance of the account. Default is 0.
        
        Explanation:
        When you create a new account, you need to provide the owner's name. You can also provide an initial balance, 
        but if you don't, it will start at $0. This method sets up the account with these details.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """
        This method adds a specified amount to the account balance.
        
        Parameters:
        amount (float): The amount to be deposited.
        
        Returns:
        str: A message indicating the deposit amount and the new balance.
        
        Explanation:
        When you want to add money to your account, you use this method. You tell it how much money you want to deposit, 
        and it adds that amount to your current balance. It then returns a message telling you how much was deposited 
        and what your new balance is.
        """
        self.balance += amount
        return f"${amount} deposited. New balance: ${self.balance}"

    def withdraw(self, amount):
        """
        This method subtracts a specified amount from the account balance if there are enough funds.
        
        Parameters:
        amount (float): The amount to be withdrawn.
        
        Returns:
        str: A message indicating the withdrawal amount and the new balance, or an error message if there are not enough funds.
        
        Explanation:
        When you want to take money out of your account, you use this method. You tell it how much money you want to withdraw. 
        If you have enough money in your account, it subtracts that amount from your balance and returns a message telling you 
        how much was withdrawn and what your new balance is. If you don't have enough money, it returns an error message 
        saying "Insufficient funds".
        """
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"${amount} withdrawn. New balance: ${self.balance}"

    def check_balance(self):
        """
        This method returns the current balance of the account.
        
        Returns:
        str: A message indicating the current balance.
        
        Explanation:
        When you want to know how much money you have in your account, you use this method. It returns a message telling you 
        your current balance.
        """
        return f"Current balance: ${self.balance}"

def main():
    """
    This is the main function that runs the bank program. It provides a text-based menu for user interaction.
    
    Explanation:
    This function is the heart of the program. It starts by greeting the user and asking for their name to create a new account. 
    It then shows a menu with options to deposit money, withdraw money, check the balance, or exit the program. The user can 
    choose an option by entering the corresponding number. The program will keep running until the user chooses to exit.
    """
    print("Welcome to the Bank!")
    owner = input("Enter your name: ")
    account = Account(owner)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == '3':
            print(account.check_balance())
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
