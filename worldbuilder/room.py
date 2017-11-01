from . import world


class Room:
    def __init__(self, _id=0):
        if _id == 0:
            self.id = world.current_world.get_next_id()
        else:
            self.id = _id

        self._name = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
