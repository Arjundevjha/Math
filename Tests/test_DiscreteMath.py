import unittest

import pytest

from Math.Discrete_Math.Combinatorics.binomial_theorem_general_term import (
    binomial_general_term,
)
from Math.Discrete_Math.Combinatorics.pascals_triangle import (
    print_pascals_triangle,
    generate_pascals_triangle,
)
from Math.utils.math_utils import factorial
from Math.Discrete_Math.Number_Theory.partitions_approximation import (
    partition_approximation,
)
from Math.Discrete_Math.Number_Theory.partitions import partition


def test_factorial_zero():
    """Test that factorial of 0 is 1."""
    assert factorial(0) == 1


def test_factorial_one():
    """Test that factorial of 1 is 1."""
    assert factorial(1) == 1


def test_factorial_positive_integers():
    """Test factorial calculation for positive integers."""
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_large_number():
    """Test factorial calculation for a slightly larger number."""
    # 20! = 2432902008176640000
    assert factorial(20) == 2432902008176640000


def test_factorial_negative_number():
    """Test factorial with a negative number, which should raise RecursionError due to infinite recursion."""
    with pytest.raises(ValueError):
        factorial(-1)


class TestPascalsTriangle:
    def test_print_pascals_triangle_normal(self, capsys):
        """Test printing a normal Pascal's triangle."""
        triangle = [[1], [1, 1], [1, 2, 1]]
        print_pascals_triangle(triangle)
        captured = capsys.readouterr()

        expected_output = "  1  \n 1 1 \n1 2 1\n"
        assert captured.out == expected_output

    def test_print_pascals_triangle_empty(self, capsys):
        """Test printing an empty Pascal's triangle."""
        triangle = []
        print_pascals_triangle(triangle)
        captured = capsys.readouterr()

        assert captured.out == ""

    def test_generate_pascals_triangle_valid(self):
        """Test generating a valid Pascal's triangle."""
        assert generate_pascals_triangle(0) == []
        assert generate_pascals_triangle(1) == [[1]]
        assert generate_pascals_triangle(2) == [[1], [1, 1]]
        assert generate_pascals_triangle(3) == [[1], [1, 1], [1, 2, 1]]
        assert generate_pascals_triangle(5) == [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
        ]

    def test_generate_pascals_triangle_invalid(self):
        """Test generating an invalid Pascal's triangle with negative rows."""
        with pytest.raises(ValueError, match="Number of rows cannot be negative."):
            generate_pascals_triangle(-1)
        with pytest.raises(ValueError, match="Number of rows cannot be negative."):
            generate_pascals_triangle(-5)



def test_binomial_general_term():
    # (a + b)^2 = a^2 + 2ab + b^2
    assert binomial_general_term(2, 0, 1, 1) == 1
    assert binomial_general_term(2, 1, 1, 1) == 2
    assert binomial_general_term(2, 2, 1, 1) == 1


def test_binomial_general_term_edge_cases():
    # Test r < 0 or r > n
    with pytest.raises(ValueError, match="Invalid values for n and r"):
        binomial_general_term(2, -1, 1, 1)
    with pytest.raises(ValueError, match="Invalid values for n and r"):
        binomial_general_term(2, 3, 1, 1)


def test_binomial_general_term_powers():
    # (2 + 3)^3 = 1*2^3*3^0 + 3*2^2*3^1 + 3*2^1*3^2 + 1*2^0*3^3
    # n=3, r=0: 1 * 8 * 1 = 8
    # n=3, r=1: 3 * 4 * 3 = 36
    # n=3, r=2: 3 * 2 * 9 = 54
    # n=3, r=3: 1 * 1 * 27 = 27
    assert binomial_general_term(3, 0, 2, 3) == 8
    assert binomial_general_term(3, 1, 2, 3) == 36
    assert binomial_general_term(3, 2, 2, 3) == 54
    assert binomial_general_term(3, 3, 2, 3) == 27


def test_binomial_general_term_security():
    """Test security validation in binomial_general_term to prevent DoS and invalid inputs."""
    # Test invalid types for n and r
    with pytest.raises(TypeError, match="Power n and term index r must be integers."):
        binomial_general_term(2.5, 1, 1, 1)  # float n
    with pytest.raises(TypeError, match="Power n and term index r must be integers."):
        binomial_general_term(2, 1.5, 1, 1)  # float r
    with pytest.raises(TypeError, match="Power n and term index r must be integers."):
        binomial_general_term(True, 1, 1, 1)  # bool n
    with pytest.raises(TypeError, match="Power n and term index r must be integers."):
        binomial_general_term(2, True, 1, 1)  # bool r

    # Test invalid types for a and b
    with pytest.raises(TypeError, match=r"Terms a and b must be numeric \(int or float\)."):
        binomial_general_term(2, 1, "x", 1)  # str a
    with pytest.raises(TypeError, match=r"Terms a and b must be numeric \(int or float\)."):
        binomial_general_term(2, 1, 1, True)  # bool b

    # Test negative n
    with pytest.raises(ValueError, match="Power n must be non-negative."):
        binomial_general_term(-1, 0, 1, 1)

    # Test upper bound limit (DoS prevention)
    with pytest.raises(ValueError, match="Power n exceeds maximum limit of 1000."):
        binomial_general_term(1001, 500, 1, 1)


def test_partition_approximation_edge_cases():
    """Test edge cases for partition approximation."""
    # Test zero
    assert partition_approximation(0) == 1

    # Test negative numbers
    with pytest.raises(ValueError, match="Number must be a non-negative integer."):
        partition_approximation(-1)


def test_partition_approximation_small_values():
    """Test small values to ensure the formula computes successfully."""
    # We test values to see if they roughly equal actual partitions

    # The approximation formula is quite poor for very small n, but we can verify the output
    # p(1) ≈ 1
    assert partition_approximation(1) == 1

    # p(2) ≈ 2
    assert partition_approximation(2) == 2

    # p(3) = 3, approx is 4
    assert partition_approximation(3) == 4

    # p(4) = 5, approx is 6
    assert partition_approximation(4) == 6

    # p(5) = 7, approx is 8
    assert partition_approximation(5) == 8


def test_partition_approximation_large_values():
    """Test larger values to ensure the formula produces expected output."""
    # p(10) = 42, approx is 48
    assert partition_approximation(10) == 48

    # p(20) = 627, approx is 692
    assert partition_approximation(20) == 692

    # p(50) = 204226, approx is 217590
    assert partition_approximation(50) == 217590

    # p(100) = 190569292, approx is 199280893
    assert partition_approximation(100) == 199280893


def test_partition_approximation_relative_error():
    """Test that the approximation improves relative to the exact partition function."""
    # Compute relative error = |approx - exact| / exact
    n_values = [10, 20, 50, 100]
    errors = []

    for n in n_values:
        approx = partition_approximation(n)
        exact = partition(n)
        relative_error = abs(approx - exact) / exact
        errors.append(relative_error)

    # Relative error should generally decrease as n gets larger
    # Let's ensure the error at n=100 is less than error at n=10
    assert errors[-1] < errors[0]

    # And at n=100, the relative error should be < 5%
    assert errors[-1] < 0.05


def test_partition_negative():
    assert partition(-1) == 0
    assert partition(-10) == 0


def test_partition_zero():
    assert partition(0) == 1


def test_partition_positive():
    # Known values from OEIS A000041
    # n:    0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10
    # p(n): 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42
    assert partition(1) == 1
    assert partition(2) == 2
    assert partition(3) == 3
    assert partition(4) == 5
    assert partition(5) == 7
    assert partition(6) == 11
    assert partition(7) == 15
    assert partition(8) == 22
    assert partition(9) == 30
    assert partition(10) == 42
    assert partition(15) == 176
    assert partition(20) == 627
    assert partition(50) == 204226





if __name__ == "__main__":
    unittest.main()
