# Arcsine calculation using numerical approximation
from typing import Union

from Math.Geometry.Trigonometry.taylor_series import sine_taylor



def arcsin_numerical(
    sin_value: Union[int, float], precision: float = 0.0001
) -> Union[float, None]:
    """
    Calculate arcsine using numerical approximation by finding angle where sin(angle) = sin_value.

    Parameters:
    sin_value (Union[int, float]): The sine value to find the arcsine for (must be between -1 and 1).
    precision (float): The precision for the approximation (default: 0.0001).

    Returns:
    Union[float, None]: The angle in radians, or None if not found.
    """
    if sin_value < -1 or sin_value > 1:
        raise ValueError("Sine value must be between -1 and 1.")

    # Use numerical search to find angle where sin(angle) ≈ sin_value
    import decimal

    decimal.getcontext().prec = 50

    pi_approx = 3.14159265358979323846

    # Search in range [0, π/2] for positive values using binary search (bisection method).
    # Optimization: Replaced O(1/step) linear scan (~15,700 iterations) with O(log(1/eps))
    # binary search (~25 iterations) since sine is strictly monotonic on [0, π/2].
    if sin_value < 0:
        return None

    low = 0.0
    high = pi_approx / 2

    # Perform binary search down to target tolerance interval
    while high - low > 1e-7:
        mid = (low + high) / 2
        calc_sin = sine_taylor(mid, terms=25)
        if calc_sin < sin_value:
            low = mid
        else:
            high = mid

    angle = (low + high) / 2
    calc_sin = sine_taylor(angle, terms=25)
    if abs(calc_sin - sin_value) < precision:
        return angle

    return None
