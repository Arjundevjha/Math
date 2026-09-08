# Numerical integration using polynomial integration
from typing import List, Union, Tuple


def integrate_polynomial(coefficients: List[Union[int, float]], powers: List[Union[int, float]]) -> Tuple[List[float], List[float]]:
    """
    Integrate a polynomial term by term.

    Parameters:
    coefficients (List[Union[int, float]]): List of coefficients for each term.
    powers (List[Union[int, float]]): List of powers for each term.

    Returns:
    Tuple[List[float], List[float]]: Lists of integrated coefficients and powers.
    """
    n = min(len(coefficients), len(powers))
    sub_powers = powers[:n]
    if -1 in sub_powers:
        raise ValueError(
            "Integration of x^-1 results in ln|x|, which is not supported by this polynomial integration function."
        )

    # Apply integration rule: ∫(ax^n)dx = (a/(n+1))×x^(n+1) + C
    integrated_powers = [power + 1 for power in sub_powers]
    integrated_coeffs = [
        coeff / new_power for coeff, new_power in zip(coefficients[:n], integrated_powers)
    ]

    return integrated_coeffs, integrated_powers


def format_polynomial_integration(coefficients: List[float], powers: List[float]) -> str:
    """
    Format an integrated polynomial as a string.

    Parameters:
    coefficients (List[float]): List of coefficients.
    powers (List[float]): List of powers.

    Returns:
    str: String representation of the integrated polynomial.
    """
    terms = []
    for coeff, power in zip(coefficients, powers):
        if power == 0:
            terms.append(f"{coeff}")
        elif power == 1:
            terms.append(f"{coeff}x")
        else:
            terms.append(f"{coeff}x^{int(power)}")
    
    result = " + ".join(terms)
    return result + " + C"