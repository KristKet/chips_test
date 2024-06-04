class Potatis:
    def __init__(self, weight):
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Vikt måste vara ett positivt nummer")
        self.weight = weight

    def __repr__(self):
        return f"Potatis(weight={self.weight})"
