class LoanCalculator:
    __slots__ = [
        '_price',
        '_deposit',
        '_interest_rate',
        '_payment_period',
        '_monthly_payments'
    ]

    def __init__(
            self,
            price: float,
            interest_rate: float,
            deposit: float = 0,
    ):
        if deposit > price:
            raise Exception(
                "You do not need a loan if the deposit matches or exceeds the "
                "purchase price"
            )
        self._price = price
        self._deposit = deposit
        self._interest_rate = interest_rate
        self._payment_period = None
        self._monthly_payments = 0.0

    @property
    def payment_months(self) -> int:
        return self._payment_period

    @property
    def monthly_payments(self) -> int:
        return round(self._monthly_payments, 2)

    @property
    def loan_amount(self) -> float:
        return self._price - self._deposit

    def calculate_monthly_payments(self, payment_years: int):
        self._payment_period = payment_years * 12
        borrowed = self._price - self._deposit
        r = pow(1 + self.monthly_interest_rate, self._payment_period)
        upper = self.monthly_interest_rate * r
        lower = r - 1
        if lower == 0:
            self._monthly_payments = borrowed / self._payment_period
        else:
            div = upper / lower
            self._monthly_payments = borrowed * div
        return self.monthly_payments

    @property
    def monthly_interest_rate(self):
        return round(self._interest_rate / 12, 5)

    def calculate_loan_length(self, monthly_payments: float):
        self._monthly_payments = monthly_payments
        self._payment_period = 0
        current_balance = self.loan_amount
        while current_balance > 0:
            self._payment_period = self._payment_period + 1
            # Last payment may cause negative balance, doesn't impact outcome
            current_balance = current_balance - self._monthly_payments
            interest = round(current_balance * self.monthly_interest_rate, 2)
            current_balance = current_balance + interest
        return self._payment_period
