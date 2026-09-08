# Nilakantha series for calculating Pi
from decimal import Decimal, getcontext


def calculate_pi_nilakantha(terms: int = 100, precision: int = 50) -> Decimal:
    """
    Calculate Pi using Nilakantha's algorithm.
    
    Formula: π = 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - ...

    Parameters:
    terms (int): The number of terms to calculate (default: 100).
    precision (int): The number of decimal places for precision (default: 50).

    Returns:
    Decimal: The calculated value of Pi.
    """
    # Security: Validate input parameters to prevent Denial of Service (DoS) via resource exhaustion
    if not isinstance(terms, int) or isinstance(terms, bool) or terms < 1 or terms > 10000:
        raise ValueError("terms must be an integer between 1 and 10000.")
    if not isinstance(precision, int) or isinstance(precision, bool) or precision < 1 or precision > 10000:
        raise ValueError("precision must be an integer between 1 and 10000.")
    
    # Set precision for Decimal calculations
    getcontext().prec = precision + 10
    
    pi = Decimal(3.0)
    four = Decimal(4)
    neg_four = Decimal(-4)
    curr_four = four

    # Apply Nilakantha series: π = 3 + Σ(sign × 4/(i×(i+1)×(i+2)))
    for i in range(2, 2 * terms + 1, 2):
        pi += curr_four / (i * (i + 1) * (i + 2))
        curr_four, neg_four = neg_four, curr_four

    return pi