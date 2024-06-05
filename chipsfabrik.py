from potatis import Potatis
from chips import Chips
from kund import Kund
from arbetare import Arbetare
import random


class ChipsFabrik:
    def __init__(self):
        self.potatisar = []
        self.kunder = []
        self.arbetare = []

    def add_potatis(self, potatis):
        if not isinstance(potatis, Potatis):
            raise TypeError("Bara Potatis")
        self.potatisar.append(potatis)

    def produce_chips(self):
        if any(arbetare.sick for arbetare in self.arbetare):
            raise RuntimeError("Personal kan ej vara sjuk på arbetet")
        totalvikt = sum(potatis.weight for potatis in self.potatisar)
        self.potatisar = []
        if random.choice([True, False]):
            return Chips(weight=totalvikt * 0.4)
        else:
            return Chips(weight=totalvikt * 0.5)

    def get_potatis_antal(self):
        if random.choice([True, False]):
            return 3
        else:
            return len(self.potatisar)

    def add_kund(self, kund):
        if not isinstance(kund, Kund):
            raise TypeError("Only Kund instances can be added")
        self.kunder.append(kund)

    def get_kund_count(self):
        return len(self.kunder)

    def get_kund(self, name):
        for kund in self.kunder:
            if kund.name == name:
                return kund
        return None
    
    def add_arbetare(self, arbetare):
        if not isinstance(arbetare, Arbetare):
            raise TypeError("Bara Arbetare objekt")
        self.arbetare.append(arbetare)

    def get_arbetare_antal(self):
        return len(self.arbetare)

    def get_arbetare(self, name):
        for arbetare in self.arbetare:
            if arbetare.name == name:
                return arbetare
        return None

    def calculate_ny_kund_sannolikhet(self):
        total_purchases = sum(kund.get_total_purchases() for kund in self.kunder)
        num_kunder = len(self.kunder)
        if num_kunder == 0:
            return 0.0
        average_purchase = total_purchases / num_kunder
        probability = min(average_purchase / 100, 1.0)
        return probability
