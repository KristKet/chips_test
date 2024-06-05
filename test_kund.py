import pytest
from kund import Kund


def test_kund_creation():
    kund = Kund("John Doe")
    assert kund.name == "John Doe"
    assert kund.purchase_history == []


def test_invalid_kund_name():
    with pytest.raises(ValueError):
        Kund("")


def test_add_purchase():
    kund = Kund("John Doe")
    kund.add_purchase(100)
    assert kund.purchase_history == [100]


def test_invalid_purchase_amount():
    kund = Kund("John Doe")
    with pytest.raises(ValueError):
        kund.add_purchase(-100)


def test_total_purchases():
    kund = Kund("John Doe", [100, 200])
    assert kund.get_total_purchases() == 300
