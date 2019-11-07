import pytest
from loan_calculator.loan_calculator import LoanCalculator


class Test_Loan_Calculator:
    @pytest.mark.parametrize(
        "yearly_rate,expected_monthly",
        [
            (
                12,
                1
            )
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
