# S. Ramanujan's formula for calculating Pi
from decimal import Decimal, getcontext


def calculate_pi_ramanujan(num_decimal_places: int = 50, num_terms: int = 10) -> Decimal:
    """
    Calculate Pi using S. Ramanujan's formula.
    
    Formula: 1/π = (2√2/9801) × Σ[(4k)! × (1103 + 26390k)] / [(k!)⁴ × 396^(4k)]

    Parameters:
    num_decimal_places (int): The desired number of decimal places for pi (default: 50).
    num_terms (int): The number of terms to use in the series summation (default: 10).

    Returns:
    Decimal: The calculated value of pi.
    """
    # Validate parameters to prevent Denial of Service (DoS) via excessive precision or iterations
    if not isinstance(num_decimal_places, int) or isinstance(num_decimal_places, bool) or num_decimal_places < 0 or num_decimal_places > 10000:
        raise ValueError("num_decimal_places must be an integer between 0 and 10000.")
    if not isinstance(num_terms, int) or isinstance(num_terms, bool) or num_terms < 1 or num_terms > 10000:
        raise ValueError("num_terms must be an integer between 1 and 10000.")

    # Set precision for Decimal calculations with extra buffer
    getcontext().prec = num_decimal_places + 20

    total_sum = Decimal(0)
    # Calculate constant: (2√2)/9801
    constant = (Decimal(2) * Decimal(2).sqrt()) / Decimal(9801)

    term_multiplier = Decimal(1)
    # 396^4 = 24591257856
    c396_4 = 24591257856

    # Apply Ramanujan's series
    for k in range(num_terms):
        numerator_expression = Decimal(1103 + 26390 * k)

        # Add to total sum
        term = term_multiplier * numerator_expression
        total_sum += term

        # Calculate next term_multiplier: T_{k} = (4k)! / ((k!)^4 * 396^{4k})
        # The ratio T_{k+1} / T_k = (4k+4)(4k+3)(4k+2)(4k+1) / ((k+1)^4 * 396^4)
        next_k = k + 1
        num = (4 * k + 4) * (4 * k + 3) * (4 * k + 2) * (4 * k + 1)
        den = (next_k ** 4) * c396_4
        term_multiplier = (term_multiplier * num) / den

    # Calculate 1/π
    one_over_pi = constant * total_sum

    # Calculate π = 1 / (1/π)
    pi_value = Decimal(1) / one_over_pi

    return pi_value