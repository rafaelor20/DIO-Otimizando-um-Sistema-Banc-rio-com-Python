from datetime import datetime
import textwrap

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append({"type": "Deposit", "amount": amount, "timestamp": datetime.now()})
            print(f'Deposit of ${amount:.2f} successful.')
        else:
            print('The deposit amount must be positive.')

    def withdraw(self, amount):
        if amount > 0 and amount <= 500 and len(self.transactions) < 3:
            if self.balance >= amount:
                self.balance -= amount
                self.transactions.append({"type": "Withdrawal", "amount": amount, "timestamp": datetime.now()})
                print(f'Withdrawal of ${amount:.2f} successful.')
            else:
                print('Insufficient balance to make the withdrawal.')
        else:
            if len(self.transactions) >= 3:
                print('Daily withdrawal limit reached. Unable to withdraw more today.')
            elif amount > 500:
                print('The maximum withdrawal limit per transaction is $500.00.')
            else:
                print('The withdrawal amount must be positive.')

    def statement(self):
        print('Transaction History:')
        if not self.transactions:
            print('No transactions have been made.')
        else:
            for transaction in self.transactions:
                print(f"{transaction['type']}: ${transaction['amount']:.2f} at {transaction['timestamp']}")
        print(f'Current balance: ${self.balance:.2f}')


class Client:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account


class Account:
    account_number_counter = 1

    def __init__(self):
        self.account_number = Account.account_number_counter
        Account.account_number_counter += 1
        self.bank_account = BankAccount()

    def deposit(self, amount):
        self.bank_account.deposit(amount)

    def withdraw(self, amount):
        self.bank_account.withdraw(amount)

    def statement(self):
        self.bank_account.statement()

def select_account(client):
    account_number = int(input("Enter the account number: "))
    account = client.accounts.get(account_number)
    if account:
        return account
    else:
        print("Account not found.")
        return None

def list_clients(clients):
    print("\n=== List of Clients ===")
    for client_name, client in clients.items():
        print(f"\nName: {client_name}")
        print(f"Address: {client.address}")
        print("Accounts:")
        for account_number, account in client.accounts.items():
            print(f"Account Number: {account_number}")
            account.statement()
        print("=" * 30)

def menu():
    menu = """\n
    ================ MENU ================
    [c]\tCreate Client
    [a]\tAdd Account
    [d]\tDeposit
    [w]\tWithdraw
    [s]\tStatement
    [q]\tExit
    => """
    return input(textwrap.dedent(menu))


def create_client():
    name = input("Enter client's name: ")
    address = input("Enter client's address: ")
    return Client(name, address)


def main():
    clients = {}

    while True:
        print('\n=== Available Operations ===')
        print('1. Create Client')
        print('2. Add Account')
        print('3. Deposit')
        print('4. Withdraw')
        print('5. Statement')
        print('6. List Clients')
        print('7. Exit')

        option = input('Enter the number of the desired operation: ')

        if option == '1':
            client = create_client()
            clients[client.name] = client
            print("\n=== Client created successfully! ===")

        elif option == '2':
            client_name = input("Enter client's name: ")
            client = clients.get(client_name)
            if client:
                account = Account()
                client.add_account(account)
                print(f"\n=== Account {account.account_number} created for {client.name} ===")

        elif option == '3':
            client_name = input("Enter client's name: ")
            client = clients.get(client_name)
            if client:
                account = select_account(client)
                if account:
                    deposit_amount = float(input('Enter the deposit amount: ').replace(',', '.'))
                    account.deposit(deposit_amount)

        elif option == '4':
            client_name = input("Enter client's name: ")
            client = clients.get(client_name)
            if client:
                account = select_account(client)
                if account:
                    withdrawal_amount = float(input('Enter the withdrawal amount: ').replace(',', '.'))
                    account.withdraw(withdrawal_amount)

        elif option == '5':
            client_name = input("Enter client's name: ")
            client = clients.get(client_name)
            if client:
                account = select_account(client)
                if account:
                    account.statement()

        elif option == '6':
            list_clients(clients)

        elif option == '7':
            print('Exiting the program...')
            break

        else:
            print('Invalid option. Please try again.')


if __name__ == "__main__":
    main()
