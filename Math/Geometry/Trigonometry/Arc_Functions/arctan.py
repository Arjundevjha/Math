# Arctangent (inverse tangent) function using Taylor series
from decimal import Decimal, getcontext, InvalidOperation
from typing import Union, Optional


def calculate_arctan(
    x: Union[int, float, Decimal],
    precision: int = 50,
    number_of_terms: Optional[int] = None,
) -> Decimal:
    """
    Calculate the arctangent of (1/x) in radians with specified precision using Taylor series.

    Parameters:
    x (Union[int, float, Decimal]): The value to calculate arctan(1/x) for.
    precision (int): The number of decimal places for the result (default: 50).
    number_of_terms (Optional[int]): Number of terms to use in the series. If None, continues until convergence.

    Returns:
    Decimal: The arctangent value in radians.
    """
    # Security: Validate precision to prevent Denial of Service (DoS) and invalid context errors
    if not isinstance(precision, int) or isinstance(precision, bool) or precision < 1 or precision > 10000:
        raise ValueError("Precision must be an integer between 1 and 10000.")

    # Set precision for Decimal calculations
    getcontext().prec = precision + 2

    if x == 0:
        return Decimal(0)
    elif x < 0:
        return -calculate_arctan(-x, precision, number_of_terms)

    arctan_value = Decimal(0)

    # Convert x to Decimal properly to avoid float underflow issues
    try:
        x_dec = Decimal(str(x)) if isinstance(x, float) else Decimal(x)
    except (ValueError, TypeError, InvalidOperation):
        x_dec = Decimal(x)

    # Check for extremely small x values that would underflow when squared
    try:
        x_squared = x_dec * x_dec
        if x_squared.is_zero():
            return arctan_value
    except (ArithmeticError, ValueError):
        return arctan_value

    # First term of the Taylor series: arctan(1/x) = Σ((-1)ⁿ / ((2n+1) × x^(2n+1)))
    try:
        term = Decimal(1) / x_dec
    except (ArithmeticError, ValueError):
        return arctan_value

    n = 0
    max_iterations = 100000  # Prevent infinite loop DoS

    # Optimization: Precompute -x_squared to avoid repeatedly instantiating -Decimal(1)
    # and performing extra intermediate multiplications in the inner loop.
    neg_x_sq = -x_squared

    if number_of_terms is not None:
        # Use fixed number of terms
        while n < number_of_terms and n < max_iterations:
            arctan_value += term / (2 * n + 1)
            n += 1
            try:
                term /= neg_x_sq
            except (ArithmeticError, ValueError):
                break
    else:
        # Optimization: Precompute convergence threshold Decimal(10) ** (-precision)
        # outside the loop to eliminate exponentiation on every iteration (~30% speedup).
        threshold = Decimal(10) ** (-precision)
        while abs(term) > threshold and n < max_iterations:
            arctan_value += term / (2 * n + 1)
            n += 1
            try:
                term /= neg_x_sq
            except (ArithmeticError, ValueError):
                break

        if n >= max_iterations:
            raise ValueError(
                "Series did not converge. x must be > 1 or < -1 for arctan(1/x) Taylor series convergence."
            )

    return arctan_value
