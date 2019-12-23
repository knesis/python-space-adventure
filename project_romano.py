__author__ = 'tonyromano'

import math
import time
import random
from Tkinter import *

# Anthony Romano - Whack-An-Alien Shooting Game - Jupiter

name = profile_main['name']               # Player Name
score1 = profile_main['score1']           # Score for Asteroid Minigame
score2 = profile_main['score2']           # Score for Simon Minigame
score3 = profile_main['score3']           # Score for Multiple Choice Minigame
score4 = profile_main['score4']           # Score for Minesweeper Minigame
score5 = profile_main['score5']           # Score for Shooting Minigame

master = Toplevel()
master.title( "Battle for the Milky Way" )
master.configure(cursor='shuttle', bg='beige')

canvas_width   = 800
canvas_height  = 500
# Space width

global missed
missed = 0

global defeated
defeated = 0

image_IDs = []
ship_IDs = []

start=0
end=0

def begin_game():
    global remove_item
    global place_ship
    global missed, defeated
    global w, shoot, start
    import random
    import time
    start = time.time()
    remove_item()
    w.bind("<Button-1>", shoot)
    place_ship(random.randint(1, 5))
    # start the mouse click shots and start placing ships around field


def place_ship(n):
    global x0, y0
    global missed, defeated
    global master, image_IDs, ship_IDs, w
    global saucer, tie_fighter, alien, boba_fett, supernova
    global tries_remaining_display, info_label, count_display, play_button, message
    import random
    # first clear previous ships
    for item in ship_IDs:
        w.delete(item)
    # assign ship to random location
    x0 = random.randint(50, 750)
    y0 = random.randint(50, 450)
    if n==1:
        ship_ID = w.create_image(x0, y0, image=saucer, anchor=CENTER)
    elif n==2:
        ship_ID = w.create_image(x0, y0, image=tie_fighter, anchor=CENTER)
    elif n==3:
        ship_ID = w.create_image(x0, y0, image=alien, anchor=CENTER)
    elif n==4:
        ship_ID = w.create_image(x0, y0, image=boba_fett, anchor=CENTER)
    elif n==5:
        ship_ID = w.create_image(x0, y0, image=supernova, anchor=CENTER)

    ship_IDs.append(ship_ID)

    # increase ship speed as the player gets closer
    if defeated < 3:
        master.after(2000, place_ship, random.randint(1, 5))
    elif 2 < defeated < 6:
        master.after(1000, place_ship, random.randint(1, 5))
    elif 5 < defeated < 9:
        master.after(800, place_ship, random.randint(1, 5))
    elif defeated == 9:
        master.after(600, place_ship, random.randint(1, 5))




def shoot( event ):
    global missed, defeated, start, end
    global remove_item
    global profile_main, name, score1, score2, score3, score4, score5
    global master, image_IDs, ship_IDs, w
    global tries_remaining_display, info_label, count_display, play_button, message
    import math, time, pickle
    diameter = 25
    fill_color = "yellow"
    radius=diameter/2
    x1, y1 = event.x, event.y
    image_ID = w.create_oval( x1-radius, y1-radius, x1+radius, y1+radius, fill = fill_color, outline = 'blue')
    image_IDs.append(image_ID)
    master.after(250, remove_item)
    # created yellow "bullet" and place at clicking point for 250 ms

    distance = math.sqrt((x1-x0) * (x1-x0) + (y1-y0) * (y1-y0)) # distance between shot and enemy

    if distance < 20: # if enemy is struck
        defeated += 1
        count_display.delete(0, END)
        count_display.insert(0, defeated)
        # add 1 to number of defeated attackers
        for item in ship_IDs:
            w.delete(item)

    else:   # if shot is missed
        missed += 1
        tries_remaining_display.delete(0, END)
        tries_remaining_display.insert(0, 10-missed)
        # subtract try remaining

    if defeated == 10:
        message = "You have survived the attack and can leave planet Jupiter! Congratulations!!!"
        end = time.time()
        score_time = round((end - start),1)
        # Adding score to profile
        if score5 == 0:
            score5 = score_time
        else:
            score5 = min(score5, score_time)
        nprofile = {'name': name, 'score1': score1, 'score2': score2, 'score3': score3, 'score4': score4,
                    'score5': score5}
        spath = 'profiles\\' + name + '.p'
        pickle.dump(nprofile, open(spath, 'wb'))
        profile_main = nprofile
        info_label.configure(text=message)
        play_button.config(state=DISABLED)
        play_button.config(text="Game Complete")
        w.unbind("<Button 1>")

    if missed == 10:
        message = "Your fleet has been defeated. Game Over."
        info_label.configure(text=message)
        play_button.config(state=DISABLED)
        play_button.config(text="Game Over")
        w.unbind("<Button 1>")


def remove_item():
    global image_IDs, w
    for item in image_IDs:
        w.delete(item)


intro_message = "Battle for the Milky Way: Click the intruders to defeat them!\n"
intro_message += "Defeat 10 intruders to win or lose when you miss 10 intruders.\n"
intro_message += 'Click the "Start Fight" button to start.'

info_label = Label(master, height =3, text = intro_message , bg = "beige")
info_label.grid(row=0, column=0, columnspan=3, sticky="EW")

w = Canvas(master,
           width=canvas_width,
           height=canvas_height, bg="beige", selectborderwidth=0, bd=0)

space = PhotoImage(file="images/space.gif")
w.grid(row=1, column=0, rowspan=5, columnspan=3)

w.create_image(4,4, image=space,  anchor=NW)


# Place a Frame along the right edge to serve as a score and control panel.
score_panel = Frame(master, bg='beige')
score_panel.grid(row=1, column=3, columnspan=2, rowspan=5, sticky=NS)

play_button = Button(master, text="Start Fight", command=begin_game, bg='beige')
play_button.grid(row=0, column=3, columnspan=2)

Label(score_panel, text="Attackers Defeated", width=20, bg='beige').grid(row=0, column=3)
count_display = Entry(score_panel, width=5, justify=CENTER)
count_display.grid(row=0, column=4)
count_display.insert(0, '  0  ')


Label(score_panel, text="Missed Shots Remaining", bg='beige').grid(row=1, column=3)
tries_remaining_display = Entry(score_panel, width=5, justify=CENTER, )
tries_remaining_display.grid(row=1, column=4)
tries_remaining_display.insert(0, ' 10 ')

saucer = PhotoImage(file="images/saucer.gif")
tie_fighter = PhotoImage(file="images/tie_fighter.gif")
alien = PhotoImage(file="images/alien.gif")
boba_fett = PhotoImage(file="images/boba_fett.gif")
supernova = PhotoImage(file="images/supernova.gif")


master.mainloop()