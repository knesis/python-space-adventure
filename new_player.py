from Tkinter import *

newplayer_width = 500
newplayer_height = 400

newplayer = Toplevel()
newplayer.geometry('%dx%d+%d+%d' % (newplayer_width,
                               newplayer_height,
                               newplayer.winfo_screenwidth()/2 - newplayer_width/2,
                               newplayer.winfo_screenheight()/2 - newplayer_height/2))
newplayer.title('New Profile')
newplayer.resizable(0,0)

def back():
    global newplayer
    global create_button
    name_entry.config(state=NORMAL)
    create_button.config(text='Create', command=createnew)
    newplayer.destroy()


def createnew():
    global menu, newplayer, info_n_label
    global name_entry, create_button
    global profile_main
    global overwrite, no_overwrite
    import pickle, os
    # Check for special characters in profile name
    if (name_entry.get()).replace(' ', '').isalnum() != True:
        info_n_label.config(text='No special characters allowed.')
        return
    if len(name_entry.get()) > 12:
        info_n_label.config(text='Profile Name - 12 Character Max')
        return
    nprofile = {'name': name_entry.get(), 'score1':0, 'score2':0, 'score3':0, 'score4':0, 'score5':0}
    npath = 'profiles\\' + name_entry.get() + '.p'
    if os.path.isfile(os.path.join(os.getcwd(),npath)):
        info_n_label.config(text='Name Taken. Overwrite?')
        name_entry.config(state=DISABLED)
        back_button.config(text='No', command=no_overwrite)
        create_button.config(text='Yes', command=overwrite)
        return
    pickle.dump(nprofile, open(npath, 'wb'))
    profile_main = nprofile
    newplayer.quit()
    newplayer.destroy()
    menu.withdraw()
    execfile('python_final_map.py')

def overwrite():
    global menu, newplayer, info_n_label
    global name_entry, create_button
    global profile_main
    global createnew
    import pickle
    # Use pickle here to create new file from name
    nprofile = {'name': name_entry.get(), 'score1':0, 'score2':0, 'score3':0, 'score4':0, 'score5':0}
    npath = 'profiles\\' + name_entry.get() + '.p'
    pickle.dump(nprofile, open(npath, 'wb'))
    profile_main = nprofile
    name_entry.config(state=NORMAL)
    create_button.config(text='Create', command=createnew)
    newplayer.quit()
    newplayer.destroy()
    menu.withdraw()
    execfile('python_final_map.py')

def no_overwrite():
    global menu, newplayer, info_n_label
    global name_entry, create_button, back_button
    global profile_main
    global createnew, back
    info_n_label.config(text='Please enter new player name.')
    name_entry.config(state=NORMAL)
    name_entry.delete(0, END)
    name_entry.insert(0, 'Enter Name:')
    create_button.config(text='Create', command=createnew)
    back_button.config(text='Back', command=back)


newplayer_background = PhotoImage(file='images/space_small.gif')

newplayer_canvas = Canvas(newplayer, width=newplayer_width, height=newplayer_height)
newplayer_canvas.create_image(0,0, image=newplayer_background, anchor=NW)
newplayer_canvas.place(x=0,y=0)


title_label = Label(newplayer, padx=16, text='New Profile', font=('ar destine', 24), fg='MediumPurple4', bg='black')
title_label.place(x=newplayer_width/2, y=50,anchor=CENTER)

name_entry = Entry(newplayer, bg='black', fg='MediumPurple4', font=('ar destine', 24), justify=CENTER)
name_entry.config(insertbackground='MediumPurple4', selectbackground='MediumPurple4')
name_entry.insert(0, 'Enter Name:')
name_entry.place(x=newplayer_width/2, y=150, anchor=CENTER)

create_button = Button(newplayer, width=10, text='Create',font=('ar destine', 20),bg='MediumPurple3')
create_button.place(x=newplayer_width/2-100, y=250, anchor=CENTER)
create_button.config(state=NORMAL,disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=GROOVE)
create_button.config(command=createnew)

back_button = Button(newplayer, width=10, text='Back',font=('ar destine', 20),bg='MediumPurple3')
back_button.place(x=newplayer_width/2+100, y=250, anchor=CENTER)
back_button.config(state=NORMAL,disabledforeground='MediumPurple4',activebackground='MediumPurple1', relief=GROOVE)
back_button.config(command=back)

info_n_label = Label(newplayer, text='Please enter new player name.',font=('ar destine', 16), fg='MediumPurple4', bg='black')
info_n_label.place(x=0, y=newplayer_height, relwidth=1.0, anchor=SW)

mainloop()
