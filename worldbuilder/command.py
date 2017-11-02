from . import world, room
import textwrap


# TODO string length checks

def parse(command, player=None, batch=False):
    words = command.split(" ")

    if words[0] == "@create":
        if words[1] == "room":
            new_room = room.Room()
            new_room.name = " ".join(words[2:])
            world.current_world.add_room(new_room)

            if not batch:
                player.current_room = new_room.id
                print("Moved into newly created room with id {}".format(new_room.id))

            return new_room.id

    if words[0] == "@set":
        if words[1] == "room":
            room_id = int(words[2])
            _room = world.current_world.get_room(room_id)

            if len(words) > 3:
                setattr(_room, words[3], " ".join(words[4:]))

                if not batch:
                    print("Changed property {} of room {}".format(words[3], room_id))

    # usage: @add exit direction from_id to_id
    if words[0] == "@add":
        if words[1] == "exit":
            direction = words[2]
            from_id = int(words[3])
            to_id = int(words[4])

            world.current_world.get_room(from_id).add_exit(direction, to_id)

            if not batch:
                print("Added exit {} from room {} to room {}".format(direction, from_id, to_id))

    if words[0] == "@list":
        if len(words) != 2:
            print("usage: @list rooms")
        elif words[1] == "rooms":
            for _, _room in world.current_world.rooms.items():
                print("{}: {} - {}".format(_room.id, _room.name, _room.short_desc))

    # usage: @save filename (save as JSON file?)
    if words[0] == "@save":
        pass

    # Player commands

    if words[0] in ("look", "l"):
        _room = world.current_world.get_room(player.current_room)
        print("{} - {}".format(_room.name, _room.short_desc))

        if len(_room.desc) > 0:
            print("\n{}".format("\n".join(textwrap.wrap(_room.desc, 80))))

        if len(_room.get_exits()) > 0:
            print()
            for direction, room_id in _room.get_exits().items():
                print("{} - {}\n".format(direction, world.current_world.get_room(room_id).name))

    # Exits
    if words[0] in ("north", "n"):
        pass
    if words[0] in ("south", "s"):
        pass
    if words[0] in ("east", "e"):
        pass
    if words[0] in ("west", "w"):
        pass
    if words[0] in ("northeast", "ne"):
        pass
    if words[0] in ("northwest", "nw"):
        pass
    if words[0] in ("southeast", "se"):
        pass
    if words[0] in ("southwest", "sw"):
        pass
    if words[0] in ("up", "u"):
        pass
    if words[0] in ("down", "d"):
        pass
    # TODO special exits
