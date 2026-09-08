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

    def test_pi_usage_in_calculations(self):
        """Test PI in standard mathematical formulas (area and circumference)."""
        radius = 5.0
        circumference = 2 * PI * radius
        area = PI * (radius ** 2)
        assert abs(circumference - 31.41592653589793) < 1e-12
        assert abs(area - 78.53981633974483) < 1e-12


class TestProductTree:
    def test_start_greater_than_end(self):
        """Test _product_tree returns 1 when start > end."""
        assert _product_tree(5, 3) == 1
        assert _product_tree(10, 2) == 1

    def test_start_equals_end(self):
        """Test _product_tree returns start when start == end."""
        assert _product_tree(5, 5) == 5
        assert _product_tree(1, 1) == 1
        assert _product_tree(-3, -3) == -3

    def test_start_plus_one_equals_end(self):
        """Test _product_tree returns start * end when start + 1 == end."""
        assert _product_tree(4, 5) == 20
        assert _product_tree(9, 10) == 90
        assert _product_tree(-3, -2) == 6

    def test_product_tree_recursive_range(self):
        """Test _product_tree for larger ranges requiring recursive splitting."""
        assert _product_tree(2, 6) == 2 * 3 * 4 * 5 * 6
        assert _product_tree(1, 10) == 3628800

    def test_product_tree_negative_ranges(self):
        """Test _product_tree with negative integer ranges."""
        assert _product_tree(-5, -1) == (-5) * (-4) * (-3) * (-2) * (-1)
        assert _product_tree(-4, -1) == 24

    def test_product_tree_range_including_zero(self):
        """Test _product_tree when zero is included in the range."""
        assert _product_tree(-3, 3) == 0
        assert _product_tree(0, 5) == 0


class TestFactorial:
    def test_factorial_zero_and_one(self):
        """Test factorial of 0 and 1 returns 1."""
        assert factorial(0) == 1
        assert factorial(1) == 1

    def test_factorial_positive_integers(self):
        """Test factorial for positive integers."""
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def test_factorial_recurrence_relation(self):
        """Test recurrence relation n! = n * (n-1)! for positive integers."""
        for n in range(2, 15):
            assert factorial(n) == n * factorial(n - 1)

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

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial(None)

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial([5])

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial({"n": 5})

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
        assert factorial_decimal(2) == Decimal(2)
        assert factorial_decimal(5) == Decimal(120)
        assert factorial_decimal(10) == Decimal(3628800)

    def test_factorial_decimal_matches_integer_factorial(self):
        """Test that factorial_decimal(n) equals Decimal(factorial(n))."""
        for n in range(0, 15):
            assert factorial_decimal(n) == Decimal(factorial(n))

    def test_factorial_decimal_recurrence_relation(self):
        """Test recurrence relation for Decimal factorials."""
        for n in range(2, 10):
            assert factorial_decimal(n) == Decimal(n) * factorial_decimal(n - 1)

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

        with pytest.raises(TypeError, match="Input must be an integer."):
            factorial_decimal(None)

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

    def test_format_polynomial_single_term(self):
        """Test format_polynomial with a single term."""
        assert format_polynomial([5], [3]) == "5x^3"

    def test_format_polynomial_floats(self):
        """Test format_polynomial with float coefficients."""
        coeffs = [1.5, -0.5]
        powers = [2, 0]
        assert format_polynomial(coeffs, powers) == "1.5x^2 + -0.5x^0"

    def test_format_polynomial_negative_coefficients_and_powers(self):
        """Test format_polynomial with negative coefficients and negative powers."""
        coeffs = [-2, 4]
        powers = [-1, -3]
        assert format_polynomial(coeffs, powers) == "-2x^-1 + 4x^-3"

    def test_format_polynomial_zero_values(self):
        """Test format_polynomial with zero coefficients and powers."""
        assert format_polynomial([0, 1], [2, 0]) == "0x^2 + 1x^0"

    def test_format_polynomial_mismatched_lengths(self):
        """Test format_polynomial when coefficients and powers have different lengths."""
        # zip truncates to shortest input length
        coeffs = [3, 2, 1]
        powers = [2, 1]
        assert format_polynomial(coeffs, powers) == "3x^2 + 2x^1"

    def test_format_polynomial_empty(self):
        """Test format_polynomial with empty lists."""
        assert format_polynomial([], []) == ""
