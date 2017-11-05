from . import world


class Object:
    def __init__(self, _id):
        if _id == 0:
            self.id = world.current_world.get_next_object_id()
        else:
            self.id = _id

        self._name = ""
        self._desc = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value