from worldbuilder import world, room, prompt, command

if __name__ == "__main__":
    p = prompt.Prompt()

    _id1 = command.parse("@create room Cell", batch=True)
    command.parse("@set room {} short_desc \"This is a horrible place\"".format(_id1), batch=True)
    command.parse("@set room {} desc This room consists of rough stone walls surrounding a smooth stone floor. The"
                  "floor is covered in a thin layer of hay, which gets progressively more blood-soaked as it progresses"
                  "toward the northern iron door. A rusty bucket is on the floor.".format(_id1), batch=True)

    _id2 = command.parse("@create room Corridor", batch=True)
    command.parse("@set room {} short_desc Dungeon corridor".format(_id2), batch=True)
    command.parse("@set room {} desc A long, straight corridor lit by torches connects various cells identical to"
                  "yours. There are no sounds other than wind coming down the stairwell to the east."
                  .format(_id2), batch=True)

    command.parse("@add exit n {} {}".format(_id1, _id2))
    command.parse("@add exit s {} {}".format(_id2, _id1))

    p.player.current_room = _id1

    p.run()