class Tile:
    TILE_WIDTH = 200
    TILE_HEIGHT = 200
    def __init__(self, pos):
        self.pos = pos
        self.pressed = False
        self.value = 'A'

    def press(self, value):
        self.value = value
        self.pressed = True

    def unpress(self):
        self.value = 'A'
        self.pressed = False

    def __str__(self):
        return f"Top left corner of tile: {self.pos}, Pressed is {self.pressed} and Value is {self.value}"
