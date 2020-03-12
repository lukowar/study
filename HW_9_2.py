from random import choice

class Ghost(object):
    def __init__(self):
        self.color = choice(["White", "Yellow", "Purple", "Red"])

ghost = Ghost()
print (ghost.color)
