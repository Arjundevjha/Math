# Trinomial theorem expansion
from Math.Discrete_Math.Combinatorics.combination import nCr


def trinomial_coefficient(n: int, i: int, j: int) -> int:
    """
    Calculate the coefficient for a term in the trinomial expansion.

    Parameters:
    n (int): The exponent in the trinomial expansion.
    i (int): The power of the first term.
    j (int): The power of the second term.

    Returns:
    int: The coefficient for the term.
    """
    if i < 0 or j < 0 or i + j > n:
        return 0
    
    # Calculate coefficient using formula: C(n,i) × C(n-i,j)
    k = n - i - j
    return nCr(n, i) * nCr(n - i, j)


def expand_trinomial(a: str, b: str, c: str, n: int) -> str:
    """
    Expand the trinomial (a + b + c)^n using the trinomial theorem.

    Parameters:
    a (str): The first term of the trinomial.
    b (str): The second term of the trinomial.
    c (str): The third term of the trinomial.
    n (int): The power to which the trinomial is raised.

    Returns:
    str: The expanded form of the trinomial.
    """
    # Security: Validate input type and upper bound limit to prevent DoS via excessive CPU/memory resource exhaustion
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Power n must be an integer.")
    if n < 0:
        raise ValueError("Power n must be non-negative.")
    if n > 1000:
        raise ValueError("Power n exceeds maximum limit of 1000.")
    
    result = []
    # Expand using trinomial theorem: (a+b+c)ⁿ = Σ C(n,i)×C(n-i,j) × aⁱ × bʲ × cᵏ
    # Optimization: Iterative recurrence for both C(n, i) and C(n-i, j) achieves O(1)
    # updates per term without redundant nCr function calls or branching checks.
    c_n_i = 1
    for i in range(n + 1):
        rem = n - i
        c_rem_j = 1
        for j in range(rem + 1):
            k = rem - j
            coeff = c_n_i * c_rem_j
            term = f"{coeff}*{a}^{i}*{b}^{j}*{c}^{k}"
            result.append(term)
            c_rem_j = c_rem_j * (rem - j) // (j + 1)
        c_n_i = c_n_i * (n - i) // (i + 1)
    
    return " + ".join(result)
