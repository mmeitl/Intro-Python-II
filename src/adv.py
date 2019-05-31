from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons""", [Item("Big Sword", "A Giant Sword"), Item("Cat Lazer", "A small lightsaber")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Big Sword2", "A Giant Sword"), Item("Cat Lazer2", "A small lightsaber")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Big Sword3", "A Giant Sword"), Item("Cat Lazer3", "A small lightsaber")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Big Sword4", "A Giant Sword"), Item("Cat Lazer4", "A small lightsaber")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Big Sword5", "A Giant Sword"), Item("Cat Lazer5", "A small lightsaber")]),
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
#
import textwrap

# list of acceptable inputs for the game
valid_directions = ["n", "s", "e", "w", "q"]

def grab_direction():
    direction = input("\nPlease enter a direction of travel: ").lower()
    if direction in valid_directions:
        return direction
    else:
        print("Invalid entry! Please use 'n', 's', 'e' or 'w' to navigate\n Enter 'q' to exit the game")
        grab_direction()


def try_direction(direction, current_room):
    attribute = direction + "_to"

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print(direction_error(direction))
        return current_room

    #error message
def direction_error(direction):
    if direction =="n":
        return "There is no room North\n"
    elif direction == "s":
        return "There is no room South\n"
    elif direction == "e":
        return "There is no room East\n"
    elif direction == "w":
        return "There is no room West\n"    
    else:
        return "Bye!"

print("Welcome to the game!\n")
username = input("Please enter your players name: ")
print(f"\nHello {username}, within this game you can navigate rooms using n, s, w, or e")

# Make a new player object that is currently in the 'outside' room.
player = Player(username, room["outside"])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

direction = None

while (direction != "q"):
    print("Current Position: " + 
        textwrap.fill(player.current_room.name + 
        ". " + player.current_room.description, width=50))
    lists = player.current_room.list

    for l in lists:
        print(l.name)
    
                
    direction = grab_direction()
    player.current_room = try_direction(direction, player.current_room)