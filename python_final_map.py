
# Sun picture - http://nineplanets.org/images/thesun.jpg
# Inner Solar System - https://www.scienceabc.com/wp-content/uploads/2016/04/Solar-system-without-sun1.jpg
# Menu - http://www.iwallscreen.com/stock/galaxies-galaxy-space.jpg


from Tkinter import *

map_width = 1024
map_height = 868

map = Toplevel()
map.title('Python Space Adventure')
map.geometry('%dx%d+%d+%d' % (map_width,
                               map_height,
                               map.winfo_screenwidth()/2 - map_width/2,
                               map.winfo_screenheight()/2 - map_height/2))
map.resizable(0,0)

class MapButton(object):
    def __init__(self, text='', command=None, state=NORMAL):
        global map_menu
        self.button = Button(map_menu, width=13, text=text, font=('ar destine', 20),bg='MediumPurple3', \
            command=command, state=state, disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=RAISED)

def launch_sun(event):
    global profile_main
    print "The sun is too hot!"


def launch_mercury(event):
    global profile_main
    print 'Mercury'
    execfile('project_vo.py')

def launch_venus(event):
    global profile_main
    print 'Venus'
    execfile('project_daloisio.py')

def launch_earth(event):
    global profile_main
    print 'Earth'
    execfile('project_wan.py')

def launch_mars(event):
    global profile_main
    print 'Mars'
    execfile('space_minesweeper.py')

def launch_jupiter(event):
    global profile_main
    print 'Jupiter'
    execfile('project_romano.py')

def main_menu():
    global profile_main, menu, map
    map.destroy()
    menu.deiconify()

def player_stats():
    global profile_main
    execfile('player_stats.py')

def leaderboard():
    global profile_main
    execfile('leaderboard.py')

def quit_game():
    quit()

map_image = PhotoImage(file='images/space_map.gif')

map_canvas = Canvas(map, width=map_width, height=map_height)
map_canvas.create_image(0,0, image=map_image, anchor=NW)

# Sun dimensions:     (NW: 356,218; SE: 626,488)
# Mercury dimensions: (NW: 676,223; SE: 748,295)
# Venus dimensions:   (NW: 193,542; SE: 288,641)
# Earth dimensions:   (NW: 761,429; SE: 848,521)
# Mars dimensions:    (NW:  67,428; SE: 133,494)
# Jupiter dimensions: (NW: 780, 21; SE: 879,118)

sun_id = map_canvas.create_oval(356,218,626,488,width=0)
mercury_id = map_canvas.create_oval(676,223,748,295,width=0)
venus_id = map_canvas.create_oval(193,542,288,641,width=0)
earth_id = map_canvas.create_oval(761,429,848,521,width=0)
mars_id = map_canvas.create_oval(67,428,133,494,width=0)
jupiter_id = map_canvas.create_oval(780,21,879,118,width=0)

map_canvas.tag_bind(sun_id, '<Button-1>', launch_sun)
map_canvas.tag_bind(mercury_id, '<Button-1>', launch_mercury)
map_canvas.tag_bind(venus_id, '<Button-1>', launch_venus)
map_canvas.tag_bind(earth_id, '<Button-1>',launch_earth)
map_canvas.tag_bind(mars_id, '<Button-1>', launch_mars)
map_canvas.tag_bind(jupiter_id, '<Button-1>', launch_jupiter)

map_canvas.grid()

map_menu = Frame(map_canvas, bg='MediumPurple3')

menu_button = MapButton('Main Menu', main_menu, NORMAL)
menu_button.button.grid(row=0, column=0, padx=(0,16))

stat_button = MapButton('Player Stats', player_stats, NORMAL)
stat_button.button.grid(row=0, column=1, padx=(0,16))

lead_button = MapButton('Leaderboard', leaderboard, NORMAL)
lead_button.button.grid(row=0, column=2, padx=(0,16))

quit_button = MapButton('Quit', quit_game, NORMAL)
quit_button.button.grid(row=0, column=3)

info_m_label = Label(map_menu, text='Select a planet!',font=('ar destine', 16), fg='MediumPurple4', bg='black')
info_m_label.grid(row=1, columnspan=4, sticky=W+E)

map_menu.place(relx=0, rely=1, relwidth=1, anchor=SW)

mainloop()