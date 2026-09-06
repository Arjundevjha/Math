# Calculate the number of partitions of a positive integer
from typing import Iterator, List, Tuple


def _generate_pentagonals(n: int) -> Iterator[Tuple[int, int]]:
    """
    Generate generalized pentagonal numbers g_k and sign (-1)^(k-1) up to n.

    Parameters:
    n (int): Upper bound limit for pentagonal numbers.

    Yields:
    Tuple[int, int]: Pair of (pentagonal_number, sign).
    """
    k = 1
    while True:
        g1 = (k * (3 * k - 1)) // 2
        if g1 > n:
            break
        sign = 1 if (k % 2 == 1) else -1
        yield g1, sign

        g2 = (k * (3 * k + 1)) // 2
        if g2 <= n:
            yield g2, sign
        k += 1


def _partition_terms(
    i: int, pentagonals: List[Tuple[int, int]], partitions: List[int]
) -> Iterator[int]:
    """
    Yield recurrence terms sign * partitions[i - g] for partition(i).

    Parameters:
    i (int): Current integer value being evaluated.
    pentagonals (List[Tuple[int, int]]): List of (pentagonal_number, sign).
    partitions (List[int]): Array of previously calculated partition values.

    Yields:
    int: Term value to contribute to partition(i).
    """
    for g, sign in pentagonals:
        if g > i:
            break
        yield sign * partitions[i - g]


def partition(n: int) -> int:
    """
    Calculate the number of partitions of a positive integer n.

    Parameters:
    n (int): The positive integer to partition.

    Returns:
    int: The number of partitions of n.
    """
    # Security: Validate input type and upper bound to prevent DoS
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n > 10000:
        raise ValueError("n exceeds maximum limit of 10000.")

    # Optimization: Use Euler's pentagonal number theorem to calculate
    # partitions in O(n sqrt(n)) time instead of O(n^2) dynamic programming.
    # Recurrence: p(n) = sum_{k != 0} (-1)^(k-1) * p(n - g_k), where
    # g_k = k(3k - 1)/2 for k = 1, -1, 2, -2, 3, -3, ...
    pentagonals = list(_generate_pentagonals(n))

    partitions = [0] * (n + 1)
    partitions[0] = 1

    for i in range(1, n + 1):
        partitions[i] = sum(_partition_terms(i, pentagonals, partitions))

    return partitions[n]
