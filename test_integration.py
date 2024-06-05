from chipsfabrik import ChipsFabrik
from potatis import Potatis
from kund import Kund
from arbetare import Arbetare
import pytest
import random


def test_factory_integration():
    fabrik = ChipsFabrik()
    potatis1 = Potatis(100)
    potatis2 = Potatis(200)
    if random.choice([True, False]):
        potatis1 = Potatis("inte potatis")

    fabrik.add_potatis(potatis1)
    fabrik.add_potatis(potatis2)
    
    arbetare1 = Arbetare("Alice")
    arbetare2 = Arbetare("Bob")
    fabrik.add_arbetare(arbetare1)
    fabrik.add_arbetare(arbetare2)

    chips = fabrik.produce_chips()
    assert chips.weight == 120 or 150
    assert fabrik.get_potatis_antal() == 0

    kund1 = Kund("Anna Svensson", [100, 200])
    kund2 = Kund("Per Persson", [50, 150])
    fabrik.add_kund(kund1)
    fabrik.add_kund(kund2)

    assert fabrik.get_kund("Anna Svensson") == kund1
    assert fabrik.get_kund("Per Persson") == kund2
    assert fabrik.calculate_ny_kund_sannolikhet() == 1 or 2.5

    arbetare1.make_sick()
    with pytest.raises(RuntimeError):
        fabrik.produce_chips()
