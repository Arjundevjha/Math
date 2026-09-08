# Calculate the number of partitions of a positive integer
from typing import List, Tuple


def _generate_pentagonals(n: int) -> List[Tuple[int, int]]:
    """
    Generate generalized pentagonal numbers up to n with their corresponding signs according to Euler's Pentagonal Formula.

    Parameters:
    n (int): The maximum limit for pentagonal numbers.

    Returns:
    List[Tuple[int, int]]: A list of tuples containing (pentagonal_number, sign).
    """
    pentagonals = []
    k = 1
    while True:
        g1 = (k * (3 * k - 1)) // 2
        g2 = (k * (3 * k + 1)) // 2
        sign = 1 if (k % 2 != 0) else -1
        if g1 > n:
            break
        pentagonals.append((g1, sign))
        if g2 <= n:
            pentagonals.append((g2, sign))
        k += 1
    return pentagonals


def partition(n: int) -> int:
    """
    Calculate the number of partitions of a positive integer n.

    Parameters:
    n (int): The positive integer to partition.

    Returns:
    int: The number of partitions of n.
    """
    # Security: Validate input type and upper bound to prevent DoS via excessive memory/CPU allocation
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n > 10000:
        raise ValueError("n exceeds maximum limit of 10000.")

    # Optimization: Use Euler's pentagonal number theorem to calculate
    # partitions in O(n sqrt(n)) time.
    # Recurrence: p(n) = sum_{k != 0} (-1)^(k-1) * p(n - g_k)
    pentagonals = _generate_pentagonals(n)

    partitions = [0] * (n + 1)
    partitions[0] = 1

    for i in range(1, n + 1):
        total = 0
        for g, sign in pentagonals:
            if g > i:
                break
            total += sign * partitions[i - g]
        partitions[i] = total

    return partitions[n]
