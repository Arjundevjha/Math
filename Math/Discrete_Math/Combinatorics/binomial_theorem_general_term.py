# General term of the binomial expansion
from typing import Union

from Math.Discrete_Math.Combinatorics.combination import nCr


def binomial_general_term(n: int, r: int, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculate the general term in the binomial expansion of (a + b)^n.

    Parameters:
    n (int): The exponent in the binomial expansion.
    r (int): The term index (0-indexed).
    a (Union[int, float]): The first term in the binomial.
    b (Union[int, float]): The second term in the binomial.

    Returns:
    Union[int, float]: The (r+1)th term in the expansion.
    """
    # Security: Validate input parameter types and upper bound limit to prevent DoS via CPU/memory resource exhaustion
    if not isinstance(n, int) or isinstance(n, bool) or not isinstance(r, int) or isinstance(r, bool):
        raise TypeError("Power n and term index r must be integers.")
    if not isinstance(a, (int, float)) or isinstance(a, bool) or not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Terms a and b must be numeric (int or float).")
    if n < 0:
        raise ValueError("Power n must be non-negative.")
    if r < 0 or r > n:
        raise ValueError("Invalid values for n and r. r must be between 0 and n.")
    if n > 1000:
        raise ValueError("Power n exceeds maximum limit of 1000.")

    # Calculate general term using formula: T_(r+1) = C(n,r) × a^(n-r) × b^r
    c = nCr(n, r)
    return c * (a ** (n - r)) * (b ** r)
