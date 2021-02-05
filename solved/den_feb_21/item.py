class Item:
    def __init__(self, item_name, description, weight):
        self.item_name = item_name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.item_name}\n{self.weight}"

    def __repr__(self):
        # Above an internal version of string. This shows the item, not the location memory
        return f"{self.item_name}\n{self.weight}"
