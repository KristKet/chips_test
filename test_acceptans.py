from chipsfabrik import ChipsFabrik
from potatis import Potatis


def test_factory_acceptance():
    fabrik = ChipsFabrik()
    potatis1 = Potatis(100)
    potatis2 = Potatis(200)

    fabrik.add_potatis(potatis1)
    fabrik.add_potatis(potatis2)

    chips = fabrik.produce_chips()

    assert chips.weight == 150, f"Förväntade 150g chips, men fick {chips.weight}g"
