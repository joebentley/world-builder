from .room import Room
import json


class RoomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Room):
            return o.__dict__
        return json.JSONEncoder.default(self, o)


class World:
    def __init__(self):
        self.rooms = {}
        self.max_object_id = 0

    def add_room(self, room: Room):
        self.rooms[room.id] = room

        if room.id > self.max_id:
            self.max_id = room.id

    def get_room(self, _id) -> Room:
        return self.rooms[_id]

    def get_next_id(self):
        return self.max_id + 1

    def get_next_object_id(self):
        return self.max_object_id + 1

    def to_json_serializable(self):
        # construct JSON serializable object manually
        rooms = {}
        for _id, room in self.rooms.items():
            rooms[_id] = room.__dict__

        json_obj = {"max_id": self.max_id, "rooms": rooms}

        return json_obj

    def to_json_str(self):
        return json.dumps(self.to_json_serializable(), indent=4, sort_keys=True)

    @classmethod
    def from_json_str(cls, string):
        obj = json.loads(string)

        w = cls()
        w.max_id = obj["max_id"]

        rooms = obj["rooms"]

        for _id, room in rooms.items():
            r = Room()
            for attr, val in room.items():
                setattr(r, attr, val)
            w.rooms[int(_id)] = r

        return w


current_world = World()
