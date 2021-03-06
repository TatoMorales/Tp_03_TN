class Player:
    def __init__(self, name, xy, hit_points=50):
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        self.max_hp = hit_points

    def loc(self):
        return self.x, self.y

    def move_to(self, xy):
        """redefine self.x y self.y"""
        self.x, self.y = xy

    def index(self):
        """ returns the exact location in wich the player is"""
        location = self.x, self.y
        return location


    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"
