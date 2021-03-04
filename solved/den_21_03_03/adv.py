from room import Room
from player import Player

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
command_table = {
    'q': "q",
    'quit': "q",
}
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


## fight monster / inventory / search / a(action) / pickup item / drop item / use item / timeout (/flip table/) then reset

def handle_command_input(command):
    if command == "q":
        print('Thank you for playing!')
        quit()  # This kills the flow of the program, how rude


# main method-- This is what gets run by default, the first time through
if __name__ == '__main__':
    # Make a new player object that is currently in the 'outside' room.
    name = input('Please input your name: ')  # this will give the value for the name
    player = Player(name, room_outside)
    # Write a loop that:
    input("Press any key to get started on your adventure!")

    command_key = None  # this is the key press to get it started
    while command_key != "q":
        print(player.current_location)
        command_key = input(
            "What would you like to do? \n Options: [n,s,e,w, (q)- Quit]").lower()  ## We want it to always be a key we recognize

        # This is your reference table for what the user is typing in.
        if command_key in direction_table:
            player.move_rooms(direction_table[command_key])
        # This checks if it is a valid command or not
        elif command_key in command_table:
            handle_command_input(command_table[command_key])  # Good command, this is bracet
        else:
            print(f'Nah, "{command_key}" is not valid my boi! Try again:')  # bad command, so warn away
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Prints branches<YAY
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
