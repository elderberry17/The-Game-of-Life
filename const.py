import sys

width, height = int(sys.argv[1]), int(sys.argv[2])
max_set_cells = int(sys.argv[3])
extra_height = 64
colors_dict = {"back": (245, 240, 225), "lines": (30, 61, 89), "life": (80, 200, 120), "text": (80, 200, 120)}
cell_size = 32
FPS = 60
time_to_sleep = 0.35
