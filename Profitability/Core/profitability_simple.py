from Profitability.exceptions.my_custom_error import MyCustomError


class ProfitabilitySimple:

    @staticmethod
    def calculate_profitability_simple(initial_value: float, return_value: float) -> float:
        if initial_value < 0:
            raise MyCustomError("investment negative not supported")

        ren_profitability: float = ((return_value - initial_value) / initial_value) * 100.00
        return float("{:.4f}".format(ren_profitability))
