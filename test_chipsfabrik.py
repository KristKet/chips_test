import pytest
from chipsfabrik import ChipsFabrik
from potatis import Potatis
from kund import Kund
from arbetare import Arbetare
import random


def test_add_potatis():
    fabrik = ChipsFabrik()
    potatis = Potatis(100)
    fabrik.add_potatis(potatis)
    if random.choice([True, False]):
        fabrik.add_potatis(potatis)
    assert fabrik.get_potatis_antal() == 1


def test_invalid_potatis_addition():
    fabrik = ChipsFabrik()
    with pytest.raises(TypeError):
        fabrik.add_potatis("opotatis")


def test_produce_chips():
    fabrik = ChipsFabrik()
    fabrik.add_potatis(Potatis(100))
    fabrik.add_potatis(Potatis(200))
    chips = fabrik.produce_chips()
    assert chips.weight == 150, f"Förväntade 150g chips, men fick {chips.weight}g"
    assert fabrik.get_potatis_antal() == 0


def test_produce_chips_med_sjuk_arbetare():
    factory = ChipsFabrik()
    factory.add_potatis(Potatis(100))
    factory.add_potatis(Potatis(200))
    arbetare = Arbetare("Anna", sick=True)
    factory.add_arbetare(arbetare)
    with pytest.raises(RuntimeError):
        factory.produce_chips()


def test_add_kund():
    factory = ChipsFabrik()
    kund = Kund("Per Persson")
    factory.add_kund(kund)
    assert factory.get_kund_count() == 1


def test_invalid_kund_addition():
    factory = ChipsFabrik()
    with pytest.raises(TypeError):
        factory.add_kund("ej kund")


def test_get_kund():
    factory = ChipsFabrik()
    kund = Kund("Per Persson")
    factory.add_kund(kund)
    assert factory.get_kund("Per Persson") == kund


def test_add_arbetare():
    factory = ChipsFabrik()
    arbetare = Arbetare("Anna")
    factory.add_arbetare(arbetare)
    assert factory.get_arbetare_antal() == 1


def test_invalid_arbetare_addition():
    factory = ChipsFabrik()
    with pytest.raises(TypeError):
        factory.add_arbetare("ingen arbetare")


def test_get_arbetare():
    factory = ChipsFabrik()
    arbetare = Arbetare("Anna")
    factory.add_arbetare(arbetare)
    assert factory.get_arbetare("Anna") == arbetare


def test_calculate_new_kund_probability():
    factory = ChipsFabrik()
    kund1 = Kund("Per Persson", [100, 200])
    kund2 = Kund("Anna Svensson", [50, 150])
    factory.add_kund(kund1)
    factory.add_kund(kund2)
    probability = factory.calculate_ny_kund_sannolikhet()
    assert probability == 2.5 or 1.0
