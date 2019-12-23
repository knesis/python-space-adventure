from Tkinter import *
import random
import pickle
import tkMessageBox

# Anthony Knesis - Space Minesweeper - Mars

#  Set window width and height
ms_width = 1024
ms_height = 768

# Set minesweeper grid rows and columns
ms_rows = 8
ms_cols = 8
ms_mines = 10
points = (ms_rows * ms_cols)

#Code for initializing grid adapted from http://stackoverflow.com/questions/521674/initializing-a-list-to-a-known-number-of-elements-in-python
tile_grid = []
mines=[]
flags=[]

name = profile_main['name']               # Player Name
score1 = profile_main['score1']           # Score for Asteroid Minigame
score2 = profile_main['score2']           # Score for Simon Minigame
score3 = profile_main['score3']           # Score for Multiple Choice Minigame
score4 = profile_main['score4']           # Score for Minesweeper Minigame
score5 = profile_main['score5']           # Score for Shooting Minigame

ms = Toplevel()
ms.geometry('%dx%d+%d+%d' % (ms_width,
                               ms_height,
                               ms.winfo_screenwidth()/2 - ms_width/2,
                               ms.winfo_screenheight()/2 - ms_height/2))
ms.resizable(0,0)

# Function to prevent wraparound of check_mine due to negative indexing
def w(index):
    if index >= 0:
        return index
    else:
        return None

class MenuButton(object):
    def __init__(self, text='', command=None, state=NORMAL):
        global ms_menu_frame
        self.button = Button(ms_menu_frame, width=13, text=text, font=('ar destine', 20),bg='MediumPurple3', \
            command=command, state=state, disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=RAISED)

class MineButton(object):
    '''Defines characteristics of minesweeper button. Includes attributes row, col, status, counter, and button.'''
    def __init__(self, mstat=0,mnum=0):
        global ms_frame
        global square_image
        self.row = 0       # Row in which the mine is placed
        self.col = 0       # Column in which the mine is placed
        self.status=mstat  # Status of tile; 0=empty, 1=mine
        self.counter=mnum  # Counter of adjacent mines
        self.button = Button(ms_frame, image=square_image, width=30, height=30, text=' ', compound=CENTER, bg='sienna3', \
            command=self.check_mine, state=NORMAL, disabledforeground='black',activebackground='sienna1')
        self.button.bind('<Button-3>', self.flag)

    def check_mine(self):
        global mines, tile_grid, points, score_entry
        # Recursion sanity check
        if self.button.cget('state') == DISABLED:
            return
        # Mine vs empty space
        if self.status==1:
            self.button.config(text='M', state=DISABLED, relief=SUNKEN, bg='red')
            self.button.unbind('<Button-3>')
            for mine in mines:
                mine.button.config(text='M', state=DISABLED, relief=SUNKEN, bg='red')
            for list in tile_grid:
                for tile in list:
                    tile.button.config(state=DISABLED)
        elif self.status==0:
            self.button.config(text=self.counter, state=DISABLED, relief=SUNKEN, bg='sienna1')
            self.button.unbind('<Button-3>')
            points -= 1
            score_entry.config(state=NORMAL)
            score_entry.delete(0,END)
            score_entry.insert(0,points)
            score_entry.config(state=DISABLED)

            # Fills in adjacent empty spaces
            erow = self.row
            ecol = self.col
            if self.counter == 0:
                self.button.config(text=' ')
                try: (tile_grid[w(erow - 1)][w(ecol - 1)]).check_mine()
                except TypeError as e: pass
                except IndexError as e: pass

                try: (tile_grid[w(erow - 1)][w(ecol)]).check_mine()
                except TypeError as e: pass
                except IndexError as e: pass

                try: (tile_grid[w(erow - 1)][w(ecol + 1)]).check_mine()
                except TypeError as e: pass
                except IndexError as e: pass

                try: (tile_grid[w(erow)][w(ecol - 1)]).check_mine()
                except TypeError as e: pass
                except IndexError as e: pass

                try: (tile_grid[w(erow)][w(ecol + 1)]).check_mine()
                except TypeError as e: pass
                except IndexError as e: pass

                try: (tile_grid[w(erow + 1)][w(ecol - 1)]).check_mine()
                except TypeError as e: pass
                except IndexError as e: pass

                try: (tile_grid[w(erow + 1)][w(ecol)]).check_mine()
                except TypeError as e: pass
                except IndexError as e: pass

                try: (tile_grid[w(erow + 1)][w(ecol + 1)]).check_mine()
                except TypeError as e: pass
                except IndexError as e: pass

    def flag(self,event):
        global flags, flags_entry, points
        global check_win
        if self.button.cget('state') == NORMAL:
            self.button.config(text='F',bg='blue', state=DISABLED)
            flags.append(self)
            points -= 1
            score_entry.config(state=NORMAL)
            score_entry.delete(0,END)
            score_entry.insert(0,points)
            score_entry.config(state=DISABLED)
            flags_entry.config(state=NORMAL)
            flags_entry.delete(0, END)
            flags_entry.insert(0, len(flags))
            flags_entry.config(state=DISABLED)
            check_win()
        elif self.button.cget('state') == DISABLED:
            self.button.config(text=' ', bg='sienna3', state=NORMAL)
            flags.remove(self)
            flags_entry.config(state=NORMAL)
            flags_entry.delete(0, END)
            flags_entry.insert(0, len(flags))
            flags_entry.config(state=DISABLED)
            check_win()

def mine_place():
    global w
    global ms_rows, ms_cols
    global mines, tile_grid
    import random
    mrow = random.choice(range(0,ms_rows))
    mcol = random.choice(range(0,ms_cols))
    while (tile_grid[mrow][mcol]).status == 1:
        mrow = random.choice(range(0,ms_rows))
        mcol = random.choice(range(0,ms_cols))
    tile_grid[mrow][mcol].status = 1
    mines.append((tile_grid[mrow][mcol]))
    print mrow, mcol
    # Increase mine counter for adjacent squares
    try: (tile_grid[w(mrow - 1)][w(mcol - 1)]).counter += 1
    except TypeError as e: pass
    except IndexError as e: pass

    try: (tile_grid[w(mrow - 1)][w(mcol)]).counter += 1
    except TypeError as e: pass
    except IndexError as e: pass

    try: (tile_grid[w(mrow - 1)][w(mcol + 1)]).counter += 1
    except TypeError as e: pass
    except IndexError as e: pass

    try:(tile_grid[w(mrow)][w(mcol-1)]).counter += 1
    except TypeError as e: pass
    except IndexError as e: pass

    try:(tile_grid[w(mrow)][w(mcol+1)]).counter += 1
    except TypeError as e: pass
    except IndexError as e: pass

    try: (tile_grid[w(mrow+1)][w(mcol-1)]).counter += 1
    except TypeError as e: pass
    except IndexError as e: pass

    try: (tile_grid[w(mrow+1)][w(mcol)]).counter += 1
    except TypeError as e: pass
    except IndexError as e: pass

    try: (tile_grid[w(mrow+1)][w(mcol+1)]).counter += 1
    except TypeError as e: pass
    except IndexError as e: pass

def reset():
    global ms_rows, ms_cols, ms_mines, points
    global tile_grid, flags, mines
    global mines_entry, flags_entry
    global MineButton, info_ms_label, ms_frame, score_entry
    global mine_place
    for mine in mines:
        mine.button.destroy()
    for list in tile_grid:
        for tile in list:
            tile.button.destroy()
    mines = []
    flags = []
    tile_grid = []
    mines_entry.config(state=NORMAL)
    mines_entry.delete(0,END)
    mines_entry.insert(0, str(ms_mines))
    mines_entry.config(state=DISABLED)
    flags_entry.config(state=NORMAL)
    flags_entry.delete(0,END)
    flags_entry.insert(0, '0')
    flags_entry.config(state=DISABLED)
    tile_grid = [[0 for y in range(ms_cols)] for x in range(ms_rows)]
    points = (ms_rows * ms_cols)
    score_entry.config(state=NORMAL)
    score_entry.delete(0,END)
    score_entry.insert(0,points)
    score_entry.config(state=DISABLED)
    info_ms_label.config(text='Planet: Mars')
    for row in range(0,ms_rows):
        for col in range(0,ms_cols):
            tile_grid[row][col] = MineButton()
            (tile_grid[row][col]).row = row
            (tile_grid[row][col]).col = col
            (tile_grid[row][col]).button.grid(row=row, column=col)
    for x in range(ms_mines):
        mine_place()

def change_difficulty():
    global d, points
    global ms_rows, ms_cols, ms_mines
    global reset
    for list in tile_grid:
        for tile in list:
            print tile.row, tile.col
            tile.button.state=NORMAL
            tile.button.destroy()
    difficulty = d.get()
    if difficulty == 1:
        ms_rows = 8
        ms_cols = 8
        ms_mines = 10
        reset()
    elif difficulty == 2:
        ms_rows = 10
        ms_cols = 10
        ms_mines = 20
        reset()
    elif difficulty == 3:
        ms_rows = 10
        ms_cols = 15
        ms_mines = 30
        reset()

def check_win():
    global flags, mines
    global score4, points, d
    global tile_grid
    global info_ms_label, score_entry
    if len(flags) != len(mines):
        return
    for flag in flags:
        if flag.status !=1:
            return
    info_ms_label.config(text='You win!')
    points += (150 * d.get())
    score_entry.config(state=NORMAL)
    score_entry.delete(0,END)
    score_entry.insert(0,points)
    score_entry.config(state=DISABLED)
    score4 = max(score4, points)
    for list in tile_grid:
        for tile in list:
            tile.button.config(state=DISABLED)
            tile.button.unbind('<Button-3>')

def help_ms():
    import tkMessageBox
    tkMessageBox.showinfo('Minesweeper Help', "Use the Left Mouse Click to uncover a tile.\n\
    The uncovered number indicates the number of mines in adjacent tiles.\n\
    Use the Right Mouse Click to place flags on suspected mines.\n\
    Cover all mines to win!")

def player_stats():
    global profile_main
    execfile('player_stats.py')

def leaderboard():
    global profile_main
    execfile('leaderboard.py')

def save_quit():
    global ms
    global profile_main
    global name, score1, score2, score3, score4, score5
    import pickle
    nprofile = {'name': name, 'score1': score1, 'score2': score2, 'score3': score3, 'score4': score4, 'score5': score5}
    spath = 'profiles\\' + name + '.p'
    pickle.dump(nprofile, open(spath, 'wb'))
    profile_main = nprofile
    ms.quit()
    ms.destroy()

# Mars image from http://planetary-science.org/wp-content/uploads/2014/12/Ladon-basin-in-full-color.jpg
square_image = PhotoImage()
ms_image = PhotoImage(file='images\mars.gif')

ms_canvas = Canvas(ms, width=ms_width, height=ms_height)
ms_canvas.create_image(0,0, image=ms_image, anchor=NW)
ms_canvas.place(x=0,y=0)

ms_frame = Frame(ms_canvas, bg='MediumPurple3')
ms_info_frame = Frame(ms_canvas, bg='sienna3')
ms_menu_frame = Frame(ms_canvas, bg='MediumPurple3')

# Description label
description = '\nUpon returning to your spacecraft after a surface exploration of the planet Mars, \
you have encountered a minefield placed by the crafty (yet dangerous) Martian people.\n\n\
Thankfully, your space echo-locator can detect nearby mines when placed in the soil.\n\n\
Uncover tiles for clues, and flag all the mines to get home safely.\n'
description_label = Label(ms, text=description, font=('ocr a std', 11), bg='sienna3', wraplength=828, justify=LEFT)
description_label.place(relx=0, rely=0, width=828, anchor=NW)

# Score display
score_label = Label(ms_info_frame, text='Score:', font=('ar destine', 16), bg='sienna3')
score_label.grid(row=0, column=0, pady=(20,0))

score_entry = Entry(ms_info_frame, font=('ar destine', 16), bg='sienna3', justify=CENTER)
score_entry.insert(0,'0')
score_entry.config(state=DISABLED, disabledbackground='sienna3', disabledforeground='black')
score_entry.grid(row=1, column=0)


# Difficulty display and buttons
difficulty_label = Label(ms_info_frame, text='Difficulty:   ', font=('ar destine', 16), bg='sienna3')
difficulty_label.grid(row=4, column=0, pady=(50,0))

d = IntVar()
easy_radio = Radiobutton(ms_info_frame, text='Easy', font=('ar destine', 16), bg='sienna3', \
                         justify=LEFT, variable=d,value=1,command=change_difficulty)
easy_radio.grid(row=5, column=0, sticky=W)
easy_radio.select()

medium_radio = Radiobutton(ms_info_frame, text='Medium', font=('ar destine', 16), bg='sienna3', \
                        justify=LEFT, variable=d,value=2,command=change_difficulty)
medium_radio.grid(row=6, column=0, sticky=W)

hard_radio = Radiobutton(ms_info_frame, text='Hard', font=('ar destine', 16), bg='sienna3', \
                         justify=LEFT, variable=d,value=3,command=change_difficulty)
hard_radio.grid(row=7, column=0, sticky=W)


# Mines and flags counter
mines_label = Label(ms_info_frame, text='Mines:', font=('ar destine', 16), bg='sienna3')
mines_label.grid(row=8, column=0, pady=(50,0))

mines_entry = Entry(ms_info_frame, font=('ar destine', 16), bg='sienna3', justify=CENTER)
mines_entry.insert(0, str(ms_mines))
mines_entry.config(state=DISABLED, disabledbackground='sienna3', disabledforeground='black')
mines_entry.grid(row=9, column=0)

flags_label = Label(ms_info_frame, text='Flags:', font=('ar destine', 16), bg='sienna3')
flags_label.grid(row=10, column=0, pady=(20,0))

flags_entry = Entry(ms_info_frame, font=('ar destine', 16), bg='sienna3', justify=CENTER)
flags_entry.insert(0,'0')
flags_entry.config(state=DISABLED, disabledbackground='sienna3', disabledforeground='black')
flags_entry.grid(row=11, column=0)

# Help button
help_radio = Button(ms_info_frame, text='?', font=('ar destine', 18), bg='sienna3', \
                         justify=LEFT, command=help_ms, relief=RAISED, activebackground='sienna3')
help_radio.grid(row=12, column=0, ipadx=(13), padx=(0,85), pady=(35,0))


# Bottom Menu buttons
reset_button = MenuButton('Reset', reset, NORMAL)
reset_button.button.grid(row=0, column=0, padx=(0,16))

stat_button = MenuButton('Player Stats', player_stats, NORMAL)
stat_button.button.grid(row=0, column=1, padx=(0,16))

lead_button = MenuButton('Leaderboard', leaderboard, NORMAL)
lead_button.button.grid(row=0, column=2, padx=(0,16))

quit_button = MenuButton('Save & Quit', save_quit, NORMAL)
quit_button.button.grid(row=0, column=3)

# Info label
info_ms_label = Label(ms_menu_frame, text='Planet: Mars',font=('ar destine', 16), fg='MediumPurple4', bg='black')
info_ms_label.grid(row=1, columnspan=4, sticky=W+E)

ms_menu_frame.place(relx=0, rely=1, relwidth=1, anchor=SW)
ms_info_frame.place(relx=1, rely=0, width=200, relheight=1, anchor=NE)
ms_frame.place(anchor=CENTER,x=ms_width/2-100,y=ms_height/2+58)

reset()

mainloop()