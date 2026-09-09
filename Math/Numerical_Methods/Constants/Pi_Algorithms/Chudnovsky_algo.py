# Chudnovsky algorithm for calculating Pi
from decimal import Decimal, getcontext


def calculate_pi_chudnovsky(precision: int = 50) -> Decimal:
    """
    Calculate Pi using the Chudnovsky algorithm.
    
    This is one of the fastest known algorithms for calculating Pi.

    Parameters:
    precision (int): The number of decimal places for the result (default: 50).

    Returns:
    Decimal: The value of Pi to the specified precision.
    """
    # Validate precision bounds and types to prevent DoS via unbounded precision context
    if (
        not isinstance(precision, int)
        or isinstance(precision, bool)
        or precision < 1
        or precision > 10000
    ):
        raise ValueError("Precision must be an integer between 1 and 10000.")

    # Set precision for Decimal calculations
    getcontext().prec = precision + 20

    # Chudnovsky algorithm constants
    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(1)
    S = L

    # Optimization: Each Chudnovsky series term yields ~14.18 digits of precision.
    # Computing `precision` terms performs redundant Decimal divisions.
    # Calculating max(1, (precision + 13) // 14) terms achieves the exact required
    # target precision with ~14x speedup.
    num_terms = max(1, (precision + 13) // 14)
    c_l = 545140134
    c_x = -262537412640768000
    k_int = 6

    # Apply Chudnovsky series
    # Optimization: Compute term recurrence updates using scalar integer arithmetic
    # (num_int = k_int**3 - 16*k_int, den_int = n**3) and integer multiplier c_x.
    # Eliminates Decimal exponentiation (K**3) and intermediate Decimal object instantiations per loop step.
    for n in range(1, num_terms):
        num_int = k_int**3 - 16 * k_int
        den_int = n**3
        M = (M * num_int) / den_int
        L += c_l
        X *= c_x
        S += (M * L) / X
        k_int += 12

    # Calculate π = C / S
    pi = C / S
    return pi

