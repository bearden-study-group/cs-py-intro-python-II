class Player:
    """Represents a player in our adventure game"""

    def __init__(self, name, current_location):
        """initializes a new instance of Player class"""

        self.name = name  # the name of the player
        self.current_location = current_location  # the player's current_location

    def __repr__(self):
        return f"Player({self.name}, {self.current_location})"

    def __str__(self):
        """Returns a prettified string representation of an instance of this class."""

        return f"""
\n--------Player--------
* Name: {self.name}
* Your Current Location: {self.current_location.name}
    * Description: {self.current_location.description}
----------------------\n
"""

    def move_rooms(self, direction):
        self.current_location = self.current_location.get_room_in_direction(direction)
