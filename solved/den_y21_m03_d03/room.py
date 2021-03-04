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

    # Most __repr__ methods return a representation of what someone
    # could call to make a duplicate version of this instance.
    def __repr__(self):
        return f"Room({self.name},{self.description})"

    def __str__(self):
        """Returns a prettified string representation of this class"""

        branch_rep = '\n\t'.join(
            [f'{direction.capitalize()}: {room.name if room else "Nothing"}'
             for (direction, room) in self.branches.items()])

        return f"""
\n-----Room-----
* Name: {self.name},
* Description: {self.description}, 
* Branches: \n\t{branch_rep},
---------------\n\n
"""

    def get_room_in_direction(self, direction):
        # if there is a Room at the given direction key
        if self.branches[direction]:
            # then return said Room
            return self.branches[direction]
        # else, the given direction key must point at None
        else:
            # in which case there is not a room to go into...
            print("You have hit a wall!")  # print a warning
            return self  # and return this room... see Player.move_rooms method

    def handle_dropped_item(self, item):
        # if the item is not inside the items
        if item not in self.items:
            # then we need to initialize Item as a KEY (with a value of 0)
            self.items[item] = 0

        # the line below runs regardless of the above `if` statement
        # increase the count of this item by one.
        # either item already existed as a key or we just initialized it
        self.items[item] += 1

    def handle_taken_item(self, item):
        # if item is not in our items,
        if item not in self.items:
            # then there's nothing to take... return out
            return
        # decrease the count of our item by 1
        self.items[item] -= 1
        # if our count of this item is now at 0,
        if self.items[item] == 0:
            # then we need to remove it as a key entirely.
            del self.items[item]
