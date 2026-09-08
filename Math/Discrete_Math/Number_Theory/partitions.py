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
    # partitions in O(n sqrt(n)) time.
    # Recurrence: p(n) = sum_{k != 0} (-1)^(k-1) * p(n - g_k)
    # Precomputing pentagonals into positive and negative term lists and maintaining
    # active lists eliminates inner-loop branching and sign multiplication overhead.
    pos_pentagonals = []
    neg_pentagonals = []
    k = 1
    while True:
        g1 = (k * (3 * k - 1)) // 2
        g2 = (k * (3 * k + 1)) // 2
        if g1 > n:
            break
        target = pos_pentagonals if (k % 2 == 1) else neg_pentagonals
        target.append(g1)
        if g2 <= n:
            target.append(g2)
        k += 1

    partitions = [0] * (n + 1)
    partitions[0] = 1

    active_pos = []
    active_neg = []
    pos_idx = 0
    neg_idx = 0
    num_pos = len(pos_pentagonals)
    num_neg = len(neg_pentagonals)

    next_pos = pos_pentagonals[0] if num_pos > 0 else n + 1
    next_neg = neg_pentagonals[0] if num_neg > 0 else n + 1

    for i in range(1, n + 1):
        if i == next_pos:
            active_pos.append(i)
            pos_idx += 1
            next_pos = pos_pentagonals[pos_idx] if pos_idx < num_pos else n + 1
        if i == next_neg:
            active_neg.append(i)
            neg_idx += 1
            next_neg = neg_pentagonals[neg_idx] if neg_idx < num_neg else n + 1

        total = 0
        for g in active_pos:
            total += partitions[i - g]
        for g in active_neg:
            total -= partitions[i - g]
        partitions[i] = total

    return partitions[n]
