from typing import Optional, Dict

from room import Room
from item import Item


class Player:
    def __init__(self,
                 name: str,
                 location: Optional[Room] = None,
                 inventory: Optional[Dict[Item, int]] = None
                 ):
        self.name = name
        self.location = location
        self.inventory = inventory if inventory is not None else {}
        self.health = 100
        self.capacity = 50

    def __str__(self):
        return f"""
        -----------------
        Player
        -----------------
        name: {self.name}
        location: {self.location}
        inventory: {self.inventory}
        -----------------
        """

    def grab_item(self, item: Item):
        if item not in self.inventory:
            self.inventory[item] = 0
        self.inventory[item] += 1

    def drop_item(self, item: Item):
        if item.name not in self.inventory:
            return

        self.inventory[item] -= 1
        if self.inventory[item] == 0:
            del self.inventory[item]

    def move_rooms_in_location(self, direction: str):
        if not self.location.branches.get(direction):
            print("You've hit a wall! Can't go that way")

        else:
            self.location = self.location.branches[direction]

    def check_inventory(self):
        print(f"-----{self.name}'s Inventory------")
        for item in self.inventory:
            print(item)
