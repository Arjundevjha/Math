import cmath
import pytest

from Math.Algebra.Polynomials.quartic_formula import (
    _compute_base_u,
    _compute_branch_roots,
    _compute_invariants,
    _compute_residual_error,
    quartic_formula,
)


def verify_roots(expected_roots, actual_roots, tol=1e-7):
    """
    Helper function to verify roots, accounting for multiplicity and
    floating point inaccuracies. Ensures that each expected root has
    exactly one corresponding actual root.
    """
    roots_list = list(actual_roots)
    for expected in expected_roots:
        matched = False
        for i, root in enumerate(roots_list):
            if cmath.isclose(expected, root, rel_tol=tol, abs_tol=tol):
                roots_list.pop(i)
                matched = True
                break
        assert matched, (
            f"Expected root {expected} not found. "
            f"Remaining unmatched actual roots: {roots_list}"
        )
    assert len(roots_list) == 0, f"Unexpected extra roots found: {roots_list}"


def assert_evaluates_to_zero(a, b, c, d, e, roots, tol=1e-6):
    """
    Helper function to verify that ax^4 + bx^3 + cx^2 + dx + e = 0
    for each root.
    """
    assert len(roots) == 4, f"Expected 4 roots, got {len(roots)}"
    for root in roots:
        val = (
            a * (root**4)
            + b * (root**3)
            + c * (root**2)
            + d * root
            + e
        )
        assert cmath.isclose(val, 0, abs_tol=tol, rel_tol=tol), (
            f"Failed for {a}x⁴ + {b}x³ + {c}x² + {d}x + {e} = 0. "
            f"Root: {root}, evaluated to: {val}"
        )


def test_quartic_formula_distinct_real_roots():
    # Equation: (x - 1)(x - 2)(x - 3)(x - 4) = 0
    # x^4 - 10x^3 + 35x^2 - 50x + 24 = 0
    roots = quartic_formula(1, -10, 35, -50, 24)
    expected_roots = [1, 2, 3, 4]
    verify_roots(expected_roots, roots)
    assert_evaluates_to_zero(1, -10, 35, -50, 24, roots)


def test_quartic_formula_non_zero_q():
    # Equation: (x - 1)(x - 2)(x - 3)(x - 5) = 0
    # x^4 - 11x^3 + 41x^2 - 61x + 30 = 0
    roots = quartic_formula(1, -11, 41, -61, 30)
    expected_roots = [1, 2, 3, 5]
    verify_roots(expected_roots, roots)
    assert_evaluates_to_zero(1, -11, 41, -61, 30, roots)


def test_quartic_formula_complex_roots():
    # Equation: x^4 - 1 = 0
    # Roots: 1, -1, i, -i
    roots = quartic_formula(1, 0, 0, 0, -1)
    expected_roots = [1, -1, 1j, -1j]
    verify_roots(expected_roots, roots)
    assert_evaluates_to_zero(1, 0, 0, 0, -1, roots)


def test_quartic_formula_quadruple_root():
    # Equation: (x - 2)^4 = x^4 - 8x^3 + 24x^2 - 32x + 16 = 0
    roots = quartic_formula(1, -8, 24, -32, 16)
    expected_roots = [2, 2, 2, 2]
    verify_roots(expected_roots, roots)
    assert_evaluates_to_zero(1, -8, 24, -32, 16, roots)


def test_quartic_formula_zero_roots():
    # Equation: x^4 = 0
    roots = quartic_formula(1, 0, 0, 0, 0)
    expected_roots = [0, 0, 0, 0]
    verify_roots(expected_roots, roots)
    assert_evaluates_to_zero(1, 0, 0, 0, 0, roots)


def test_quartic_formula_float_coefficients():
    # Equation: 2.5x^4 - 25x^3 + 87.5x^2 - 125x + 60 = 0
    # Roots: 1, 2, 3, 4
    roots = quartic_formula(2.5, -25.0, 87.5, -125.0, 60.0)
    expected_roots = [1, 2, 3, 4]
    verify_roots(expected_roots, roots)
    assert_evaluates_to_zero(2.5, -25.0, 87.5, -125.0, 60.0, roots)


def test_quartic_formula_negative_a():
    # Equation: -x^4 + 10x^3 - 35x^2 + 50x - 24 = 0
    # Roots: 1, 2, 3, 4
    roots = quartic_formula(-1, 10, -35, 50, -24)
    expected_roots = [1, 2, 3, 4]
    verify_roots(expected_roots, roots)
    assert_evaluates_to_zero(-1, 10, -35, 50, -24, roots)


def test_quartic_formula_value_error():
    # a = 0 should raise ValueError
    with pytest.raises(
        ValueError,
        match="Coefficient 'a' cannot be zero for a quartic equation.",
    ):
        quartic_formula(0, 1, 1, 1, 1)


def test_quartic_formula_mixed_roots():
    # Equation: (x^2 + 1)(x^2 - 4) = x^4 - 3x^2 - 4 = 0
    # Roots: 2, -2, i, -i
    roots = quartic_formula(1, 0, -3, 0, -4)
    expected_roots = [2, -2, 1j, -1j]
    verify_roots(expected_roots, roots)
    assert_evaluates_to_zero(1, 0, -3, 0, -4, roots)


def test_quartic_formula_helpers():
    # Test helper functions directly for equation
    # (x-1)(x-2)(x-3)(x-4) = x^4 - 10x^3 + 35x^2 - 50x + 24
    ca, cb, cc, cd, ce = (
        complex(1),
        complex(-10),
        complex(35),
        complex(-50),
        complex(24),
    )
    p1, p2 = _compute_invariants(ca, cb, cc, cd, ce)
    assert isinstance(p1, complex)
    assert isinstance(p2, complex)

    base_u = _compute_base_u(p1, p2)
    assert isinstance(base_u, complex)

    cube_root_2 = 2.0 ** (1.0 / 3.0)
    shift = -cb / (4.0 * ca)
    roots = _compute_branch_roots(
        ca, cb, cc, cd, base_u, p1, cube_root_2, shift
    )
    assert len(roots) == 4

    err = _compute_residual_error(ca, cb, cc, cd, ce, roots)
    assert isinstance(err, float)
    assert err >= 0.0


if __name__ == "__main__":
    pytest.main([__file__])
