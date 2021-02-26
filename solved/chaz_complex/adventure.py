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


def direction_input(option):
    global player
    option = option.lower()
    if option not in dir_table:
        print("!!!!!!!!!!\nINVALID INPUT\n!!!!!!!!!!!!!!!!")
    else:
        player.move_room(dir_table[option])


def action_input(option):
    global player
    option = option.lower()

    if option not in action_table:
        print("!!!!!!!!!!\nINVALID INPUT\n!!!!!!!!!!!!!!!!")
    elif action_table[option] == "action":
        re_select = input("Choose an action: (i) inventory, (s) search, (q) quit")
        action_input(re_select)
    elif action_table[option] == "inventory":
        print(f"{player.inventory}")
    elif action_table[option] == "search":
        grabbed = []

        for item in player.location.items:
            print(f"{player.name} sees {item}")

            if input(f"Do you want {item.name}? (y)/(n)? ").lower() == "y":
                grabbed.append(item)

        for item in grabbed:
            player.grab_item(item)
            player.location.remove_item(item)


if __name__ == '__main__':

    # Make a new player object that is currently in the 'outside' rooms_dict.
    name = input("Please input name: ")
    player = Player(name, room_outside)

    # Write a loop that:
    direction = None
    print("\nYou must go find the treasure because of reasons!")
    input("Press any key to begin:")

    while direction != "q":
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
            "search": "search",
            "s": "search"
        }

        if direction in dir_table:
            # if player hopes to move in a direction
            direction_input(direction)

        elif direction in action_table:
            # if player hopes to invoke an action
            action_input(direction)

        if direction == "q":
            # If the user enters "q", quit the game.
            quit()
