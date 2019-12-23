
# Sun picture - http://nineplanets.org/images/thesun.jpg
# Inner Solar System - https://www.scienceabc.com/wp-content/uploads/2016/04/Solar-system-without-sun1.jpg
# Menu - http://www.iwallscreen.com/stock/galaxies-galaxy-space.jpg


from Tkinter import *

# Main Menu - Start Game From Here

menu_width = 1024
menu_height = 768

menu = Tk()
menu.title('Python Space Adventure')
menu.geometry('%dx%d+%d+%d' % (menu_width,
                               menu_height,
                               menu.winfo_screenwidth()/2 - menu_width/2,
                               menu.winfo_screenheight()/2 - menu_height/2))
menu.resizable(0,0)

class MenuButton(object):
    def __init__(self, text='', command=None, state=NORMAL):
        self.button = Button(menu, width=15, text=text, font=('ar destine', 20),bg='MediumPurple3', \
            command=command, state=state, disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=GROOVE)


def new_game():
    global profile_main
    execfile('new_player.py')

def continue_game():
    global profile_main
    global menu
    menu.withdraw()
    execfile('python_final_map.py')

def load_profile():
    global profile_main
    try:
        execfile('load_profile.py')
    except TclError as e: pass
    except IOError as e:
        load.destroy()
        info_label.config(text='Profile Directory Missing')
    except KeyError as e:
        load.destroy()
        info_label.config(text='Profile Corrupted')
        return

def player_stats():
    global profile_main
    execfile('player_stats.py')

def quit_game():
    quit()



menu_image = PhotoImage(file='images/space_menu.gif')

menu_canvas = Canvas(menu, width=menu_width, height=menu_height)
menu_canvas.create_image(0,0, image=menu_image, anchor=NW)
menu_canvas.grid()


title_label = Label(menu, padx=16, text='Python Space Adventure', font=('ar destine', 40), fg='MediumPurple4', bg='black')
title_label.config(relief=FLAT)
title_label.place(x=menu_width/2, y=100, anchor=CENTER)


# Creates Menu Buttons for New Game, Continue, Load Profile, Player Stats, and Quit

newgame_button = MenuButton('New Game', new_game, NORMAL)
newgame_button.button.place(x=menu_width/2,y=250, anchor=CENTER)

continue_button = MenuButton('Continue', continue_game, DISABLED)
continue_button.button.place(x=menu_width/2,y=350, anchor=CENTER)

loadprofile_button = MenuButton('Load Profile', load_profile, NORMAL)
loadprofile_button.button.place(x=menu_width/2,y=450, anchor=CENTER)

stat_button = MenuButton('Player Stats', player_stats, DISABLED)
stat_button.button.place(x=menu_width/2,y=550, anchor=CENTER)

quit_button = MenuButton('Quit', quit_game, NORMAL)
quit_button.button.place(x=menu_width/2,y=650, anchor=CENTER)

info_label = Label(menu, text='Welcome to Python Space Adventure!',font=('ar destine', 16), fg='MediumPurple4', bg='black')
info_label.place(x=0, y=menu_height, relwidth=1.0, anchor=SW)

mainloop()

