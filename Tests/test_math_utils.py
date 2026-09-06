from decimal import Decimal
import pytest

from Math.utils.math_utils import (
    PI,
    _product_tree,
    factorial,
    factorial_decimal,
    format_polynomial,
)


def test_pi_constant():
    assert PI == 3.14159265358979323846


class TestFactorialDecimal:
    def test_factorial_decimal_zero(self):
        result = factorial_decimal(0)
        assert isinstance(result, Decimal)
        assert result == Decimal(1)

    def test_factorial_decimal_one(self):
        result = factorial_decimal(1)
        assert isinstance(result, Decimal)
        assert result == Decimal(1)

    def test_factorial_decimal_positive(self):
        assert factorial_decimal(5) == Decimal(120)
        assert factorial_decimal(10) == Decimal(3628800)

    def test_factorial_decimal_large(self):
        assert factorial_decimal(20) == Decimal(2432902008176640000)
        assert factorial_decimal(25) == Decimal(15511210043330985984000000)

    def test_factorial_decimal_matches_factorial(self):
        for n in [0, 1, 5, 10, 20]:
            assert factorial_decimal(n) == Decimal(factorial(n))

    def test_factorial_decimal_negative(self):
        with pytest.raises(
            ValueError, match="Factorial is not defined for negative numbers."
        ):
            factorial_decimal(-1)

    def test_factorial_decimal_exceeds_upper_bound(self):
        with pytest.raises(
            ValueError, match="Input exceeds maximum allowed limit of 100000."
        ):
            factorial_decimal(100001)

    def test_factorial_decimal_invalid_types(self):
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal(True)
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal(5.5)
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal("10")
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal(None)


class TestFactorial:
    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def test_factorial_negative(self):
        with pytest.raises(
            ValueError, match="Factorial is not defined for negative numbers."
        ):
            factorial(-1)

    def test_factorial_large(self):
        assert factorial(20) == 2432902008176640000
        assert factorial(25) == 15511210043330985984000000

    def test_factorial_exceeds_upper_bound(self):
        with pytest.raises(
            ValueError, match="Input exceeds maximum allowed limit of 100000."
        ):
            factorial(100001)

    def test_factorial_invalid_types(self):
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial(True)
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial(5.5)
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial("10")
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial(None)


class TestProductTree:
    def test_product_tree_start_greater_than_end(self):
        assert _product_tree(5, 3) == 1

    def test_product_tree_start_equal_end(self):
        assert _product_tree(7, 7) == 7

    def test_product_tree_start_plus_one_equal_end(self):
        assert _product_tree(3, 4) == 12

    def test_product_tree_range(self):
        assert _product_tree(1, 5) == 120
        assert _product_tree(2, 6) == 720


class TestFormatPolynomial:
    def test_format_polynomial_basic(self):
        coeffs = [3, -2, 1]
        powers = [2, 1, 0]
        assert format_polynomial(coeffs, powers) == "3x^2 + -2x^1 + 1x^0"

    def test_format_polynomial_float_powers(self):
        coeffs = [4, 5]
        powers = [3.0, 0.0]
        assert format_polynomial(coeffs, powers) == "4x^3 + 5x^0"
