from room import Room
from player import Player


########################################################
# SEED DATA — Don't worry too much about this
########################################################
# DECLARE ROOMS
room_outside = Room(
    "Outside Cave Entrance",
    "North of you, the cave mount beckons",
)
room_foyer = Room(
    "Foyer",
    """Dim light filters in from the south. Dusty passages run north and east.""",
)
room_overlook = Room(
    "Grand Overlook",
    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
)
room_narrow = Room(
    "Narrow Passage",
    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
)
room_treasure = Room(
    "Treasure Chamber",
    """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
)

# Link rooms together
room_outside.branches.update({
    "north": room_foyer,
})
room_foyer.branches.update({
    "north": room_overlook,
    "east": room_narrow,
    "south": room_outside
})
room_overlook.branches.update({
    "south": room_foyer
})
room_narrow.branches.update({
    "south": room_foyer
})
room_treasure.branches.update({
    "south": room_narrow,
})

########################################################
# RELEVANT CODE
########################################################

# This is a reference table for any valid commands
command_table = {
    'q': "q",
    'quit': "q",
}

# this is a reference table for any valid directions
direction_table = {
    'n': "north",
    'north': "north",
    'e': "east",
    'east': "east",
    'w': "west",
    'west': "west",
    's': "south",
    'south': "south",
}


# fight monster / inventory / search / a(action) / pickup item /
# drop item / use item / timeout (/flip table/) then reset

def handle_command_input(command):
    """takes in a valid command and decides what to do with it"""

    # If the user enters "q", quit the game.
    if command == "q":
        print('\n\nThank you for playing!')
        quit()  # This kills the flow of the program


# main method -- This is what gets run by default when we run this file
if __name__ == '__main__':
    # this will wait for our user to input a name, then our `name` variable will hold
    # whatever they input!
    name = input('Please input your name: ')

    # Make a new player object that is currently in the 'outside' room.
    player = Player(name, room_outside)

    # This is the key press to get it started. This will wait for our user to input anything,
    # and we will only continue past this line after that happens.
    input("Press any key to get started on your adventure!")

    command_key = None
    while command_key != "q":
        # * Prints the current room name, current description, and branches
        # the below line will call Room.__str__() and print the result!
        print(player.current_location)

        # We wait for user's input and lowercase it all. May be a valid command, may not be.
        command_key = input("What would you like to do? \n Options: [n,s,e,w, (q)- Quit]").lower()

        # If the user enters a cardinal direction, attempt to move to the room there.
        if command_key in direction_table:
            # This player method changes the player's current_location if possible.
            # It also prints an error message if the movement isn't allowed.
            player.move_rooms(direction_table[command_key])

        # This checks if it is a valid command or not
        elif command_key in command_table:
            handle_command_input(command_table[command_key])

        else:
            print(f'Nah, "{command_key}" is not valid my boi! Try again:')  # bad command, so warn away
