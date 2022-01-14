import pygame as pg
from cell_class import Cell
from const import width, height, max_set_cells

class Grid:
    def __init__(self, display, colors, cell_size):
        self.display = display
        self.colors = colors
        self.cells = []
        self.cell_size = cell_size
        self.alive = max_set_cells

    def draw_grid(self):
        for x in range(width // self.cell_size):
            for y in range(height // self.cell_size):
                rect = pg.Rect(x * self.cell_size, y * self.cell_size,
                               self.cell_size, self.cell_size)
                pg.draw.rect(self.display, pg.Color(self.colors["lines"]), rect, 1)

    def make_cells(self):
        for x in range(0, width, self.cell_size):
            for y in range(0, height, self.cell_size):
                self.cells.append(Cell(x, y, self.colors["back"], self.cell_size))

    def draw_cells(self):
        for cell in self.cells:
            rect = pg.Rect(cell.x, cell.y,
                           cell.size, cell.size)

            pg.draw.rect(self.display, pg.Color(cell.color), rect)
