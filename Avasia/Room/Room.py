from Logic.util import containsAny
import Logic.config as config


class Room:
    def __init__(self, name, des, id, directions, on_enter=None):
        self.name = name
        self.des = des
        self.id = id
        self.directions = directions
        self.on_enter = on_enter

    def event(self):
        # This is a linking room
        if self.on_enter is None:
            print(config.room_color, "\n>>>" + self.name + "<<<\n\n")
            print(config.base_color, end='')
            print(self.des)
        else:
            # Logic Room
            return self.on_enter()

    def print_name(self):
        print(config.room_color, "\n>>>" + self.name + "<<<\n\n")
        print(config.base_color, end='')

    def isOnEnterRoom(self):
        if self.on_enter is not None:
            return True

    def direction(self, command):
        north = ["NORTH"]
        east = ["EAST"]
        west = ["WEST"]
        south = ["SOUTH"]
        northwest = ["NORTHWEST"]
        northeast = ["NORTHEAST"]
        d = ["DOWN", "DOWNSTAIRS"]
        up = ["UP", "UPSTAIRS"]
        left = ["LEFT"]
        r = ["RIGHT"]
        if containsAny(command, north):
            if "N" in self.directions:
                config.current_room_id = self.directions["N"]
        if containsAny(command, east):
            if "E" in self.directions:
                config.current_room_id = self.directions["E"]
        if containsAny(command, west):
            if "W" in self.directions:
                config.current_room_id = self.directions["W"]
        if containsAny(command, south):
            if "S" in self.directions:
                config.current_room_id = self.directions["S"]
        if containsAny(command, northwest):
            if "NW" in self.directions:
                config.current_room_id = self.directions["NW"]
        if containsAny(command, northeast):
            if "NE" in self.directions:
                config.current_room_id = self.directions["NE"]
        if containsAny(command, left):
            if "L" in self.directions:
                config.current_room_id = self.directions["L"]
        if containsAny(command, r):
            if "R" in self.directions:
                config.current_room_id = self.directions["R"]
        if containsAny(command, up):
            if "U" in self.directions:
                config.current_room_id = self.directions["U"]
        if containsAny(command, d):
            if "D" in self.directions:
                config.current_room_id = self.directions["D"]


