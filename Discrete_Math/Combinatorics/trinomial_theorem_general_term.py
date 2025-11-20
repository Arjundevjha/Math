#class for trinomial theorem general term
import sys
sys.path.append("../..")

from Numerical_Methods.Functions.Factorial.factorial import Factorial
class TrinomialTheorem:
    """
    Class to calculate the general term in the trinomial expansion of (a + b + c)^n.
    The general term T_(i, j, k) is given by:
    T_(i, j, k) = n! / (i! * j! * k!) * a^i * b^j * c^k
    where n = i + j + k and i, j, k are non-negative integers.
    """

    @staticmethod
    def general_term(n, i, j, a, b, c):
        """Calculate the general term in the trinomial expansion."""
        if i < 0 or j < 0 or i + j > n:
            raise ValueError("Invalid values for n, i, and j.")
        k = n - i - j
        if k < 0:
            raise ValueError("Invalid value for k.")
        n_factorial = Factorial.factorial(n)
        i_factorial = Factorial.factorial(i)
        j_factorial = Factorial.factorial(j)
        k_factorial = Factorial.factorial(k)
        return (n_factorial // (i_factorial * j_factorial * k_factorial)) * (a ** i) * (b ** j) * (c ** k)

if __name__ == "__main__":
    # Example usage
    n = int(input("Enter the exponent n for (a + b + c)^n: "))
    i = int(input("Enter the value of i (for a^i): "))
    j = int(input("Enter the value of j (for b^j): "))
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    
    try:
        term = TrinomialTheorem.general_term(n, i, j, a, b, c)
        print(f"The general term T_({i}, {j}, {n - i - j}) in the expansion of (a + b + c)^{n} is: {term}")
    except ValueError as e:
        print(e)