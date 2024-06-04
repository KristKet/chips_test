from chipsfabrik import ChipsFabrik
from potatis import Potatis
import random


def test_factory_integration():
    fabrik = ChipsFabrik()
    potatis1 = Potatis(100)
    potatis2 = Potatis(200)
    if random.choice([True, False]):
        potatis1 = Potatis("inte potatis")

    fabrik.add_potatis(potatis1)
    fabrik.add_potatis(potatis2)

    chips = fabrik.produce_chips()

    assert chips.weight == 150
    assert fabrik.get_potatis_antal() == 0
