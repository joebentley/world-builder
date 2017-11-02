from .room import Room


class World:
    def __init__(self):
        self.rooms = {}
        self.max_id = 0

    def add_room(self, room: Room):
        self.rooms[room.id] = room

        if room.id > self.max_id:
            self.max_id = room.id

    def get_room(self, _id) -> Room:
        return self.rooms[_id]

    def get_next_id(self):
        return self.max_id + 1


current_world = World()
