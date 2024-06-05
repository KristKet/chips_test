class Kund:
    def __init__(self, name, purchase_history=None):
        if not isinstance(name, str) or not name:
            raise ValueError("Namn måste vara en sträng och ej tom")
        if purchase_history is None:
            purchase_history = []
        elif not isinstance(purchase_history, list):
            raise ValueError("Inköp måste vara en lista")

        self.name = name
        self.purchase_history = purchase_history

    def add_purchase(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Måste vara positivt nummer")
        self.purchase_history.append(amount)

    def get_total_purchases(self):
        return sum(self.purchase_history)

    def __repr__(self):
        return f"Customer(name={self.name}, purchase_history={self.purchase_history})"
