from . import player, command


class Prompt:
    def __init__(self):
        self.player = player.Player()

    def run(self):
        while True:
            command_string = input('> ')

            command.parse(command_string, self.player)

            if command_string.startswith('q'):
                break
