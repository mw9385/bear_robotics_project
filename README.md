# bear_robotics_project
banking_machine_project

# Simple ATM Simulator

This project is a simple ATM simulator implemented in Python. It simulates core ATM functionalities such as inserting a card, entering a PIN, selecting an account, checking balance, depositing, and withdrawing money.

The goal is to provide a simplified version of an ATM system that can be integrated with real bank APIs and cash bins in the future.

## Features
- **Card Insertion and PIN Validation**: Insert a card and validate the PIN.
- **Account Selection**: Select an account linked to the card.
- **View Balance**: Check the current account balance.
- **Deposit Money**: Deposit money into the account (fixed at $1).
- **Withdraw Money**: Withdraw money from the account.

## Installation

    ```sh
    git clone https://github.com/mw9385/bear_robotics_project.git
    ```

## File Structure

The project is split into several Python files for modularity and easier maintainability:

- **`account.py`**: Contains the `Account` class, which handles balance management, deposits, and withdrawals.
- **`bankapi.py`**: Contains the `BankAPI` class, a mock API to validate PINs and simulate bank interactions.
- **`card.py`**: Contains the `Card` class, which stores card-related information (card number and PIN).
- **`controller.py`**: Contains the `ATMController` class, which manages the ATM workflow, including card insertion, PIN verification, account selection, and transactions.
- **`main.py`**: The entry point of the project, which provides an interactive console session to simulate ATM operations.

## Usage

To run the program, execute the following command:

```sh
python main.py
