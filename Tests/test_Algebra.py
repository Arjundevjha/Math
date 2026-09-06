import math
import pytest

from Math.Algebra.Linear_Equations.linear_eqn import linear_eqn
from Math.Algebra.Polynomials.factor_theorem import check_factor


def test_linear_eqn_positive_slope():
    # Points: (1, 2) and (3, 6)
    # m = (6 - 2) / (3 - 1) = 4 / 2 = 2.0
    # b = 2 - 2.0 * 1 = 0.0
    # Result: y = 2.0x + 0.0
    assert linear_eqn(1, 2, 3, 6) == "y = 2.0x + 0.0"


def test_linear_eqn_negative_slope():
    # Points: (0, 5) and (5, 0)
    # m = (0 - 5) / (5 - 0) = -5 / 5 = -1.0
    # b = 5 - (-1.0) * 0 = 5.0
    # Result: y = -1.0x + 5.0
    assert linear_eqn(0, 5, 5, 0) == "y = -1.0x + 5.0"


def test_linear_eqn_zero_slope():
    # Points: (1, 4) and (5, 4)
    # Horizontal line
    # m = (4 - 4) / (5 - 1) = 0.0
    # b = 4 - 0.0 * 1 = 4.0
    # Result: y = 0.0x + 4.0
    assert linear_eqn(1, 4, 5, 4) == "y = 0.0x + 4.0"


def test_linear_eqn_floats():
    # Points: (1.5, 2.5) and (3.5, 6.5)
    # m = (6.5 - 2.5) / (3.5 - 1.5) = 4.0 / 2.0 = 2.0
    # b = 2.5 - 2.0 * 1.5 = 2.5 - 3.0 = -0.5
    # Result: y = 2.0x + -0.5
    assert linear_eqn(1.5, 2.5, 3.5, 6.5) == "y = 2.0x + -0.5"


def test_linear_eqn_vertical_line():
    # Points: (2, 3) and (2, 7)
    # x1 == x2, expects ValueError
    with pytest.raises(ValueError, match=r"The x-coordinates cannot be the same \(vertical line\)\."):
        linear_eqn(2, 3, 2, 7)


def test_linear_eqn_identical_points():
    # Points: (2, 3) and (2, 3)
    # x1 == x2, expects ValueError
    with pytest.raises(ValueError, match=r"The x-coordinates cannot be the same \(vertical line\)\."):
        linear_eqn(2, 3, 2, 3)


def test_linear_eqn_origin():
    # Points: (0, 0) and (2, 4)
    # m = (4 - 0) / (2 - 0) = 2.0
    # b = 0 - 2.0 * 0 = 0.0
    assert linear_eqn(0, 0, 2, 4) == "y = 2.0x + 0.0"


def test_linear_eqn_all_negative():
    # Points: (-2, -3) and (-4, -7)
    # m = (-7 - -3) / (-4 - -2) = -4 / -2 = 2.0
    # b = -3 - 2.0 * (-2) = -3 + 4 = 1.0
    assert linear_eqn(-2, -3, -4, -7) == "y = 2.0x + 1.0"


def test_linear_eqn_fractional_slope():
    # Points: (1, 1) and (4, 2)
    # m = (2 - 1) / (4 - 1) = 1 / 3
    # b = 1 - (1/3) * 1 = 2 / 3
    # Since python uses floats, computing m and b explicitly and then doing format
    m = (2.0 - 1.0) / (4.0 - 1.0)
    b = 1.0 - m * 1.0
    assert linear_eqn(1, 1, 4, 2) == f"y = {m}x + {b}"


def test_linear_eqn_large_coordinates():
    # Points: (1000000, 2000000) and (3000000, 6000000)
    # m = 4000000 / 2000000 = 2.0
    # b = 2000000 - 2.0 * 1000000 = 0.0
    assert linear_eqn(1000000, 2000000, 3000000, 6000000) == "y = 2.0x + 0.0"


def test_check_factor_true():
    # P(x) = x^2 - 4x + 4, check if (x - 2) is a factor
    # P(2) = 2^2 - 4*2 + 4 = 4 - 8 + 4 = 0 -> True
    assert check_factor([1, -4, 4], [2, 1, 0], 2) is True


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


def test_check_factor_float():
    # P(x) = 2x^2 - x - 1
    # Factors are (2x+1)(x-1) => x = -0.5, x = 1
    coefficients = [2, -1, -1]
    powers = [2, 1, 0]
    assert check_factor(coefficients, powers, -0.5) is True
    assert check_factor(coefficients, powers, 1.0) is True
    assert check_factor(coefficients, powers, 0.5) is False


def test_check_factor_precision():
    # P(x) = x^2 - 2
    # Factor is (x - sqrt(2)) => x = sqrt(2)
    assert check_factor([1, -2], [2, 0], math.sqrt(2)) is True

    # P(x) = x^3 - 3
    # Factor is (x - cbrt(3))
    assert check_factor([1, -3], [3, 0], 3 ** (1 / 3)) is True


def test_check_factor_empty():
    # Empty polynomial evaluates to 0, so any x should technically yield 0 and therefore True
    assert check_factor([], [], 5) is True


def test_check_factor_zero_polynomial():
    # Zero polynomial P(x) = 0
    assert check_factor([0], [2], 10) is True
    # P(x) = 0.1x^2 + 0.2x - 0.3
    # P(1.0) = 0.1 + 0.2 - 0.3 = 0 (but floating point arithmetic gives 5.55e-17)
    assert check_factor([0.1, 0.2, -0.3], [2, 1, 0], 1.0) is True


def test_check_factor_zero_coefficients():
    # P(x) = 0x^2 + 0x + 0 = 0
    assert check_factor([0, 0, 0], [2, 1, 0], 100) is True


def test_check_factor_negative_powers():
    # P(x) = x^-1 - 0.5
    # P(2) = 0.5 - 0.5 = 0
    assert check_factor([1, -0.5], [-1, 0], 2) is True

    # P(x) = x^2 - 2, check if x = sqrt(2) is a factor
    # This evaluates to ~4.44e-16 instead of exactly 0 due to float precision
    assert check_factor([1, -2], [2, 0], math.sqrt(2)) is True


def test_check_factor_zero():
    # P(x) = 0x^2
    assert check_factor([0], [2], 10) is True


def test_check_factor_irrational():
    # P(x) = x^2 - 2
    # Factors are (x - sqrt(2))(x + sqrt(2))
    coefficients = [1, -2]
    powers = [2, 0]
    assert check_factor(coefficients, powers, math.sqrt(2)) is True
    assert check_factor(coefficients, powers, -math.sqrt(2)) is True


def test_check_factor_zero_value():
    # P(x) = x^2 - x
    # Factors are x(x - 1), so (x - 0) is a factor
    coefficients = [1, -1]
    powers = [2, 1]
    assert check_factor(coefficients, powers, 0) is True
    assert check_factor(coefficients, powers, 1) is True
    assert check_factor(coefficients, powers, 2) is False
