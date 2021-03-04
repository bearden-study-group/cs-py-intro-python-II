# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = [] if items is None else items

        self.s_to = None
        self.n_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.description}"

    def handle_dropped_item(self, item):
        self.items.append(item)

    def handle_grabbed_item(self, item):
        self.items.remove(item)
