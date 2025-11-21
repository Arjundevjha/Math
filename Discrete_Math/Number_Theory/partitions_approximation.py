import sys
sys.path.append("../..")
from Numerical_Methods.Constants.Pi_Algorithms.S_Ramanujan_algo import S_Ramanujan_algo
from decimal import Decimal, getcontext
from Numerical_Methods.Constants.Eulers_number import EulersNumber

from math import sqrt


class Partition:

    def __call__(self, num: int) -> int:
        return self.partition(num)
    @staticmethod
    def partition(num: int) -> int:

        """Calculate an approximation of the number of partitions p(n) for a
        non-negative integer n using Ramanujan's asymptotic formula:

            p(n) ~ (1 / (4 * n * sqrt(3))) * exp(pi * sqrt(2n/3))

        Returns an integer approximation of p(n).
        """
        if num < 0:
            raise ValueError("Number must be a non-negative integer.")

        # Use Decimal for high-precision arithmetic and avoid mixing floats
        getcontext().prec = 60
        n_dec = Decimal(num)

        # sqrt(2n/3) as Decimal
        sqrt_term = (Decimal(2) * n_dec / Decimal(3)).sqrt()

        # pi as Decimal from Ramanujan algorithm (returns Decimal)
        pi_dec = S_Ramanujan_algo.calculate_pi_ramanujan(50, 10)

        # exponent = pi * sqrt(2n/3)
        exponent = pi_dec * sqrt_term

        # numerator = exp(exponent) using Decimal.exp()
        numerator = exponent.exp()

        # denominator = 4 * n * sqrt(3)
        denominator = Decimal(4) * n_dec * Decimal(3).sqrt()

        partition_number = numerator / denominator

        # Return integer approximation
        return int(partition_number)

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    partitions = Partition.partition(n)
    print(f"The number of partitions of {n} is: {int(partitions)}")
# This code calculates the number of partitions of a positive integer n.