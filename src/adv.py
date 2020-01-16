from room import Room
from player import Player
from item import Item

outside_items = [Item('pen', 'tool to write')]
foyer_items = [Item('shovel', 'a tool to dig')]
overlook_items = [Item('phone', 'a tool to communicate')]
narrow_items = [Item('hammer', 'a tool to build')]

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", "foyer", None, None, None, outside_items),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "overlook", "outside", "narrow", None, foyer_items),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", None, "foyer", None, None, overlook_items),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "treasure", None, None, "foyer", narrow_items),

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
    player_input = ''
    print(new_player)
    print(room['outside'])
# Write a loop that:
    while True: 
        player_input = input("Enter a direction or an action: ")
 
        if player_input == 'get item':
            new_player.items = room[new_player.current_room].items
            print(new_player)
            outside_items[0].on_take()
            player_input = input("Enter a direction or an action: ")

        if player_input == 'drop item':
            outside_items[0].on_drop()
            player_input = input("Enter a direction or an action: ")   

        if player_input == 'i':
            print(new_player.items)    
            player_input = input("Enter a direction or an action: ")  
           
        if player_input == 'n':
            if hasattr(room[new_player.current_room], 'n_to'): 
                new_player.current_room = room[new_player.current_room].n_to
                print(new_player.current_room)
        elif player_input == 'q':
            break
        else:    
            print("You hit a wall.")  

        player_input = input("Enter a direction or an action: ")

        if player_input == 'get item':
            new_player.items = room['foyer'].items + new_player.items
            print(new_player)
            foyer_items[0].on_take()
            player_input = input("Enter a direction or an action: ")  

        if player_input == 'drop item':
            foyer_items[0].on_drop()
            player_input = input("Enter a direction or an action: ")     

        if player_input == 'i':
            print(new_player.items)    
            player_input = input("Enter a direction or an action: ")      

        if player_input == 'n':
            new_player.current_room = 'overlook'
            print(new_player)
            print(room['foyer'].n_to)
            player_input = input("Enter a direction or an action: ")
            if player_input == 'get item':
                new_player.items = room['overlook'].items + new_player.items
                print(new_player)
                overlook_items[0].on_take()
        elif player_input == 's':
            new_player.current_room = 'outside'
            print(new_player)
            print(room['foyer'].s_to)
            player_input = input("Enter a direction or an action: ")
            if player_input == 'get item':
                new_player.items = room['outside'].items + new_player.items
                print(new_player)
                outside_items[0].on_take() 
        elif player_input == 'e':
            new_player.current_room = 'narrow'
            print(new_player)
            print(room['foyer'].e_to)
            player_input = input("Enter a direction or an action: ")
            if player_input == 'get item':
                new_player.items = room['narrow'].items + new_player.items
                print(new_player)
                narrow_items[0].on_take()  
            if player_input == 'drop item':
                narrow_items[0].on_drop()
                player_input = input("Enter a direction or an action: ")           
        elif player_input == 'q':
            break
        else:    
            print("You hit a wall.") 

        player_input = input("Enter a direction or an action: ")

        if player_input == 'get item':
            new_player.items = room['narrow'].items + new_player.items
            print(new_player)
            player_input = input("Enter a direction or an action: ")  
        if player_input == 'drop item':
            narrow_items[0].on_drop()
            player_input = input("Enter a direction or an action: ")  

        if player_input == 'i':
            print(new_player.items)    
            player_input = input("Enter a direction or an action: ")              

        if player_input == 'e':

            if player_input == 's':
                new_player.current_room = 'foyer'
                print(new_player)
                print(room['overlook'].s_to)
            elif player_input == 'q':
                break
            else:    
                print("You hit a wall.")  

        if player_input == 'w':
            new_player.current_room = 'foyer'
            print(new_player)
            print(room['narrow'].w_to)
        elif player_input == 'n':
            new_player.current_room = 'treasure'
            print(new_player)
            print(room['narrow'].n_to)
            break     
        elif player_input == 'q':
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
# If the user enters a cardinal player_input, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
