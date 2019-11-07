import pytest
from loan_calculator.loan_calculator import LoanCalculator


class TestLoanCalculator:

    @pytest.mark.parametrize(
        "yearly_rate,expected_monthly",
        [
            (
                12,
                1,
            ),
            (
                1.2,
                0.1,
            ),
        ]
    )
    def test_monthly_interest_rate(
            self,
            yearly_rate: float,
            expected_monthly: float
    ):
        calculator = LoanCalculator(
            1,
            yearly_rate,
            1
        )
        assert calculator.monthly_interest_rate == float(expected_monthly)

    @pytest.mark.parametrize(
        "loan_amount,monthly_payment,interest_rate,deposit,expected_months",
        [
            (100, 10, 0, 10, 9),
            (100, 10, 0, 10, 9),
        ]
    )
    def test_calculate_months_to_pay(
            self,
            loan_amount: float,
            monthly_payment: float,
            interest_rate: float,
            deposit: float,
            expected_months: int,
    ):
        calculator = LoanCalculator(
            loan_amount,
            interest_rate,
            deposit
        )
        months = calculator.calculate_loan_length(monthly_payment)
        assert months == expected_months
        assert calculator.payment_months == expected_months

    @pytest.mark.parametrize(
        "loan_amount,years_to_pay,interest_rate,deposit,expected_payment",
        [
            (120, 1, 0, 0, 10),
        ]
    )
    def test_calculate_monthly_payments(
            self,
            loan_amount: float,
            years_to_pay: int,
            interest_rate: float,
            deposit: float,
            expected_payment: float,
    ):
        calculator = LoanCalculator(
            loan_amount,
            interest_rate,
            deposit
        )
        payment = calculator.calculate_monthly_payments(years_to_pay)
        assert payment == expected_payment
        assert calculator.monthly_payments == expected_payment

    @pytest.mark.parametrize(
        "loan_amount,years_to_pay,interest_rate,deposit, exception_message",
        [
            (100, 1, 0, 110,
             "You do not need a loan if the deposit matches "
             "or exceeds the purchase price"),
        ]
    )
    def test_exceptions(
            self,
            loan_amount: float,
            years_to_pay: int,
            interest_rate: float,
            deposit: float,
            exception_message: str,
    ):
        with pytest.raises(Exception):
            LoanCalculator(
                loan_amount,
                interest_rate,
                deposit
            )
