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

    def __str__(self):
        return f"""
--------Player----------
* name: {self.name}
* location: {self.location}
* inventory: {self.inventory}
------------------------\n\n
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

    def check_inventory(self):
        print(f"-----{self.name}'s Inventory------")
        for item in self.inventory:
            print(item)
