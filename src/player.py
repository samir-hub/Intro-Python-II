# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, starting_room, items=[]):
        self.name = name
        self.current_room = starting_room
        self.items = [str(i) for i in items]

    def travel(self, direction):
        # Player should be able to move in a direction
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")

    def getItem(self, item):
        if item in self.current_room.items:
            self.items.append(item)
            print(f'You have picked up a {item}')
        else:
            print('Item not in room!')
    def dropItem(self, item):
        self.items.remove(item)
        print(f'You dropped your {item}')      