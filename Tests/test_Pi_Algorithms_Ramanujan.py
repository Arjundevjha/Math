# Unit tests for S. Ramanujan's Pi calculation algorithm
from decimal import Decimal
import pytest

from Math.Numerical_Methods.Constants.Pi_Algorithms.S_Ramanujan_algo import (
    calculate_pi_ramanujan,
)

class TestRamanujanAlgorithm:
    """Test suite for calculate_pi_ramanujan function."""

    KNOWN_PI_50_DIGITS = "3.14159265358979323846264338327950288419716939937510"
    KNOWN_PI_100_DIGITS = (
        "3.14159265358979323846264338327950288419716939937510"
        "58209749445923078164062862089986280348253421170679"
    )

    def test_calculate_pi_ramanujan_default_args(self):
        """Test default arguments (num_decimal_places=50, num_terms=10)."""
        pi_val = calculate_pi_ramanujan()
        assert isinstance(pi_val, Decimal)
        assert str(pi_val).startswith(self.KNOWN_PI_50_DIGITS)

    def test_calculate_pi_ramanujan_precision(self):
        """Test calculation with high precision."""
        pi_val = calculate_pi_ramanujan(num_decimal_places=100, num_terms=15)
        assert isinstance(pi_val, Decimal)
        # Verify precision against known digits (prefix match to avoid endpoint rounding)
        assert str(pi_val).startswith(self.KNOWN_PI_100_DIGITS[:90])

    def test_calculate_pi_ramanujan_convergence(self):
        """Test that adding terms improves accuracy of the approximation."""
        pi_1 = calculate_pi_ramanujan(num_decimal_places=50, num_terms=1)
        pi_2 = calculate_pi_ramanujan(num_decimal_places=50, num_terms=2)
        pi_3 = calculate_pi_ramanujan(num_decimal_places=50, num_terms=3)

        float_pi = 3.141592653589793
        error_1 = abs(float(pi_1) - float_pi)
        error_2 = abs(float(pi_2) - float_pi)
        error_3 = abs(float(pi_3) - float_pi)

        assert error_1 < 1e-5
        assert error_2 < error_1
        assert error_3 < error_2

    def test_calculate_pi_ramanujan_boundary_decimal_places(self):
        """Test boundary conditions for num_decimal_places."""
        # Lower bound: 0
        pi_0 = calculate_pi_ramanujan(num_decimal_places=0, num_terms=5)
        assert isinstance(pi_0, Decimal)
        assert str(pi_0).startswith("3")

    def test_calculate_pi_ramanujan_terms_boundary(self):
        """Test boundary conditions for num_terms (lower bound = 1)."""
        pi_1 = calculate_pi_ramanujan(num_decimal_places=10, num_terms=1)
        assert isinstance(pi_1, Decimal)
        assert str(pi_1).startswith("3.141592")

    def test_calculate_pi_ramanujan_invalid_decimal_places(self):
        """Test invalid num_decimal_places values raise ValueError."""
        invalid_values = [-1, -10, 10001, True, False, 5.5, "50"]
        expected_msg = r"^num_decimal_places must be an integer between 0 and 10000\.$"

        for val in invalid_values:
            with pytest.raises(ValueError, match=expected_msg):
                calculate_pi_ramanujan(num_decimal_places=val, num_terms=10)

    def test_calculate_pi_ramanujan_invalid_terms(self):
        """Test invalid num_terms values raise ValueError."""
        invalid_values = [0, -1, -10, 10001, True, False, 2.5, "10"]
        expected_msg = r"^num_terms must be an integer between 1 and 10000\.$"

        for val in invalid_values:
            with pytest.raises(ValueError, match=expected_msg):
                calculate_pi_ramanujan(num_decimal_places=50, num_terms=val)
