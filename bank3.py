
Rule1 = print('Welcome, How Can I help You Today!')

class Bank:
    def __init__(self, name, acc_1, acc_2, acc_3, D_balance, C_balance, S_balance,total_balance):
        self.acc_holder = {
            'Name': name,
            'Acc_1': acc_1,
            'Acc_2': acc_2,
            'Acc_3': acc_3,
            'Debit_Balance': D_balance,
            'Credit_Balance': C_balance,
            'Saving_Balance': S_balance,
            'Balance': total_balance
        }

    def display_balance(self):
        total_balance = self.acc_holder['Debit_Balance'] + self.acc_holder['Credit_Balance'] + self.acc_holder['Saving_Balance']
        total_balance = self.acc_holder['Balance']
        print(f'Your Current Total Balance Is: {total_balance}')

    def debit_deposit(self, amount):
        self.acc_holder['Debit_Balance'] += amount
        print(f'Deposited {amount}. Your Current Debit Balance Is {self.acc_holder["Debit_Balance"]}')

    def credit_deposit(self, amount):
            self.acc_holder['Credit_Balance'] += amount
            print(f'You Deposited {amount}. Your Current Balance Is: {self.acc_holder['Credit_Balance']}')

    def savings_deposit(self, amount):
        self.acc_holder['Saving_Balance'] += amount
        print(f'Deposited {amount}. Your Current Savings Balance Is {self.acc_holder["Saving_Balance"]}')

    def debit_withdrawal(self, amount):
        if self.acc_holder['Debit_Balance'] >= amount:
            self.acc_holder['Debit_Balance'] -= amount
            print(f'Withdrew {amount}. Your Current Debit Balance Is {self.acc_holder["Debit_Balance"]}')
        else:
            print('You have insufficient funds to make this transaction')

    def credit_withdrawal(self, amount):
        if self.acc_holder['Credit_Balance'] >= -2000:
            self.acc_holder['Credit_Balance'] -= amount
            print(f'Withdrew {amount}. Your Current Credit Balance Is {self.acc_holder["Credit_Balance"]}')
        else:
            print('You have exceeded your credit limit')



    def savings_withdrawal(self, amount):
        if self.acc_holder['Saving_Balance'] >= amount:
            self.acc_holder['Saving_Balance'] -= amount
            print(f'Withdrew {amount}. Your Current Savings Balance Is {self.acc_holder["Saving_Balance"]}')
        else:
            print('You have insufficient funds to make this transaction')

    def acc_holder_info(self):
        for key, value in self.acc_holder.items():
            print(f'{key}: {value}')

def main_menu():
    print('\nMenu')
    print('1. Check Balance')
    print('2. Account Holder Information')
    print('3. Debit Account')
    print('4. Credit Account')
    print('5. Savings Account')
    print('6. Exit')
    choice = input('Enter Your Choice: ')
    return choice

def sub_menu(account_type):
    print(f'\n{account_type} Sub Menu')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Back to main menu')
    print('4. Exit')
    choice = input('Enter Your Choice: ')
    return choice

def main():
    bank_info = Bank('Nombulelo Khumalo', 'Debit Account', 'Credit Account', 'Savings Account', 5000, -1000, 8000, 12000)

    while True:
        main_choice = main_menu()

        if main_choice == '1':
            bank_info.display_balance()
            another_transaction = input('Do you want to perform another transaction? (yes/no) ' )
            if another_transaction.lower() != 'yes':
                print('Bye! Thank You For Banking With Us')
                break

        elif main_choice == '2':
            bank_info.acc_holder_info()
            another_transaction = input('Do you want to perform another transaction? (yes/no) ' )
            if another_transaction.lower() != 'yes':
                print('Bye! Thank You For Banking With Us')
                break

        elif main_choice == '3':
            while True:
                sub_choice = sub_menu("Debit Account")
                if sub_choice == '1':
                    amount_depositing = float(input('Enter Amount Depositing: '))
                    bank_info.debit_deposit(amount_depositing)
                elif sub_choice == '2':
                    amount_withdrawing = float(input('Enter Amount Withdrawing: '))
                    bank_info.debit_withdrawal(amount_withdrawing)
                elif sub_choice == '3':
                    break  
                elif sub_choice == '4':
                    print('Thank You For Banking With Us!! Goodbye')
                    break
                else:
                    print('Invalid choice, please try again.')
                another_transaction = input('Do you want to perform another transaction? (yes/no) ' )
                if another_transaction.lower() != 'yes':
                    print('Bye! Thank You For Banking With Us')
                    break


        elif main_choice == '4':
            while True:
                sub_choice = sub_menu("Credit Account")
                if sub_choice == '1':
                    amount_depositing = float(input('Enter Amount Depositing: '))
                    bank_info.credit_deposit(amount_depositing)
                elif sub_choice == '2':
                    amount_withdrawing = float(input('Enter Amount Withdrawing: '))
                    bank_info.credit_withdrawal(amount_withdrawing)
                elif sub_choice == '3':
                    break  
                elif sub_choice == '4':
                    print('Thank You For Banking With Us!!! Goodbye')
                    break
                else:
                    print('Invalid choice, please try again.')

                another_transaction = input('Do you want to perform another transaction? (yes/no) ' )
                if another_transaction.lower() != 'yes':
                    print('Bye! Thank You For Banking With Us')
                    break

        elif main_choice == '5':
            while True:
                sub_choice = sub_menu("Savings Account")
                if sub_choice == '1':
                    amount_depositing = float(input('Enter Amount Depositing: '))
                    bank_info.savings_deposit(amount_depositing)
                elif sub_choice == '2':
                    amount_withdrawing = float(input('Enter Amount Withdrawing: '))
                    bank_info.savings_withdrawal(amount_withdrawing)
                elif sub_choice == '3':
                    break  
                elif sub_choice == '4':
                    print('Thank You For Banking With Us')
                    break
                else:
                    print('Invalid choice, please try again.')
                another_transaction = input('Do you want to perform another transaction? (yes/no) ' )
                if another_transaction.lower() != 'yes':
                    print('Bye! Thank You For Banking With Us')
                    break

        elif main_choice == '6':
            print('Thank You For Banking With Us!!!Goodbye')
            break
        else:
            print('Invalid choice, please try again.')
            break 

if __name__ == '__main__':
    main()
