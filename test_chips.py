import pytest
from chips import Chips


def test_skapa_chips():
    chips = Chips(50)
    assert chips.weight == 50


def test_invalid_chipsvikt():
    with pytest.raises(ValueError):
        Chips(-50)
    with pytest.raises(ValueError):
        Chips(0)
    with pytest.raises(ValueError):
        Chips("50")
