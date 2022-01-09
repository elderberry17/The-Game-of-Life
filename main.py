import pygame as pg
import sys
from const import max_set_cells, FPS, time_to_sleep
from tools import clock, check_click, draw, main_simulator, logging, show_end
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
                if check_click(event):
                    set_cells += 1
            elif has_changes:
                if not simulation:
                    simulation = True
                pops.append(main_simulator.grid.alive)
                has_changes = main_simulator.check_n_and_refresh()
                generation += 1
                gens.append(generation)
                sleep(time_to_sleep)

            if has_changes:
                logging(generation, main_simulator.grid.alive, simulation, max_set_cells - set_cells)
                draw()

            else:
                show_end(gens, pops)


if __name__ == "__main__":
    pg.init()
    play()
