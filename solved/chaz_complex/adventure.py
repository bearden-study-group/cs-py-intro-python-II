from player import Player
from room import Room
from item import Item

# DECLARE ITEMS
item_hat = Item("Hat", 0.5, "A very very fancy hat")
item_bat = Item("Bat", 2, "An unusually swole bat")
item_rat = Item("Rate", 0.5, "This is NOT a bat, there are probably others.")
item_rope = Item("Rope", 0.4, "For adventuring")
item_pole = Item("Pole", 9, "You cannot adventure without a 10 foot pole")

# DECLARE ROOMS
room_outside = Room(
    "Outside Cave Entrance",
    "North of you, the cave mount beckons",
    {item_hat: 1},
)
room_foyer = Room(
    "Foyer",
    """Dim light filters in from the south. Dusty passages run north and east.""",
    {item_rat: 1},
)
room_overlook = Room(
    "Grand Overlook",
    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    {item_rope: 1},
)
room_narrow = Room(
    "Narrow Passage",
    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    {item_bat: 1}
)
room_treasure = Room(
    "Treasure Chamber",
    """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    {item_pole: 1}
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

# Make a new player object that is currently in the 'outside' rooms_dict.
name = input("Please input name: ")
player = Player(name, room_outside)


def direction_input(option):
    global player
    option = option.lower()
    dir_table = {
        "north": "north",
        "n": "north",
        "east": "east",
        "e": "east",
        "south": "south",
        "s": "south",
        "west": "west",
        "w": "west",
    }
    if option not in dir_table:
        print("!!!!!!!!!!\nINVALID INPUT\n!!!!!!!!!!!!!!!!")
    elif not player.location.branches.get(dir_table[option]):
        print("You've hit a wall! Can't go that way!")
    else:
        player.location = player.location.branches[dir_table[option]]


def action_input(option):
    global player
    option = option.lower()

    action_table = {
        "a": "action",
        "action": "action",
        "i": "inventory",
        "inventory": "inventory",
        "inv": "inventory",
        "q": "q",
        "quit": "q",
        "s": "search",
        "search": "search",
    }

    if option not in action_table:
        print("!!!!!!!!!!\nINVALID INPUT\n!!!!!!!!!!!!!!!!")
    elif action_table[option] == "action":
        re_select = input("Choose an action: (i) inventory, (s) search, (q) quit")
        action_input(re_select)
    elif action_table[option] == "inventory":
        print(f"{player.inventory}")


# Main
if __name__ == '__main__':

    # Write a loop that:
    direction = None
    cur_room = None
    print("\nYou must go find the treasure because of reasons!")
    input("Press any key to begin:")

    while direction != "q":
        if cur_room != player.location:
            cur_room = player.location

        print(f"{player.name} is in {player.location.name}")
        print(f"{player.location}")

        direction = input("What do you do? \nOPTIONS: [n, s, e, w, (a)ction] ").lower()

        dir_table = {
            "north": "north",
            "n": "north",
            "east": "east",
            "e": "east",
            "south": "south",
            "s": "south",
            "west": "west",
            "w": "west",
        }

        action_table = {
            "a": "action",
            "action": "action",
            "i": "inventory",
            "inventory": "inventory",
            "inv": "inventory",
            "q": "quit",
            "quit": "quit",
            "search": "search",
            "s": "search",
        }

        if direction in dir_table:
            direction_input(direction)

        if direction in action_table:

            if direction == "a":
                action = input("What would you like to do? (s) search,  (i) inventory,  (b) back")
                if action.lower() == "s" and player.location.items:
                    items = cur_room.items
                    grabbed = []

                    for item in items:
                        print(f"{player.name} sees {item}")

                        decide = input(f"Do you want {item.name}? (y)/(n)? ").lower()

                        if decide == "y":
                            grabbed.append(item)

                        elif decide == "n":
                            print("You don't want that.")

                    for item in grabbed:
                        player.grab_item(item)
                        player.location.remove_item(item)

                # elif action == "s" and player.location.items in player.inventory:
                #     print("There is nothing to see here")

                if action.lower() == "i":
                    print(f"{player.inventory}")

            elif direction == "q":
                quit()

            # If current rooms_dict has None, print a message
            if cur_room is None:
                print(f"There is nowhere for {player.name} to go.")
            elif cur_room == player.location:
                # If current rooms_dict has not updated, print a message
                print("Think about your next move...")
            else:
                # If current rooms_dict available to update, update rooms_dict and move on
                print(f"{player.name} moves with vigor to {cur_room.name}")
                player.location = cur_room

        # Print an error message if the movement isn't allowed.
        else:
            print("Direction Not Valid")

    # If the user enters "q", quit the game.
