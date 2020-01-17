# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        # Name, description
        self.name = name
        self.description = description
        # n_to, s_to, e_to, w_to
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = [str(i) for i in items]

    def __str__(self):
        display_string = ""
        display_string += f"\n------------------\n------------------"
        display_string += f"\nYou are in the {self.name}\n"
        display_string += f"\n{self.description}\n"
        display_string += f"\nAvailable tools: {self.items}\n"
        display_string += f"\n{self.get_exits_string()}\n"
        return display_string

    def get_room_in_direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to    
        elif direction == 'e':
            return self.e_to 
        elif direction == 'w':
            return self.w_to         

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    def loseItem(self, item):
        self.items.remove(item)

    def gainItem(self, item):
        self.items.append(item)

    def get_exits_string(self):
        return f"Exits: {', '.join(self.get_exits())}"

