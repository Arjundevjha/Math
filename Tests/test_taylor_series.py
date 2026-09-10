import pytest
from Math.Geometry.Trigonometry.taylor_series import sine_taylor, cosine_taylor

def test_sine_taylor_valid():
    pi = 3.141592653589793
    assert abs(sine_taylor(0) - 0.0) < 1e-5
    assert abs(sine_taylor(pi / 2) - 1.0) < 1e-5
    assert abs(sine_taylor(pi) - 0.0) < 1e-5
    assert abs(sine_taylor(pi / 6) - 0.5) < 1e-5

def test_cosine_taylor_valid():
    pi = 3.141592653589793
    assert abs(cosine_taylor(0) - 1.0) < 1e-5
    assert abs(cosine_taylor(pi / 2) - 0.0) < 1e-5
    assert abs(cosine_taylor(pi) - (-1.0)) < 1e-5
    assert abs(cosine_taylor(pi / 3) - 0.5) < 1e-5
    assert abs(cosine_taylor(pi / 4) - 0.70710678118) < 1e-5

def test_sine_taylor_invalid_terms():
    for invalid in [0, -1, 10001, True, False, 5.5, "10"]:
        with pytest.raises(ValueError, match="terms must be an integer between 1 and 10000."):
            sine_taylor(0, invalid)

def test_cosine_taylor_invalid_terms():
    for invalid in [0, -1, 10001, True, False, 5.5, "10"]:
        with pytest.raises(ValueError, match="terms must be an integer between 1 and 10000."):
            cosine_taylor(0, invalid)

def test_taylor_large_terms():
    pi = 3.141592653589793
    assert abs(sine_taylor(pi / 2, terms=1001) - 1.0) < 1e-5
    assert abs(cosine_taylor(0, terms=1001) - 1.0) < 1e-5

def test_taylor_large_angles():
    # Test range reduction for large angles (e.g. x = 10, 50, 100, -100)
    pi = 3.141592653589793
    # Compare against periodic reference values
    assert abs(sine_taylor(10.0) - sine_taylor(10.0 % (2 * pi))) < 1e-5
    assert abs(cosine_taylor(10.0) - cosine_taylor(10.0 % (2 * pi))) < 1e-5
    assert abs(sine_taylor(50.0) - sine_taylor(50.0 % (2 * pi))) < 1e-5
    assert abs(cosine_taylor(50.0) - cosine_taylor(50.0 % (2 * pi))) < 1e-5
    assert abs(sine_taylor(100.0) - sine_taylor(100.0 % (2 * pi))) < 1e-5
    assert abs(cosine_taylor(100.0) - cosine_taylor(100.0 % (2 * pi))) < 1e-5
    assert abs(sine_taylor(-100.0) - sine_taylor(-100.0 % (2 * pi))) < 1e-5
    assert abs(cosine_taylor(-100.0) - cosine_taylor(-100.0 % (2 * pi))) < 1e-5
