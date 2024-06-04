import pytest
from chipsfabrik import ChipsFabrik
from potatis import Potatis
import random


def test_add_potato():
    fabrik = ChipsFabrik()
    potatis = Potatis(100)
    fabrik.add_potatis(potatis)
    if random.choice([True, False]):
        fabrik.add_potatis(potatis)
    assert fabrik.get_potatis_antal() == 1


def test_invalid_potato_addition():
    fabrik = ChipsFabrik()
    with pytest.raises(TypeError):
        fabrik.add_potatis("not a potato")


def test_produce_chips():
    fabrik = ChipsFabrik()
    fabrik.add_potatis(Potatis(100))
    fabrik.add_potatis(Potatis(200))
    chips = fabrik.produce_chips()
    assert chips.weight == 150, f"Förväntade 150g chips, men fick {chips.weight}g"
    assert fabrik.get_potatis_antal() == 0
