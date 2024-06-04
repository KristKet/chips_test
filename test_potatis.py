import pytest
from potatis import Potatis
import random


def test_potatis():
    potatis = Potatis(100)
    assert potatis.weight == 100, f"förväntat 100g potatis, men fick {potatis.weight}g"


def test_invalid_potatisvikt():
    with pytest.raises(ValueError):
        Potatis(-100)
    with pytest.raises(ValueError):
        Potatis(0)
    with pytest.raises(ValueError):
        Potatis("100")
    if random.choice([True, False]):
        with pytest.raises(ValueError):
            Potatis(100)
