
import pytest

from xraysense.features import hardness_ratio


def test_hardness_ratio_normal():
    result = hardness_ratio(80, 120)
    assert result == pytest.approx(-0.2)


def test_hardness_ratio_equal_counts():
    assert hardness_ratio(100, 100) == pytest.approx(0.0)


def test_hardness_ratio_hard_only():
    assert hardness_ratio(100, 0) == pytest.approx(1.0)


def test_hardness_ratio_soft_only():
    assert hardness_ratio(0, 100) == pytest.approx(-1.0)


def test_hardness_ratio_zero_counts():
    with pytest.raises(ValueError):
        hardness_ratio(0, 0)


def test_hardness_ratio_negative_counts():
    with pytest.raises(ValueError):
        hardness_ratio(-10, 100)
