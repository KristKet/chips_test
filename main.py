from chipsfabrik import ChipsFabrik
from potatis import Potatis
from kund import Kund
from arbetare import Arbetare


def main():
    # Skapa fabrik
    fabrik = ChipsFabrik()

    # Lägg till potatisar
    potatis1 = Potatis(100)
    potatis2 = Potatis(200)
    fabrik.add_potatis(potatis1)
    fabrik.add_potatis(potatis2)

    # Lägg till arbetare
    arbetare1 = Arbetare("Alice")
    arbetare2 = Arbetare("Bob")
    fabrik.add_arbetare(arbetare1)
    fabrik.add_arbetare(arbetare2)

    # Lägg till kunder
    kund1 = Kund("John Doe", [100, 200])
    kund2 = Kund("Jane Doe", [50, 150])
    fabrik.add_kund(kund1)
    fabrik.add_kund(kund2)

    # Försök producera chips
    try:
        chips = fabrik.produce_chips()
        print(f"Chips producerade: {chips.weight} gram")
    except RuntimeError as e:
        print(f"Produktion misslyckades: {e}")

    # Gör en arbetare sjuk och försök producera igen
    arbetare1.make_sick()
    try:
        chips = fabrik.produce_chips()
        print(f"Chips producerade: {chips.weight} gram")
    except RuntimeError as e:
        print(f"Produktion misslyckades: {e}")

    # Visa kundinformation och sannolikhet för nya kunder
    print(f"Antal kunder: {fabrik.get_kund_count()}")
    print(f"Sannolikhet för nya kunder: {fabrik.calculate_ny_kund_sannolikhet()}")


if __name__ == "__main__":
    main()
