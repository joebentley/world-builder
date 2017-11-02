from . import world, room


class Prompt:
    def __init__(self):
        self.current_room = None

    def run(self):
        while True:
            command = input('> ')

            words = command.split(" ")

            if words[0] == "@create":
                if words[1] == "room":
                    new_room = room.Room()
                    new_room.name = " ".join(words[2:])
                    world.current_world.add_room(new_room)
                    self.current_room = new_room.id
                    print("Moved into newly created room with id {}".format(new_room.id))

            if words[0] == "@set":
                if words[1] == "room":
                    room_id = int(words[2])
                    _room = world.current_world.get_room(room_id)

                    if words[3] == "desc":
                        _room.desc = " ".join(words[4:])

                        print("Changed room {} description".format(room_id))

            if words[0] == "@list":
                if len(words) != 2:
                    print("usage: @list rooms")
                elif words[1] == "rooms":
                    for _, _room in world.current_world.rooms.items():
                        print("{}: {} - {}".format(_room.id, _room.name, _room.short_desc))

            if words[0] == "look":
                _room = world.current_world.get_room(self.current_room)
                print("{} - {}".format(_room.name, _room.short_desc))

                if len(_room.desc) > 0:
                    print("\n{}".format(_room.desc))

            if command.startswith('q'):
                break
