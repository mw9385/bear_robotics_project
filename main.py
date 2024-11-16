from controller import ATMController
from bankapi import BankAPI
from card import Card
from account import Account

if __name__ == "__main__":
    # Create BankAPI instance
    bank_api = BankAPI()

    # Create a card and register with the bank
    card = Card(card_number="1234-5678", pin="1234")
    bank_api.register_card(card)

    # Create an ATM controller
    atm = ATMController(bank_api)

    # Add an account linked to the card
    account = Account(account_number="0001", balance=1)
    atm.add_account(account)

    # Insert the card
    insert_card_input = input("Insert Card (yes/no): ").strip().lower()
    if insert_card_input == "yes":
        atm.insert_card(card)
    else:
        print("ATM session ended.")
        exit()

    # Enter PIN and validate
    pin_attempts = 3  # Allow 3 attempts for PIN
    while pin_attempts > 0:
        pin_input = input("Enter PIN: ").strip()
        try:
            atm.enter_pin(pin_input)
            print("PIN validated successfully.")
            break
        except ValueError as e:
            pin_attempts -= 1
            if pin_attempts > 0:
                print(f"Incorrect PIN. You have {pin_attempts} attempts left.")
            else:
                print("PIN validation failed. Card retained.")
                exit()

    # Select the account
    try:
        atm.select_account("0001")
        print("Account selected successfully.")
    except ValueError as e:
        print(f"Account selection failed: {e}")
        exit()

    # Check balance
    print(f"Balance: {atm.see_balance()}")

    # Deposit money (fixed to $1)
    deposit_input = input("Would you like to deposit $1? (yes/no): ").strip().lower()
    if deposit_input == "yes":
        print(f"Depositing $1. New balance: {atm.deposit(1)}")

    # Withdraw money
    withdraw_input = input("Would you like to withdraw money? (yes/no): ").strip().lower()
    if withdraw_input == "yes":
        try:
            amount = int(input("Enter the amount to withdraw: ").strip())
            print(f"Withdrawing {amount}. New balance: {atm.withdraw(amount)}")
        except ValueError as e:
            print(f"Withdrawal failed: {e}")
