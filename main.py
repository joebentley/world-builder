import worldbuilder.prompt as prompt
import worldbuilder.world as world
import worldbuilder.room as room

if __name__ == "__main__":
    p = prompt.Prompt()

    r1 = room.Room()
    r1.name = "Jail cell"
    r1.short_desc = "Horrible jail cell"

    p.current_room = r1.id

    world.current_world.add_room(r1)

    p.run()