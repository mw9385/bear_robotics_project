class BankAPI:
    """Mocked Bank API to validate PIN."""
    def __init__(self):
        # Dictionary to store cards and PINs
        self.cards = {}

    def register_card(self, card):
        self.cards[card.card_number] = card.pin

    def validate_pin(self, card_number, pin):
        """Check if the provided PIN matches the stored PIN."""
        return self.cards.get(card_number) == pin