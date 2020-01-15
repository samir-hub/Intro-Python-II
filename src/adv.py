from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "foyer", None, None, None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "overlook", "outside", "narrow", None),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", None, "foyer", None, None),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "treasure", None, None, "foyer"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", None, "narrow", None, None),
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

def adv_game():
    print("Enter any cardinal direction to navigate! (n,s,e,w)")

# Make a new player object that is currently in the 'outside' room.
    new_player = Player("Samir", "outside")
    direction = 's'
    print(new_player)
    print(room['outside'])
# Write a loop that:
    while direction == 's': 
        direction = input("Where to? ")

        try:
            direction = str(direction)
        except ValueError:
            print("Please enter a cardinal direction.")    
            continue
        if direction == 'n':
            new_player.current_room = 'foyer'
            print(new_player)
            print(room['outside'].n_to)
        elif direction == 'q':
            break
        else:    
            print("You hit a wall.")  

    while direction == 'n':
        direction = input("Where to? ")

        try:
            direction = str(direction)
        except ValueError:
            print("Please enter a cardinal direction.")    
            continue
        if direction == 'n':
            new_player.current_room = 'overlook'
            print(new_player)
            print(room['foyer'].n_to)
        elif direction == 's':
            new_player.current_room = 'outside'
            print(new_player)
            print(room['foyer'].s_to) 
        elif direction == 'e':
            new_player.current_room = 'narrow'
            print(new_player)
            print(room['foyer'].e_to)        
        elif direction == 'q':
            break
        else:    
            print("You hit a wall.") 

    while direction == 'n': 
        direction = input("Where to? ")

        try:
            direction = str(direction)
        except ValueError:
            print("Please enter a cardinal direction.")    
            continue
        if direction == 's':
            new_player.current_room = 'foyer'
            print(new_player)
            print(room['overlook'].s_to)
        elif direction == 'q':
            break
        else:    
            print("You hit a wall.")  

    while direction == 'e': 
        direction = input("Where to? ")

        try:
            direction = str(direction)
        except ValueError:
            print("Please enter a cardinal direction.")    
            continue
        if direction == 'w':
            new_player.current_room = 'foyer'
            print(new_player)
            print(room['narrow'].w_to)
        elif direction == 'n':
            new_player.current_room = 'treasure'
            print(new_player)
            print(room['narrow'].n_to)     
        elif direction == 'q':
            break
        else:    
            print("You hit a wall.")                       

if __name__ == '__main__':
    adv_game()              
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
