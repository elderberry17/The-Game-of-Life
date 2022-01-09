class Cell:
    def __init__(self, x, y, start_color, size):
        self.color = start_color
        self.size = size
        self.x = x
        self.y = y

    def change_color(self, new_color):
        self.color = new_color
