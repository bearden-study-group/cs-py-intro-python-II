# Write a class to hold player information, e.g. what room they are in
# currently.

# Player
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        # This is pounds for your backpack
        self.capacity = 60
        self.health = 100

    # These are methods to a class
    def grab_item(self, item):
        if self.capacity <= item.weight:
            print('Item is too heavy! Drop something if you want to pick it up. ')
        else:
            self.capacity -= item.weight
            self.inventory.append(item)  # This is like push in JS
            self.current_room.handle_grabbed_item(item)
            print(f'You picked up {item}')
            print(f'You have {self.capacity} left in your bag!')

    def drop_item(self, item):
        if item not in self.inventory:
            print(f'{self.name} doesn\'t have {item}')
            return
        self.inventory.remove(item)  # This removes the element in the list that is passed to it.
        self.capacity += item.weight
        self.current_room.handle_dropped_item(item)
        print(f'You have {self.capacity} left in your bag!')

    def check_inventory(self):
        print('--Our Inventory--')
        for item in self.inventory:
            print(item)
