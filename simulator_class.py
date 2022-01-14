from const import cell_size, height, colors_dict


class Simulation:
    def __init__(self, grid_to_simulate):
        self.grid = grid_to_simulate

    def find_n(self, x, y):
        neigh_coors = [(x + cell_size, y), (x, y + cell_size),
                       (x - cell_size, y), (x, y - cell_size),
                       (x + cell_size, y + cell_size), (x - cell_size, y - cell_size),
                       (x + cell_size, y - cell_size), (x - cell_size, y + cell_size)]

        neigh_coors = list(filter(lambda t: 0 <= t[0] <= 992 and 0 <= t[1] <= 480, neigh_coors))
        neigh_indexes = list(map(lambda t: t[0] // cell_size * height // cell_size + t[1] // cell_size, neigh_coors))

        return neigh_indexes

    def count_alive_n(self, neighbours):
        n_alive = 0
        for index in neighbours:
            if self.grid.cells[index].color == colors_dict["life"]:
                n_alive += 1
        return n_alive

    def check_n_and_refresh(self):
        changes = False
        for cell in self.grid.cells:
            x, y = cell.x, cell.y
            neighbours = self.find_n(x, y)
            n_alive = self.count_alive_n(neighbours)
            if cell.color == colors_dict["life"]:
                if n_alive not in [2, 3]:
                    cell.change_color(colors_dict["back"])
                    self.grid.alive -= 1
                    changes = True
            else:
                if n_alive == 3:
                    cell.change_color(colors_dict["life"])
                    self.grid.alive += 1
                    changes = True
        return changes
