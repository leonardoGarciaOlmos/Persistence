class Asset:

    initial_investment_amount: float
    return_investment_amount: float

    def __init__(self, initial_investment_amount: float = 0.0, return_investment_amount: float = 0.0):
        self.initial_investment_amount = initial_investment_amount
        self.return_investment_amount = return_investment_amount

    def is_initial_investment_valid(self) -> bool:
        return bool(self.initial_investment_amount > 0)