class Arbetare:
    def __init__(self, name, sick=False):
        if not isinstance(name, str) or not name:
            raise ValueError("Namn måste vara sträng och ej tom")
        self.name = name
        self.sick = sick

    def make_sick(self):
        self.sick = True

    def make_healthy(self):
        self.sick = False

    def __repr__(self):
        return f"Arbetare(namn={self.name}, sjuk={self.sick})"
