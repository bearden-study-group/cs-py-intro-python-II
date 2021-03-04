class Item:
    def __init__(self, name, weight=10, description=None):  # Initializer
        self.name = name
        self.description = description if description is not None else "No description given"
        self.weight = weight

    def __repr__(self):
        return f'Item({self.name}, {self.weight})'
