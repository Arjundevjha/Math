import math
from Math.Algebra.Polynomials.factor_theorem import check_factor


class TestCheckFactor:
    def test_check_factor_true(self):
        # P(x) = x^2 - 4x + 4, check if (x - 2) is a factor
        # P(2) = 2^2 - 4*2 + 4 = 4 - 8 + 4 = 0 -> True
        assert check_factor([1, -4, 4], [2, 1, 0], 2) is True

    def test_check_factor_false(self):
        # P(x) = x^2 - 4x + 4, check if (x - 3) is a factor
        # P(3) = 3^2 - 4*3 + 4 = 9 - 12 + 4 = 1 -> False
        assert check_factor([1, -4, 4], [2, 1, 0], 3) is False

    def test_check_factor_linear(self):
        # P(x) = 2x - 6, check if (x - 3) is a factor
        # P(3) = 2*3 - 6 = 0 -> True
        assert check_factor([2, -6], [1, 0], 3) is True

    def test_check_factor_linear_false(self):
        # P(x) = 2x - 6, check if (x - 2) is a factor
        # P(2) = 2*2 - 6 = -2 -> False
        assert check_factor([2, -6], [1, 0], 2) is False

    def test_check_factor_cubic(self):
        # P(x) = x^3 - 6x^2 + 11x - 6
        # Factors are (x-1)(x-2)(x-3)
        coefficients = [1, -6, 11, -6]
        powers = [3, 2, 1, 0]
        assert check_factor(coefficients, powers, 1) is True
        assert check_factor(coefficients, powers, 2) is True
        assert check_factor(coefficients, powers, 3) is True
        assert check_factor(coefficients, powers, 4) is False

    def test_check_factor_float(self):
        # P(x) = 2x^2 - x - 1
        # Factors are (2x+1)(x-1) => x = -0.5, x = 1
        coefficients = [2, -1, -1]
        powers = [2, 1, 0]
        assert check_factor(coefficients, powers, -0.5) is True
        assert check_factor(coefficients, powers, 1.0) is True
        assert check_factor(coefficients, powers, 0.5) is False

    def test_check_factor_floating_point_imprecision(self):
        # A case that mathematically equals 0, but due to floating point math might not be exactly 0
        # For example, x^3 - x^2 = 0 where x = 1/3
        # Let's use P(x) = 3x - 1, x = 1/3
        assert check_factor([3, -1], [1, 0], 1 / 3) is True

    def test_check_factor_empty(self):
        # Empty polynomial evaluates to 0
        assert check_factor([], [], 5) is True

    def test_check_factor_all_zeros(self):
        # Polynomial 0x^2 + 0x + 0
        assert check_factor([0, 0, 0], [2, 1, 0], 100) is True

    def test_check_factor_gaps_in_powers(self):
        # P(x) = x^4 - 16
        # Factors are x=2, x=-2
        assert check_factor([1, -16], [4, 0], 2) is True
        assert check_factor([1, -16], [4, 0], -2) is True
        assert check_factor([1, -16], [4, 0], 1) is False


def test_check_factor_true():
    assert check_factor([1, -4, 4], [2, 1, 0], 2) is True


def test_check_factor_false():
    assert check_factor([1, -4, 4], [2, 1, 0], 3) is False


def test_check_factor_linear():
    assert check_factor([2, -6], [1, 0], 3) is True


def test_check_factor_linear_false():
    assert check_factor([2, -6], [1, 0], 2) is False


def test_check_factor_cubic():
    coefficients = [1, -6, 11, -6]
    powers = [3, 2, 1, 0]
    assert check_factor(coefficients, powers, 1) is True
    assert check_factor(coefficients, powers, 2) is True
    assert check_factor(coefficients, powers, 3) is True
    assert check_factor(coefficients, powers, 4) is False


def test_check_factor_float():
    coefficients = [2, -1, -1]
    powers = [2, 1, 0]
    assert check_factor(coefficients, powers, -0.5) is True
    assert check_factor(coefficients, powers, 1.0) is True
    assert check_factor(coefficients, powers, 0.5) is False
