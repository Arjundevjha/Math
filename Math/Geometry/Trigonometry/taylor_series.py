# Taylor series approximations for trigonometric functions
from typing import Union
from Math.utils.math_utils import PI


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

    # Range reduction: reduce angle to [-π, π] modulo 2π
    # This prevents numerical divergence for large angles and accelerates convergence.
    x = float(radians)
    twopi = 2.0 * PI
    x = x % twopi
    if x > PI:
        x -= twopi

    sine_value = x
    term = x
    radians_sq = x * x

    # Optimization: Terminate early when floating-point precision limit is reached
    # (i.e. term becomes smaller than double-precision float resolution relative to accumulated sum).
    for idx in range(3, terms * 2, 2):
        term *= -radians_sq / ((idx - 1) * idx)
        new_val = sine_value + term
        if new_val == sine_value:
            break
        sine_value = new_val

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

    # Range reduction: reduce angle to [-π, π] modulo 2π
    # This prevents numerical divergence for large angles and accelerates convergence.
    x = float(radians)
    twopi = 2.0 * PI
    x = x % twopi
    if x > PI:
        x -= twopi

    cos_value = 1.0
    term = 1.0
    radians_sq = x * x

    # Optimization: Terminate early when floating-point precision limit is reached
    # (i.e. term becomes smaller than double-precision float resolution relative to accumulated sum).
    for idx in range(2, terms * 2, 2):
        term *= -radians_sq / (idx * (idx - 1))
        new_val = cos_value + term
        if new_val == cos_value:
            break
        cos_value = new_val

    return cos_value
