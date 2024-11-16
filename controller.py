class ATMController:
    def __init__(self, bank_api):
        self.bank_api = bank_api
        self.current_card = None
        self.current_account = None
        self.accounts = {}

    def insert_card(self, card):
        self.current_card = card

    def enter_pin(self, pin):
        if self.current_card is None:
            raise ValueError("No card inserted.")
        if not self.bank_api.validate_pin(self.current_card.card_number, pin):
            raise ValueError("Invalid PIN.")

    def select_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account does not exist.")
        self.current_account = self.accounts[account_number]

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def see_balance(self):
        if self.current_account is None:
            raise ValueError("No account selected.")
        return self.current_account.get_balance()

    def deposit(self, amount):
        if self.current_account is None:
            raise ValueError("No account selected.")
        return self.current_account.deposit(amount)

    def withdraw(self, amount):
        if self.current_account is None:
            raise ValueError("No account selected.")
        return self.current_account.withdraw(amount)