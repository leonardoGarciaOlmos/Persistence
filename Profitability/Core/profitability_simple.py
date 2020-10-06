from Profitability.exceptions.my_custom_error import MyCustomError
from Profitability.wrappers.asset import Asset

class ProfitabilitySimple:

    @staticmethod
    def calculate(asset: Asset) -> float:
        if not asset.is_initial_investment_valid():
            raise MyCustomError("investment negative not supported")

        ren_profitability: float = ((asset.return_investment_amount - asset.initial_investment_amount) / asset.initial_investment_amount) * 100.00
        return float("{:.4f}".format(ren_profitability))
