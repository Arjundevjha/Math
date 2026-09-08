# Taylor series approximations for trigonometric functions
from typing import Union


def sine_taylor(radians: Union[int, float], terms: int = 50) -> float:
    """
    Calculate sine using Taylor series expansion iteratively.

    Parameters:
    radians (Union[int, float]): The angle in radians.
    terms (int): Number of terms to use in the series. Default is 50.

    Returns:
    float: The sine of the angle.
    """
    # Security: Validate terms parameter to prevent Denial of Service (DoS) via resource exhaustion or invalid types
    if not isinstance(terms, int) or isinstance(terms, bool) or terms < 1 or terms > 10000:
        raise ValueError("terms must be an integer between 1 and 10000.")

    sine_value = float(radians)
    term = float(radians)
    radians_sq = float(radians * radians)

    for idx in range(3, terms * 2, 2):
        term *= -radians_sq / ((idx - 1) * idx)
        sine_value += term

    return sine_value


def cosine_taylor(radians: Union[int, float], terms: int = 50) -> float:
    """
    Calculate cosine using Taylor series expansion iteratively.

    Parameters:
    radians (Union[int, float]): The angle in radians.
    terms (int): Number of terms to use in the series. Default is 50.

    Returns:
    float: The cosine of the angle.
    """
    # Security: Validate terms parameter to prevent Denial of Service (DoS) via resource exhaustion or invalid types
    if not isinstance(terms, int) or isinstance(terms, bool) or terms < 1 or terms > 10000:
        raise ValueError("terms must be an integer between 1 and 10000.")

    cos_value = 1.0
    term = 1.0
    radians_sq = float(radians * radians)

    for idx in range(2, terms * 2, 2):
        term *= -radians_sq / (idx * (idx - 1))
        cos_value += term

    return cos_value
