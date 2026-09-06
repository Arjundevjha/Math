# Calculate the number of partitions of a positive integer


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
    # partitions in O(n sqrt(n)) time instead of O(n^2) dynamic programming.
    # Recurrence: p(n) = sum_{k != 0} (-1)^(k-1) * p(n - g_k), where
    # g_k = k(3k - 1)/2 for k = 1, -1, 2, -2, 3, -3, ...
    pentagonals = []
    k = 1
    while True:
        g1 = (k * (3 * k - 1)) // 2
        g2 = (k * (3 * k + 1)) // 2
        sign = 1 if (k % 2 == 1) else -1
        if g1 > n:
            break
        pentagonals.append((g1, sign))
        if g2 <= n:
            pentagonals.append((g2, sign))
        k += 1

    partitions = [0] * (n + 1)
    partitions[0] = 1

    num_pent = len(pentagonals)
    active = 0
    active_pos = []
    active_neg = []

    for i in range(1, n + 1):
        if active < num_pent and pentagonals[active][0] == i:
            while active < num_pent and pentagonals[active][0] <= i:
                g, sign = pentagonals[active]
                if sign == 1:
                    active_pos.append(g)
                else:
                    active_neg.append(g)
                active += 1

        total = 0
        for g in active_pos:
            total += partitions[i - g]
        for g in active_neg:
            total -= partitions[i - g]
        partitions[i] = total

    return partitions[n]
