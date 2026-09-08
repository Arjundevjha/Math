# Unit tests for polynomial evaluation and formatting
import pytest
from Math.Algebra.Polynomials.polynomial import (
    evaluate_polynomial,
    format_polynomial,
)


class TestEvaluatePolynomial:
    def test_evaluate_polynomial_basic(self):
        # P(x) = 2x^2 + 3x + 1 at x=2 => 2*4 + 3*2 + 1 = 15
        assert evaluate_polynomial([2, 3, 1], [2, 1, 0], 2) == 15

    def test_evaluate_polynomial_zero_x(self):
        # P(x) = 5x^3 - 2x^2 + 4 at x=0 => 4
        assert evaluate_polynomial([5, -2, 4], [3, 2, 0], 0) == 4

    def test_evaluate_polynomial_negative_x(self):
        # P(x) = x^3 - x^2 + x - 1 at x=-2 => -8 - 4 - 2 - 1 = -15
        assert evaluate_polynomial([1, -1, 1, -1], [3, 2, 1, 0], -2) == -15

    def test_evaluate_polynomial_fractional_powers(self):
        # P(x) = x^0.5 at x=4 => 2.0
        assert evaluate_polynomial([1], [0.5], 4) == pytest.approx(2.0)

    def test_evaluate_polynomial_float_coefficients(self):
        # P(x) = 1.5x^2 + 0.5 at x=2.0 => 1.5*4 + 0.5 = 6.5
        assert evaluate_polynomial([1.5, 0.5], [2, 0], 2.0) == pytest.approx(6.5)

    def test_evaluate_polynomial_empty(self):
        assert evaluate_polynomial([], [], 5) == 0

    def test_evaluate_polynomial_negative_powers(self):
        # P(x) = 4x^-1 + 2x^-2 at x=2 => 4/2 + 2/4 = 2.5
        assert evaluate_polynomial([4, 2], [-1, -2], 2) == pytest.approx(2.5)

    def test_evaluate_polynomial_zero_division(self):
        # P(x) = x^-1 at x=0 raises ZeroDivisionError
        with pytest.raises(ZeroDivisionError):
            evaluate_polynomial([1], [-1], 0)

    def test_evaluate_polynomial_mismatched_lengths(self):
        # zip stops at shortest list: coeffs=[2, 3, 4], powers=[2, 1] => 2*x^2 + 3*x^1
        assert evaluate_polynomial([2, 3, 4], [2, 1], 2) == 14

    def test_evaluate_polynomial_multiple_terms_same_power(self):
        # 2x^2 + 3x^2 = 5x^2 at x=2 => 20
        assert evaluate_polynomial([2, 3], [2, 2], 2) == 20

    def test_evaluate_polynomial_unsorted_powers(self):
        # 3x^1 + 2x^2 + 1x^0 at x=2 => 6 + 8 + 1 = 15
        assert evaluate_polynomial([3, 2, 1], [1, 2, 0], 2) == 15

    def test_evaluate_polynomial_zero_power_zero_x(self):
        # 0^0 is 1 in Python => 5 * (0^0) = 5
        assert evaluate_polynomial([5], [0], 0) == 5

    def test_evaluate_polynomial_large_inputs(self):
        assert evaluate_polynomial([1], [10], 2) == 1024

    def test_evaluate_polynomial_all_zero_coeffs(self):
        assert evaluate_polynomial([0, 0, 0], [2, 1, 0], 5) == 0

    def test_evaluate_polynomial_precision(self):
        # 0.1x + 0.2 at x=1.0 => 0.3
        assert evaluate_polynomial([0.1, 0.2], [1, 0], 1.0) == pytest.approx(0.3)


class TestFormatPolynomial:
    def test_format_polynomial_basic(self):
        assert format_polynomial([2, 3, 4], [2, 1, 0]) == "2x^2 + 3x + 4"

    def test_format_polynomial_empty(self):
        assert format_polynomial([], []) == ""

    def test_format_polynomial_single_term(self):
        assert format_polynomial([5], [3]) == "5x^3"

    def test_format_polynomial_power_one(self):
        assert format_polynomial([3], [1]) == "3x"

    def test_format_polynomial_power_zero(self):
        assert format_polynomial([4], [0]) == "4"

    def test_format_polynomial_negative_powers(self):
        assert format_polynomial([2, -3], [-1, -2]) == "2x^-1 + -3x^-2"

    def test_format_polynomial_floats(self):
        assert (
            format_polynomial([1.5, -2.5, 3.1], [2.5, 1.0, 0.0])
            == "1.5x^2.5 + -2.5x + 3.1"
        )

    def test_format_polynomial_mismatched_lengths(self):
        # zip stops at shortest list
        assert format_polynomial([2, 3, 4], [2, 1]) == "2x^2 + 3x"
