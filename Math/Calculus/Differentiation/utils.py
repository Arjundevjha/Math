# Polynomial differentiation and formatting utilities
from typing import List, Union, Tuple


def compute_polynomial_derivative_str(
    coefficients: List[Union[int, float]], powers: List[Union[int, float]]
) -> str:
    """
    Compute the derivative of a polynomial and return as string.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients.
    powers (List[Union[int, float]]): List of powers.

    Returns:
    str: String representation of the derivative.
    """
    # Apply power rule: d/dx(ax^n) = n×a×x^(n-1)
    derivative_terms = [
        f"{coeff * power}x^{int(power - 1)}"
        for coeff, power in zip(coefficients, powers)
        if power != 0
    ]

    return " + ".join(derivative_terms) if derivative_terms else "0"


def compute_polynomial_derivative(
    coefficients: List[Union[int, float]], powers: List[Union[int, float]]
) -> Tuple[List[float], List[float]]:
    """
    Compute the derivative of a polynomial.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients.
    powers (List[Union[int, float]]): List of powers.

    Returns:
    Tuple[List[float], List[float]]: Lists of derivative coefficients and powers.
    """
    derivative_coeffs = []
    derivative_powers = []

    # Apply power rule: d/dx(ax^n) = n×a×x^(n-1)
    for coeff, power in zip(coefficients, powers):
        if power == 0:
            continue
        derivative_coeffs.append(coeff * power)
        derivative_powers.append(power - 1)

    return derivative_coeffs, derivative_powers
