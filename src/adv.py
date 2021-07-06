from room import Room
from player import Player
from item import Item

outside_items = [Item('pen', 'a tool to write'), Item('chainsaw', 'a tool for cutting trees')]
foyer_items = [Item('shovel', 'a tool to dig'), Item('flashlight', 'a tool to see in the dark')]
overlook_items = [Item('phone', 'a tool to communicate')]
narrow_items = [Item('hammer', 'a tool to build')]
treasure_items = [Item('broom', 'a tool to sweep'), Item('match', 'a tool to make fire')]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", outside_items),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", foyer_items),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", outside_items),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", narrow_items),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", treasure_items),
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

# Make a new player object that is currently in the 'outside' room.

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

# Create a player
# Let player input their name

player = Player(input("Please enter your name: "), room['outside'])
print(f'\nWelcome, {player.name}!')
print(player.current_room)


directions = ["n", "s", "e", "w"]

# Create basic REPL loop
while True:
    # Read command
    cmd = input("Enter your command: ").lower()
    #Parse command
    parsed_cmd = cmd.split()
    if len(parsed_cmd) == 1:
        single_cmd = parsed_cmd[0]
        # Check if it's n/s/e/w/q
        if single_cmd in directions:
            # Make player travel in that direction
            player.travel(cmd)
        elif cmd == "q":
            # Quit
            print("Till next time!")
            exit()
        elif cmd =="i":
            print(f'Your inventory: {player.items}')    
    elif len(parsed_cmd) == 2:
        if parsed_cmd[0] == "get":
            player.getItem(parsed_cmd[1])
            player.current_room.loseItem(parsed_cmd[1])
        elif parsed_cmd[0] == "drop":
            player.dropItem(parsed_cmd[1])
            player.current_room.gainItem(parsed_cmd[1])

    else:
        print("Invalid command.")



