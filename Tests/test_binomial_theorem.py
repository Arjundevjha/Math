import pytest

# Add root directory to path



from Math.Discrete_Math.Combinatorics.binomial_theorem import expand_binomial, binomial_coefficient

def test_expand_binomial_basic():
    # (x + y)^2 = 1*x^2*y^0 + 2*x^1*y^1 + 1*x^0*y^2
    result = expand_binomial('x', 'y', 2)
    terms = [term.strip() for term in result.split('+')]

    assert "1*x^2*y^0" in terms
    assert "2*x^1*y^1" in terms
    assert "1*x^0*y^2" in terms
    assert len(terms) == 3


def test_expand_binomial_n_0():
    # (x + y)^0 = 1*x^0*y^0
    result = expand_binomial('x', 'y', 0)
    terms = [term.strip() for term in result.split('+')]

    assert "1*x^0*y^0" in terms
    assert len(terms) == 1


def test_expand_binomial_n_3():
    # (a + b)^3 = 1*a^3*b^0 + 3*a^2*b^1 + 3*a^1*b^2 + 1*a^0*b^3
    result = expand_binomial('a', 'b', 3)
    terms = [term.strip() for term in result.split('+')]

    assert "1*a^3*b^0" in terms
    assert "3*a^2*b^1" in terms
    assert "3*a^1*b^2" in terms
    assert "1*a^0*b^3" in terms
    assert len(terms) == 4


def test_expand_binomial_negative_n():
    with pytest.raises(ValueError, match="Power n must be non-negative."):
        expand_binomial('x', 'y', -1)


def test_expand_binomial_exceeds_max_n():
    with pytest.raises(ValueError, match="Power n exceeds maximum limit of 1000."):
        expand_binomial('x', 'y', 1001)


def test_expand_binomial_invalid_type():
    with pytest.raises(TypeError, match="Power n must be an integer."):
        expand_binomial('x', 'y', 2.5)  # float
    with pytest.raises(TypeError, match="Power n must be an integer."):
        expand_binomial('x', 'y', True)  # bool


def test_binomial_coefficient_normal():
    assert binomial_coefficient(5, 2) == 10
    assert binomial_coefficient(10, 3) == 120
    assert binomial_coefficient(6, 3) == 20


def test_binomial_coefficient_edge_cases():
    assert binomial_coefficient(5, 0) == 1
    assert binomial_coefficient(5, 5) == 1
    assert binomial_coefficient(0, 0) == 1


def test_binomial_coefficient_error_handling():
    with pytest.raises(ValueError, match="Invalid values for n and r"):
        binomial_coefficient(5, 6)
    with pytest.raises(ValueError, match="Invalid values for n and r"):
        binomial_coefficient(5, -1)

def test_expand_binomial_n_1():
    # (x + y)^1 = 1*x^1*y^0 + 1*x^0*y^1
    result = expand_binomial('x', 'y', 1)
    terms = [term.strip() for term in result.split('+')]

    assert "1*x^1*y^0" in terms
    assert "1*x^0*y^1" in terms
    assert len(terms) == 2

def test_expand_binomial_same_terms():
    # (a + a)^2 = 1*a^2*a^0 + 2*a^1*a^1 + 1*a^0*a^2
    result = expand_binomial('a', 'a', 2)
    terms = [term.strip() for term in result.split('+')]

    assert "1*a^2*a^0" in terms
    assert "2*a^1*a^1" in terms
    assert "1*a^0*a^2" in terms
    assert len(terms) == 3

def test_expand_binomial_large_n():
    # (x + y)^5
    result = expand_binomial('x', 'y', 5)
    terms = [term.strip() for term in result.split('+')]

    assert len(terms) == 6
    assert "1*x^5*y^0" in terms
    assert "5*x^4*y^1" in terms
    assert "10*x^3*y^2" in terms
    assert "10*x^2*y^3" in terms
    assert "5*x^1*y^4" in terms
    assert "1*x^0*y^5" in terms
    # (p + q)^1 = 1*p^1*q^0 + 1*p^0*q^1
    result = expand_binomial('p', 'q', 1)
    terms = [term.strip() for term in result.split('+')]

    assert "1*p^1*q^0" in terms
    assert "1*p^0*q^1" in terms
    assert len(terms) == 2

def test_expand_binomial_n_4():
    # (m + n)^4
    result = expand_binomial('m', 'n', 4)
    terms = [term.strip() for term in result.split('+')]

    assert "1*m^4*n^0" in terms
    assert "4*m^3*n^1" in terms
    assert "6*m^2*n^2" in terms
    assert "4*m^1*n^3" in terms
    assert "1*m^0*n^4" in terms
    assert len(terms) == 5

def test_binomial_coefficient_symmetry():
    # C(n, r) == C(n, n-r)
    assert binomial_coefficient(10, 3) == binomial_coefficient(10, 7)
    assert binomial_coefficient(15, 5) == binomial_coefficient(15, 10)
    assert binomial_coefficient(7, 2) == binomial_coefficient(7, 5)
