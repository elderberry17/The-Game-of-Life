import sys

colors_dict = {"back": (245, 240, 225), "lines": (30, 61, 89), "life": (80, 200, 120), "text": (80, 200, 120)}
cell_size = 32
FPS = 60
time_to_sleep = 0.35
capture = 'The Game of Life'

width, height = int(sys.argv[1]) * cell_size, int(sys.argv[2]) * cell_size
max_set_cells = int(sys.argv[3])
extra_height = 64
