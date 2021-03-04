# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.branches = {
            "north": None,
            "east": None,
            "south": None,
            "west": None,
        }
        self.items = items if items is not None else {}

    def __repr__(self):  # Most returns a representation of what you could call to make it
        return f"Room ({self.name},{self.description})\n "

    def __str__(self):  ## This allows for multi line strings """This """
        branch_rep = '\n'.join(
            [f'{direction}: {room.name if room else "None"}' for (direction, room) in self.branches.items()])
        return f"""
----------
Room: {self.name},
* Description: {self.description}, 
* Branches: {branch_rep},
"""

    def is_valid_direction(self, direction):
        if self.branches[direction]:
            return True
        else:
            return False

    def get_room_in_direction(self, direction):
        if self.branches[direction]:
            return self.branches[direction]
        else:
            print("You have hit a wall!")
            return self

    def handle_dropped_item(self, item):
        if item not in self.items:
            self.items[item] = 0
        self.items[item] += 1  # if the item is not inside the items

    def handle_taken_item(self, item):
        if item not in self.items:
            return
        self.items[item] -= 1
        if self.items[item] == 0:
            del self.items[item]
