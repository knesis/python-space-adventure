
from Tkinter import *
import os
import pickle

load_width = 500
load_height = 600

load = Toplevel()
load.geometry('%dx%d+%d+%d' % (load_width,
                               load_height,
                               load.winfo_screenwidth()/2 - load_width/2,
                               load.winfo_screenheight()/2 - load_height/2))
load.title('Load Profile')
load.resizable(0,0)

# Define profile directory
dprofile = dict()
profile_dir = os.getcwd() + '\profiles'
for file in os.listdir(profile_dir):
    f, e = os.path.splitext(file)
    dprofile.update({str(f): profile_dir + '\\' + file})
profile_names = dprofile.keys()
profile_names.sort()



def back():
    global load
    load.destroy()


def select():
    global load, info_l_label, info_label
    global profile_select, dprofile
    global profile_main
    import pickle
    # Use pickle here to take selection from listbox, decode into plaintext and return to main menu
    try:
        pselect = profile_select.get(profile_select.curselection())
    except TclError as e:
        info_l_label.config(text='Please select a profile.')
        return
    fprofile = dprofile[pselect]
    lprofile = pickle.load(open(fprofile, 'rb'))
    profile_main = lprofile
    info_label.config(text=('Welcome: ' + str(profile_main['name'])))
    continue_button.button.config(state=NORMAL)
    stat_button.button.config(state=NORMAL)
    load.quit()
    load.destroy()


load_image = PhotoImage(file='images/space_small.gif')

load_canvas = Canvas(load, width=load_width, height=load_height)
load_canvas.create_image(0,0, image=load_image,anchor=NW)
load_canvas.place(x=0,y=0)


title_label = Label(load, padx=16, text='Load Profile', font=('ar destine', 24), fg='MediumPurple4', bg='black')
title_label.place(x=load_width/2, y=50,anchor=CENTER)


listbox_frame = Frame(load)

# Scrollbar code adapted from http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/listbox-scrolling.html
profile_xscroll = Scrollbar(listbox_frame, orient=HORIZONTAL)
profile_yscroll = Scrollbar(listbox_frame, orient=VERTICAL)

profile_select = Listbox(listbox_frame)
for item in profile_names:
    profile_select.insert(END,item)
profile_select.config(font=('ar destine', 16), fg='MediumPurple4', bg='black')
profile_select.config(activestyle='none', selectbackground='MediumPurple4')

profile_select.config(xscrollcommand=profile_xscroll.set, yscrollcommand=profile_yscroll.set)
profile_xscroll.config(command=profile_select.xview)
profile_yscroll.config(command=profile_select.yview)

profile_xscroll.pack(side=BOTTOM, fill=X)
profile_yscroll.pack(side=RIGHT, fill=Y)
profile_select.pack()
listbox_frame.place(x=load_width/2, y=275, anchor=CENTER)



load_button = Button(load, width=10, text='Load',font=('ar destine', 20),bg='MediumPurple3')
load_button.place(x=load_width/2-100, y=500, anchor=CENTER)
load_button.config(state=NORMAL,disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=GROOVE)
load_button.config(command=select)

back_button = Button(load, width=10, text='Back',font=('ar destine', 20),bg='MediumPurple3')
back_button.place(x=load_width/2+100, y=500, anchor=CENTER)
back_button.config(state=NORMAL,disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=GROOVE)
back_button.config(command=back)

info_l_label = Label(load, text='Load Profile.',font=('ar destine', 16), fg='MediumPurple4', bg='black')
info_l_label.place(x=0, y=load_height, relwidth=1.0, anchor=SW)

mainloop()