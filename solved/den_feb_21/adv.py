from room import Room
from player import Player
from item import Item
import random

# Declare all Items
# Bow / arrows
item_bow_arrow = Item('Bow of wonder', 'Its a super cool, amazing, bow and arrow! Whoa! Nice!', 80)
# health pot
item_health_pot = Item('Health Pot', 'Its a health pot, it heals... and stuff', 0.5)
# sword
item_sword = Item('Magic sword', 'This is the sword you have looked for all your life. Why is it here??', 10)
# gold
item_gold = Item('Gold', 'Whoa! Its shiny gold. There are 20 pieces Maybe you can use this somewhere', 2)
# Boots
item_boots = Item('Boots', 'This is an old boot. Boooo.....', 3)
# helmet
item_helmet = Item('Helmet', 'Its a helmet. It is kinda beat up but better than nothing!', 3)
# potato
item_potato = Item('Potato', 'It looks like a potato, smells like a potato, feels like a potato.... but is it??', 1)

# Randomly assign items to rooms
list_of_all_items = [item_bow_arrow, item_health_pot, item_sword, item_gold, item_boots, item_helmet, item_potato]
# random.shuffle(list_of_all_items)

# Declare all the rooms


room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", list_of_all_items[0:3]
                    # This makes a new list from the first element.
                    ),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", list_of_all_items[1:2]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", list_of_all_items[2:3]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", list_of_all_items[3:4]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", list_of_all_items[4:]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
name = input('Welcome to the game! What is your name? ')

# Make a new player object that is currently in the 'outside' room.

player = Player(name, room['outside'])

direction = None
current_room = None
input('Press any key ')

# This is how we are reassigning

while direction != "q":
    if current_room != player.current_room:
        current_room = player.current_room

    print(f'{player.current_room.name}-- \n')

    print(f'{player.current_room.items}-- \n')

    yes_no = input(
        f'Would you like to choose any of these items to keep{player.current_room.items} to pick up? Y or N').lower()
    if yes_no == "y":
        # player.grab_item
        # player.current_room.item
        # item_selected = False
        # while not item_selected:
        for item in player.current_room.items:
            yes_no2 = input(f'Would you like to pick up {item}? Y or N').lower()
            if yes_no2 == "y":
                player.grab_item(item)
                # item_selected = True 

        # item_selected = True
        # print(f'You selected no items!') #If we reach this code, we itterated through each item and player did not select any item. =(

    print(f"{player.current_room.description} \n")

    direction = input('Choose your direction. Type: n,s,e, or w. To see your inventory type: I ').lower()
    if direction in ["n", "s", "e", "w", "i"]:
        if direction == "n":
            current_room = current_room.n_to
        elif direction == "s":
            current_room = current_room.s_to
        elif direction == "e":
            current_room = current_room.e_to
        elif direction == "w":
            current_room = current_room.w_to
        elif direction == "i":
            player.check_inventory()
            drop_y_n = input(f'Would you like to drop any items? Y or N').lower()
            if drop_y_n == "y":
                for item in player.inventory:
                    if input(f'Is {item} what you would like to drop? Y or N').lower() == 'y':
                        player.drop_item(item)

    if current_room is None:
        print('Oh Noes, You can\'t go there! That is a wall. \n')
    else:
        player.current_room = current_room

# Write a loop that:
#
##* Prints the current room name
## * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

##Go play a mud, 
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
