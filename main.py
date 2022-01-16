import pygame as pg
import sys
from const import max_set_cells, FPS, time_to_sleep, \
    width, height, extra_height, colors_dict, cell_size, capture
from tools import check_click, draw, logging, show_end
from simulator_class import Simulation
from grid_class import Grid
from time import sleep


def play():
    set_cells = 0
    generation = 0
    simulation = False
    has_changes = True
    gens, pops = [], []
    while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif set_cells < max_set_cells:
                if check_click(event, main_grid):
                    set_cells += 1

        if has_changes and set_cells == max_set_cells:
            if not simulation:
                simulation = True
            pops.append(main_simulator.grid.alive)
            has_changes = main_simulator.check_n_and_refresh()
            generation += 1
            gens.append(generation)
            sleep(time_to_sleep)

        if has_changes:
            logging(display, generation, main_simulator.grid.alive, simulation, max_set_cells - set_cells)
            draw(main_grid)

        else:
            show_end(display, gens, pops)


if __name__ == "__main__":
    pg.init()

    if width <= 0 or height <= 0:
        print("Некорректный размер поля!")
    elif max_set_cells % 1 != 0 or max_set_cells < 1:
        print("Некорректное первоначальное количество существ!")
    else:
        display = pg.display.set_mode((width, height + extra_height))
        pg.display.set_caption(capture)
        clock = pg.time.Clock()

        main_grid = Grid(display, colors_dict, cell_size)
        main_grid.make_cells()

        main_simulator = Simulation(main_grid)
        play()
