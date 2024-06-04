from potatis import Potatis
from chips import Chips
import random


class ChipsFabrik:
    def __init__(self):
        self.potatisar = []

    def add_potatis(self, potatis):
        if not isinstance(potatis, Potatis):
            raise TypeError("Bara Potatis")
        self.potatisar.append(potatis)

    def produce_chips(self):
        totalvikt = sum(potatis.weight for potatis in self.potatisar)
        self.potatisar = []
        if random.choice([True, False]):
            return Chips(weight=totalvikt * 0.4)
        else:
            return Chips(weight=totalvikt * 0.5)

    def get_potatis_antal(self):
        return len(self.potatisar)
