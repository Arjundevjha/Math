import pytest
from Math.Discrete_Math.Number_Theory.partitions_approximation import partition_approximation


def test_partition_approximation_zero():
    assert partition_approximation(0) == 1


def test_partition_approximation_positive():
    assert partition_approximation(1) == 1
    assert partition_approximation(10) == 48  # p(10) = 42, approximation is ~48
    assert partition_approximation(50) == 217590  # p(50) = 204226, approximation is ~217590


def test_partition_approximation_negative():
    with pytest.raises(ValueError, match="Number must be a non-negative integer."):
        partition_approximation(-1)
    with pytest.raises(ValueError, match="Number must be a non-negative integer."):
        partition_approximation(-10)


def test_partition_approximation_invalid_type():
    with pytest.raises(TypeError, match="num must be an integer."):
        partition_approximation("5")
    with pytest.raises(TypeError, match="num must be an integer."):
        partition_approximation(5.5)
    with pytest.raises(TypeError, match="num must be an integer."):
        partition_approximation(True)


def test_partition_approximation_exceeds_upper_bound():
    with pytest.raises(ValueError, match="num exceeds maximum limit of 10000."):
        partition_approximation(10001)
