# The Game of Life

Here is one of my task from Tinkoff exam for ML&DL course and it is really shitty things yet

I must simulate a game named "Game of life" (like Scorpions's song, ha-ha) 

PyGame window freezes, when there is not active movements from user

It's bad, 'cause one should just see this life simulation with out any interventions

This process may be really long lasting, so one can't move her/his mouse all the time

Also there is not beautiful plot in the end (ha-ha) showing dynamic of this "society" population as I'd like it to be

# Attention. How to use it:

I used pygame library for the graphic interface (there isn't anything about using outsider libraries it the conditions, so I did it)

You have to call "pip3 install pygame" in the terminal. You also must have installed python3 on your computer (obviously)

I made a little bash script named install.bash, which may does it for you. But it won't work if you have Windows OS

I also pondered about put it in a Docker container, but my friends said me "Don't do the things you're not required to do" and I heeded this advice

### After you clone this repo to your local machine you should call it in this repo:

python3 main.py -num_cells_for_width -num_cells_for_height -num_of_start_creatures

-num_cells_for_width -- a game field size in cells in width 
-num_cells_for_heigth -- a game field size in cells in height
-num_of_start_creatures -- an amount of creatures you set in the field in the start

All these parameters are integere positive numbers!!

![see cuteness](pictures/fun.jpg "Как-то так я писал этот код")​

