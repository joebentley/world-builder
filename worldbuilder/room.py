from . import world


class Room:
    def __init__(self, _id=0):
        if _id == 0:
            self.id = world.current_world.get_next_id()
        else:
            self.id = _id

        self._name = ""
        self._short_desc = ""
        self._desc = ""
        self.exits = {}
        self.objects = {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def short_desc(self):
        return self._short_desc

    @short_desc.setter
    def short_desc(self, value):
        self._short_desc = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

    def add_exit(self, exit_name, room_id):
        self.exits[exit_name] = room_id

    def get_exits(self):
        return self.exits

    def add_object(self, object):
        self.objects[object.id] = object

    def get_objects(self):
        return self.objects