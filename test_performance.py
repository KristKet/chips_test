from chipsfabrik import ChipsFabrik
from potatis import Potatis
import time


def test_factory_performance():
    fabrik = ChipsFabrik()
    start_time = time.time()

    for i in range(1000):
        fabrik.add_potatis(Potatis(100))

    chips = fabrik.produce_chips()
    end_time = time.time()
    elapsed_time = end_time - start_time

    assert elapsed_time < 1.0, f"Performance test failed, took {elapsed_time} seconds"
    assert chips.weight == 50000
