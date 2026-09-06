# Binomial theorem expansion
from Math.Discrete_Math.Combinatorics.combination import nCr


def binomial_coefficient(n: int, r: int) -> int:
    """
    Calculate the binomial coefficient C(n, r).

    Parameters:
    n (int): The power to which the binomial is raised.
    r (int): The term index.

    Returns:
    int: The binomial coefficient.
    """
    return nCr(n, r)


def expand_binomial(a: str, b: str, n: int) -> str:
    """
    Expand the binomial (a + b)^n using the binomial theorem.

    Parameters:
    a (str): The first term of the binomial.
    b (str): The second term of the binomial.
    n (int): The power to which the binomial is raised.

    Returns:
    str: The expanded form of the binomial.
    """
    # Security: Validate type and enforce upper bound limit to prevent DoS via CPU/memory exhaustion
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Power n must be an integer.")
    if n < 0:
        raise ValueError("Power n must be non-negative.")
    if n > 1000:
        raise ValueError("Power n exceeds maximum limit of 1000.")
    
    result = []
    # Expand using binomial theorem: (a+b)ⁿ = Σ C(n,r) × aⁿ⁻ʳ × bʳ
    # Optimization: Compute coefficients iteratively in O(1) per term using
    # C(n, r) = C(n, r-1) * (n - r + 1) // r, reducing total complexity to O(n).
    coeff = 1
    for r in range(n + 1):
        if r > 0:
            coeff = coeff * (n - r + 1) // r
        term = f"{coeff}*{a}^{n - r}*{b}^{r}"
        result.append(term)
    
    return " + ".join(result)