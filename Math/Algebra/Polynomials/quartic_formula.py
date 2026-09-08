# Quartic formula solver for equations of the form ax⁴ + bx³ + cx² + dx + e = 0
from typing import Tuple, Union


def _compute_invariants(
    ca: complex, cb: complex, cc: complex, cd: complex, ce: complex
) -> Tuple[complex, complex]:
    """
    Compute invariant polynomial terms p1 and p2 for Landesman's formula.

    Parameters:
    ca, cb, cc, cd, ce (complex): Complex coefficients of the quartic.

    Returns:
    Tuple[complex, complex]: Computed (p1, p2) invariant values.
    """
    p1 = cc**2 - 3.0 * cb * cd + 12.0 * ca * ce
    p2 = (
        2.0 * (cc**3)
        - 9.0 * cb * cc * cd
        - 72.0 * ca * cc * ce
        + 27.0 * ca * (cd**2)
        + 27.0 * (cb**2) * ce
    )
    return p1, p2


def _compute_base_u(p1: complex, p2: complex) -> complex:
    """
    Compute the base core cube-root term U before branch selection.

    Parameters:
    p1, p2 (complex): Invariant polynomial terms.

    Returns:
    complex: Base cube root term.
    """
    inner = p2**2 - 4.0 * (p1**3)
    return (p2 + inner**0.5) ** (1.0 / 3.0)


def _compute_branch_roots(
    ca: complex,
    cb: complex,
    cc: complex,
    cd: complex,
    U: complex,
    p1: complex,
    cube_root_2: float,
    shift: complex,
) -> Tuple[complex, complex, complex, complex]:
    """
    Compute the four candidate quartic roots for a specific cube root branch U.

    Parameters:
    ca, cb, cc, cd (complex): Polynomial coefficients.
    U (complex): Current cube-root branch value.
    p1 (complex): Invariant p1 term.
    cube_root_2 (float): Pre-calculated 2^(1/3).
    shift (complex): Shift value -b / (4a).

    Returns:
    Tuple[complex, complex, complex, complex]: Four candidate roots.
    """
    term_U = U / (3.0 * cube_root_2 * ca)
    term_p1 = (
        (cube_root_2 * p1) / (3.0 * ca * U) if abs(U) > 1e-15 else 0.0
    )

    # Resolvent Radical (R)
    R_inner = (
        (cb**2) / (4.0 * (ca**2))
        - (2.0 * cc) / (3.0 * ca)
        + term_U
        + term_p1
    )
    R = R_inner**0.5

    # Core Polynomial Shift & Cross-Term (V) and Base Expression (Q)
    if abs(R) > 1e-15:
        v_num = (
            -((cb**3) / (ca**3))
            + (4.0 * cb * cc) / (ca**2)
            - (8.0 * cd) / ca
        )
        V = v_num / (4.0 * R)
    else:
        V = 0.0

    Q = (
        (cb**2) / (2.0 * (ca**2))
        - (4.0 * cc) / (3.0 * ca)
        - term_U
        - term_p1
    )

    # Compact Quartic Roots
    half_R = 0.5 * R
    sqrt_Q_minus_V = (Q - V) ** 0.5
    sqrt_Q_plus_V = (Q + V) ** 0.5

    x1 = shift - half_R - 0.5 * sqrt_Q_minus_V
    x2 = shift - half_R + 0.5 * sqrt_Q_minus_V
    x3 = shift + half_R - 0.5 * sqrt_Q_plus_V
    x4 = shift + half_R + 0.5 * sqrt_Q_plus_V

    return (x1, x2, x3, x4)


def _compute_residual_error(
    ca: complex,
    cb: complex,
    cc: complex,
    cd: complex,
    ce: complex,
    roots: Tuple[complex, complex, complex, complex],
) -> float:
    """
    Calculate residual sum of absolute evaluation errors for candidate roots.

    Parameters:
    ca, cb, cc, cd, ce (complex): Coefficients of the quartic equation.
    roots (Tuple[complex, ...]): The candidate roots to evaluate.

    Returns:
    float: Total residual error across all four roots.
    """
    return sum(
        abs(ca * (r**4) + cb * (r**3) + cc * (r**2) + cd * r + ce)
        for r in roots
    )


def _select_best_branch(
    ca: complex,
    cb: complex,
    cc: complex,
    cd: complex,
    ce: complex,
    base_U: complex,
    p1: complex,
    shift: complex,
) -> Tuple[complex, complex, complex, complex]:
    """
    Evaluate candidate roots across cube root branches of U to find the set
    with minimum residual error.

    Parameters:
    ca, cb, cc, cd, ce (complex): Complex coefficients of the quartic equation.
    base_U (complex): Base cube root term.
    p1 (complex): Invariant polynomial term p1.
    shift (complex): Shift value -b / (4a).

    Returns:
    Tuple[complex, complex, complex, complex]: The best candidate roots.
    """
    cube_root_2 = 2.0 ** (1.0 / 3.0)
    omega = complex(-0.5, 0.8660254037844386)

    best_roots: Tuple[complex, complex, complex, complex] = (
        0j,
        0j,
        0j,
        0j,
    )
    best_error = float("inf")

    # Evaluate all 3 cube root branches of U to find the optimal branch
    for k in range(3):
        U = base_U * (omega**k)
        roots = _compute_branch_roots(
            ca, cb, cc, cd, U, p1, cube_root_2, shift
        )
        err = _compute_residual_error(ca, cb, cc, cd, ce, roots)

        if err < best_error:
            best_error = err
            best_roots = roots

    return best_roots


def quartic_formula(
    a: Union[float, int],
    b: Union[float, int],
    c: Union[float, int],
    d: Union[float, int],
    e: Union[float, int],
) -> Tuple[complex, complex, complex, complex]:
    """
    Solve quartic equations of the form ax⁴ + bx³ + cx² + dx + e = 0
    using Landesman's closed-form quartic formula.

    Parameters:
    a (Union[float, int]): Coefficient of x⁴.
    b (Union[float, int]): Coefficient of x³.
    c (Union[float, int]): Coefficient of x².
    d (Union[float, int]): Coefficient of x.
    e (Union[float, int]): Constant term.

    Returns:
    Tuple[complex, complex, complex, complex]: The four roots of the quartic.

    Examples:
    >>> quartic_formula(1, -10, 35, -50, 24)
    ((1+0j), (2+0j), (3+0j), (4+0j))
    """
    if a == 0:
        raise ValueError(
            "Coefficient 'a' cannot be zero for a quartic equation."
        )

    ca, cb, cc, cd, ce = (
        complex(a),
        complex(b),
        complex(c),
        complex(d),
        complex(e),
    )

    p1, p2 = _compute_invariants(ca, cb, cc, cd, ce)
    base_U = _compute_base_u(p1, p2)
    shift = -cb / (4.0 * ca)

    return _select_best_branch(ca, cb, cc, cd, ce, base_U, p1, shift)
