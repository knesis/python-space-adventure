
from Tkinter import *
import pickle
import os

lead_width = 500
lead_height = 600

scores1 = []
scores2 = []
scores3 = []
scores4 = []
scores5 = []

# Adapted from http://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
lead = Toplevel()
lead.geometry('%dx%d+%d+%d' % (lead_width,
                               lead_height,
                               lead.winfo_screenwidth()/2 - lead_width/2,
                               lead.winfo_screenheight()/2 - lead_height/2))
# End code adaptation

lead.title('Leaderboard')
lead.resizable(0,0)

class LeadLabel(object):
    def __init__(self, text=''):
        self.label = Label(lead, text=text, font=('ar destine', 12), fg='MediumPurple4', bg='black', padx=10)

def back():
    global lead
    lead.quit()
    lead.destroy()

# Get highest scores from each game
profile_dir = os.getcwd() + '\profiles'
for file in os.listdir(profile_dir):
    fpath = os.path.join(profile_dir, file)
    lprofile = pickle.load(open(fpath, 'rb'))
    scores1.append((lprofile['score1'], lprofile['name']))
    scores2.append((lprofile['score2'], lprofile['name']))
    scores3.append((lprofile['score3'], lprofile['name']))
    scores4.append((lprofile['score4'], lprofile['name']))
    scores5.append((lprofile['score5'], lprofile['name']))

scores1.sort(reverse=True)
scores2.sort(reverse=True)
scores3.sort(reverse=True)
scores4.sort(reverse=True)
#For game 5, lower scores are better.
scores5.sort()
for score in scores5:
    if score > 0 or '0':
        scores5.remove(score)




lead_image = PhotoImage(file='images/space_small.gif')

lead_canvas = Canvas(lead, width=lead_width, height=lead_height)
lead_canvas.create_image(0,0, image=lead_image,anchor=NW)
lead_canvas.place(x=0,y=0)


title_label = LeadLabel('Player Leaderboard')
title_label.label.config(padx=16)
title_label.label.place(x=lead_width/2, y=50,anchor=CENTER)

game_header_label = LeadLabel('Game: ')
game_header_label.label.config(padx=16)
game_header_label.label.place(x=lead_width/2-80, y=150,anchor=E)

name_header_label = LeadLabel('Name: ')
name_header_label.label.config(padx=16)
name_header_label.label.place(x=lead_width/2, y=150,anchor=CENTER)

score_header_label = LeadLabel('Score: ')
score_header_label.label.config(padx=16)
score_header_label.label.place(x=lead_width/2+50, y=150,anchor=W)

asteroidscore_label = LeadLabel('Asteroid: ')
asteroidscore_label.label.place(x=lead_width/2-80, y=200, anchor=E)
asteroidscore_name_label = LeadLabel(str(scores1[0][1]))
asteroidscore_name_label.label.place(x=lead_width/2, y=200, anchor=CENTER)
asteroidscore_value_label = LeadLabel(str(scores1[0][0]))
asteroidscore_value_label.label.place(x=lead_width/2+150, y=200, anchor=E)

matchingscore_label = LeadLabel('Simon: ')
matchingscore_label.label.place(x=lead_width/2-80, y=250, anchor=E)
matchingscore_name_label = LeadLabel(str(scores2[0][1]))
matchingscore_name_label.label.place(x=lead_width/2, y=250, anchor=CENTER)
matchingscore_value_label = LeadLabel(str(scores2[0][0]))
matchingscore_value_label.label.place(x=lead_width/2+150, y=250, anchor=E)

mcscore_label = LeadLabel('Quiz: ')
mcscore_label.label.place(x=lead_width/2-80, y=300,anchor=E)
mcscore_name_label = LeadLabel(str(scores3[0][1]))
mcscore_name_label.label.place(x=lead_width/2, y=300, anchor=CENTER)
mcscore_value_label = LeadLabel(str(scores3[0][0]))
mcscore_value_label.label.place(x=lead_width/2+150, y=300, anchor=E)

minesweeperscore_label = LeadLabel('Minesweeper: ')
minesweeperscore_label.label.place(x=lead_width/2-80, y=350,anchor=E)
minesweeperscore_name_label = LeadLabel(str(scores4[0][1]))
minesweeperscore_name_label.label.place(x=lead_width/2, y=350, anchor=CENTER)
minesweeperscore_value_label = LeadLabel(str(scores4[0][0]))
minesweeperscore_value_label.label.place(x=lead_width/2+150, y=350, anchor=E)

shootscore_label = LeadLabel('Shooting: ')
shootscore_label.label.place(x=lead_width/2-80, y=400,anchor=E)
shootscore_name_label = LeadLabel(str(scores5[0][1]))
shootscore_name_label.label.place(x=lead_width/2, y=400, anchor=CENTER)
shootscore_value_label = LeadLabel(str(scores5[0][0]))
shootscore_value_label.label.place(x=lead_width/2+150, y=400, anchor=E)


back_button = Button(lead, width=15, text='Back',font=('ar destine', 20),bg='MediumPurple3')
back_button.place(x=lead_width/2, y=500, anchor=CENTER)
back_button.config(state=NORMAL,disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=GROOVE)
back_button.config(command=back)


mainloop()