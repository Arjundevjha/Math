import math
import pytest
from Math.Algebra.Polynomials.polynomial import evaluate_polynomial, format_polynomial


# Tests for evaluate_polynomial
def test_evaluate_polynomial_basic():
    # P(x) = x^2 + 2x + 1 at x=2 -> 2^2 + 2(2) + 1 = 9
    assert math.isclose(evaluate_polynomial([1, 2, 1], [2, 1, 0], 2), 9.0)


def test_evaluate_polynomial_zero_x():
    # P(x) = 5x^3 - 2x^2 + 4 at x=0 -> 4
    assert evaluate_polynomial([5, -2, 4], [3, 2, 0], 0) == 4


def test_evaluate_polynomial_negative_x():
    # P(x) = x^3 - x^2 + x - 1 at x=-2 -> -8 - 4 - 2 - 1 = -15
    assert evaluate_polynomial([1, -1, 1, -1], [3, 2, 1, 0], -2) == -15


def test_evaluate_polynomial_float_coefficients():
    # P(x) = 1.5x^2 + 2.5x at x=2.0 -> 1.5(4) + 2.5(2) = 11.0
    assert math.isclose(evaluate_polynomial([1.5, 2.5], [2, 1], 2.0), 11.0)


def test_evaluate_polynomial_fractional_powers():
    # P(x) = 1*x^0.5 at x=4 -> 2.0
    assert math.isclose(evaluate_polynomial([1], [0.5], 4), 2.0)


def test_evaluate_polynomial_negative_powers():
    # P(x) = 4*x^-1 + 2*x^-2 at x=2 -> 4/2 + 2/4 = 2.5
    assert math.isclose(evaluate_polynomial([4, 2], [-1, -2], 2), 2.5)


def test_evaluate_polynomial_zero_power_zero_x():
    # P(x) = 5*x^0 at x=0 -> 5*(0^0) = 5
    assert evaluate_polynomial([5], [0], 0) == 5


def test_evaluate_polynomial_empty():
    assert evaluate_polynomial([], [], 5) == 0


def test_evaluate_polynomial_mismatched_lengths():
    # Zip stops at the shortest list
    # [2, 3, 4], [2, 1] -> 2*x^2 + 3*x^1 at x=2 -> 2(4) + 3(2) = 14
    assert evaluate_polynomial([2, 3, 4], [2, 1], 2) == 14
    assert evaluate_polynomial([2, 3], [2, 1, 0], 2) == 14


def test_evaluate_polynomial_all_zero_coefficients():
    assert evaluate_polynomial([0, 0, 0], [2, 1, 0], 5) == 0


def test_evaluate_polynomial_zero_division():
    # Negative power at x=0 should raise ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        evaluate_polynomial([1], [-1], 0)


def test_evaluate_polynomial_large_powers_and_inputs():
    # 1*x^10 at x=2 -> 1024
    assert evaluate_polynomial([1], [10], 2) == 1024


def test_evaluate_polynomial_multiple_terms_same_power():
    # 2x^2 + 3x^2 = 5x^2 at x=2 -> 20
    assert math.isclose(evaluate_polynomial([2, 3], [2, 2], 2), 20.0)


def test_evaluate_polynomial_unsorted_powers():
    # 3x^1 + 2x^2 + 1x^0 at x=2 -> 6 + 8 + 1 = 15
    assert math.isclose(evaluate_polynomial([3, 2, 1], [1, 2, 0], 2), 15.0)


def test_evaluate_polynomial_precision():
    # 0.1x + 0.2 at x=1.0 -> 0.3
    assert math.isclose(evaluate_polynomial([0.1, 0.2], [1, 0], 1.0), 0.3)


# Tests for format_polynomial
def test_format_polynomial_basic():
    assert format_polynomial([2, 3, 4], [2, 1, 0]) == "2x^2 + 3x + 4"


def test_format_polynomial_negative_and_zero():
    assert format_polynomial([-1, 0], [3, 2]) == "-1x^3 + 0x^2"


def test_format_polynomial_empty():
    assert format_polynomial([], []) == ""


def test_format_polynomial_floats():
    assert format_polynomial([1.5, -2.5, 3.1], [2.5, 1.0, 0.0]) == "1.5x^2.5 + -2.5x + 3.1"


def test_format_polynomial_single_term():
    assert format_polynomial([5], [3]) == "5x^3"


def test_format_polynomial_negative_powers():
    assert format_polynomial([2, -3], [-1, -2]) == "2x^-1 + -3x^-2"


def test_format_polynomial_all_zero_powers():
    assert format_polynomial([1, 2], [0, 0]) == "1 + 2"


def test_format_polynomial_all_ones_powers():
    assert format_polynomial([3, 4], [1, 1]) == "3x + 4x"


def test_format_polynomial_mismatched_lengths():
    # zip stops at shortest list
    assert format_polynomial([1, 2, 3], [2, 1]) == "1x^2 + 2x"
