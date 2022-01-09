import pygame as pg
from const import height, width, cell_size, colors_dict


def show_plot(gens, pops):
    max_pop = max(pops)
    max_gen = gens[-1]
    scale_x, scale_y = width // max_gen, height // max_pop
    gens = [(generation - 1) * scale_x + cell_size for generation in gens]
    pops = [height - population * scale_y + cell_size for population in pops]

    points = [(x, y) for x, y in zip(gens, pops)]
    pg.draw.lines(display, colors_dict["life"], False, points, width=2)
    pg.display.flip()
