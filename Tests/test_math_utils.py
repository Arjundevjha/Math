from decimal import Decimal
import pytest

from Math.utils.math_utils import (
    PI,
    _product_tree,
    factorial,
    factorial_decimal,
    format_polynomial,
)


class TestPiConstant:
    def test_pi_value_and_type(self):
        """Test value and float type of PI constant."""
        assert PI == 3.14159265358979323846
        assert isinstance(PI, float)


class TestProductTree:
    def test_start_greater_than_end(self):
        """Test _product_tree returns 1 when start > end."""
        assert _product_tree(5, 3) == 1
        assert _product_tree(10, 2) == 1

    def test_start_equals_end(self):
        """Test _product_tree returns start when start == end."""
        assert _product_tree(5, 5) == 5
        assert _product_tree(1, 1) == 1

    def test_start_plus_one_equals_end(self):
        """Test _product_tree returns start * end when start + 1 == end."""
        assert _product_tree(4, 5) == 20
        assert _product_tree(9, 10) == 90

    def test_product_tree_recursive_range(self):
        """Test _product_tree for larger ranges requiring recursive splitting."""
        assert _product_tree(2, 6) == 2 * 3 * 4 * 5 * 6
        assert _product_tree(1, 10) == 3628800


class TestFactorial:
    def test_factorial_zero_and_one(self):
        """Test factorial of 0 and 1 returns 1."""
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_positive_integers(self):
        """Test factorial for positive integers."""
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def test_factorial_type_errors(self):
        """Test that non-integer inputs (including booleans) raise TypeError."""
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial(True)

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial(False)

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial(5.5)

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial("5")

    def test_factorial_negative_value_error(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
            factorial(-1)

        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
            factorial(-10)

    def test_factorial_exceeds_limit(self):
        """Test that input exceeding max limit raises ValueError."""
        with pytest.raises(ValueError, match="Input exceeds maximum allowed limit of 100000."):
            factorial(100001)


class TestFactorialDecimal:
    def test_factorial_decimal_zero_and_one(self):
        """Test factorial_decimal of 0 and 1 returns Decimal(1)."""
        assert factorial_decimal(0) == Decimal(1)
        assert factorial_decimal(1) == Decimal(1)

    def test_factorial_decimal_positive_integers(self):
        """Test factorial_decimal for positive integers."""
        assert factorial_decimal(5) == Decimal(120)
        assert factorial_decimal(10) == Decimal(3628800)

    def test_factorial_decimal_return_type(self):
        """Test that return value is of type Decimal."""
        res = factorial_decimal(5)
        assert isinstance(res, Decimal)

    def test_factorial_decimal_type_errors(self):
        """Test that non-integer inputs raise TypeError."""
        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal(True)

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal(False)

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal(3.14)

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal("10")

    def test_factorial_decimal_negative_value_error(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
            factorial_decimal(-1)

    def test_factorial_decimal_exceeds_limit(self):
        """Test that input exceeding max limit raises ValueError."""
        with pytest.raises(ValueError, match="Input exceeds maximum allowed limit of 100000."):
            factorial_decimal(100001)


class TestFormatPolynomial:
    def test_format_polynomial_basic(self):
        """Test format_polynomial with standard integer coefficients and powers."""
        coeffs = [3, 2, 1]
        powers = [2, 1, 0]
        assert format_polynomial(coeffs, powers) == "3x^2 + 2x^1 + 1x^0"

    def test_format_polynomial_floats(self):
        """Test format_polynomial with float coefficients."""
        coeffs = [1.5, -0.5]
        powers = [2, 0]
        assert format_polynomial(coeffs, powers) == "1.5x^2 + -0.5x^0"

    def test_format_polynomial_empty(self):
        """Test format_polynomial with empty lists."""
        assert format_polynomial([], []) == ""
