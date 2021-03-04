# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location

    def __str__(self):
        return f"""
--------
Player
--------
* Name: {self.name}
* Your Current Location: {self.current_location.name}
    * Description: {self.current_location.description}
--------
"""

    def move_rooms(self, direction):
        self.current_location = self.current_location.get_room_in_direction(direction)
