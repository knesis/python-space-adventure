from Tkinter import *

stat_width = 500
stat_height = 600

# Profile information imported from python_final_menu
name = profile_main['name']               # Player Name
score1 = profile_main['score1']           # Score for Asteroid Minigame
score2 = profile_main['score2']           # Score for Simon Minigame
score3 = profile_main['score3']           # Score for Multiple Choice Minigame
score4 = profile_main['score4']           # Score for Minesweeper Minigame
score5 = profile_main['score5']           # Score for Shooting Minigame

# Adapted from http://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
stat = Toplevel()
stat.geometry('%dx%d+%d+%d' % (stat_width,
                               stat_height,
                               stat.winfo_screenwidth()/2 - stat_width/2,
                               stat.winfo_screenheight()/2 - stat_height/2))
# End code adaptation

stat.title('Player Stats')
stat.resizable(0,0)

class StatLabel(object):
    def __init__(self, text=''):
        self.label = Label(stat, text=text, font=('ar destine', 16), fg='MediumPurple4', bg='black', padx=10)

def back():
    global stat
    stat.quit()
    stat.destroy()


stat_image = PhotoImage(file='images/space_small.gif')

stat_canvas = Canvas(stat, width=stat_width, height=stat_height)
stat_canvas.create_image(0,0, image=stat_image,anchor=NW)
stat_canvas.place(x=0,y=0)


title_label = StatLabel('Player Statistics')
title_label.label.config(padx=16)
title_label.label.place(x=stat_width/2, y=50,anchor=CENTER)

name_label = StatLabel('Player: ')
name_label.label.config(padx=16)
name_label.label.place(x=stat_width/2+50, y=150,anchor=E)
name_value_label = StatLabel(str(name))
name_value_label.label.config(padx=16)
name_value_label.label.place(x=stat_width/2+50, y=150,anchor=W)

asteroidscore_label = StatLabel('Asteroid: ')
asteroidscore_label.label.place(x=stat_width/2+50, y=200, anchor=E)
asteroidscore_value_label = StatLabel(str(score1))
asteroidscore_value_label.label.place(x=stat_width/2+50, y=200, anchor=W)

matchingscore_label = StatLabel('Simon: ')
matchingscore_label.label.place(x=stat_width/2+50, y=250, anchor=E)
matchingscore_value_label = StatLabel(str(score2))
matchingscore_value_label.label.place(x=stat_width/2+50, y=250, anchor=W)

mcscore_label = StatLabel('Multiple Choice: ')
mcscore_label.label.place(x=stat_width/2+50, y=300,anchor=E)
mcscore_value_label = StatLabel(str(score3))
mcscore_value_label.label.place(x=stat_width/2+50, y=300, anchor=W)

minesweeperscore_label = StatLabel('Minesweeper: ')
minesweeperscore_label.label.place(x=stat_width/2+50, y=350,anchor=E)
minesweeperscore_value_label = StatLabel(str(score4))
minesweeperscore_value_label.label.place(x=stat_width/2+50, y=350, anchor=W)

shootscore_label = StatLabel('Shooting: ')
shootscore_label.label.place(x=stat_width/2+50, y=400,anchor=E)
shootscore_value_label = StatLabel(str(score5))
shootscore_value_label.label.place(x=stat_width/2+50, y=400, anchor=W)



back_button = Button(stat, width=15, text='Back',font=('ar destine', 20),bg='MediumPurple3')
back_button.place(x=stat_width/2, y=500, anchor=CENTER)
back_button.config(state=NORMAL,disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=GROOVE)
back_button.config(command=back)


mainloop()