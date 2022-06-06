import random
from player import Player

class Gnome(Player):
    def __init__(self, name, xy):
        super().__init__(name, xy, 50)
        self.alive = True
        self.face = 'G'

    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def kill(self):
        self.hp = 0
        self.alive = False

    def has_sword(self):
        # completar
        pass
