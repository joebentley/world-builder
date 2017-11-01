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
                    new_room.name = words[2]
                    world.current_world.add_room(new_room)
                    self.current_room = new_room.id
                    print("Moved into newly created room")

            if words[0] == "look":
                print(world.current_world.get_room(self.current_room).name)

            if command.startswith('q'):
                break
