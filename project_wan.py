from Tkinter import *
from PIL import Image, ImageTk
import pickle

# Eric Wan - Space Quiz - Earth

root = Toplevel()
root.title("Space Multiple Choice Questions")
root.geometry('%dx%d+%d+%d' % (1920,
                               1080,
                               root.winfo_screenwidth()/2 - 1920/2,
                               root.winfo_screenheight()/2 - 1080/2))


name = profile_main['name']               # Player Name
score1 = profile_main['score1']           # Score for Asteroid Minigame
score2 = profile_main['score2']           # Score for Simon Minigame
score3 = profile_main['score3']           # Score for Multiple Choice Minigame
score4 = profile_main['score4']           # Score for Minesweeper Minigame
score5 = profile_main['score5']           # Score for Shooting Minigame


# The question and answers text
Message = StringVar()
Message.set("empty")
AnsAlpha = StringVar()
AnsAlpha.set("empty")
AnsBravo = StringVar()
AnsBravo.set("empty")
AnsCharlie = StringVar()
AnsCharlie.set("empty")
AnsDelta = StringVar()
AnsDelta.set("empty")
AnsEcho = StringVar()
AnsEcho.set("empty")

# Right or wrong text
RightOrWrong = StringVar()
RightOrWrong.set("Were you correct or incorrect?")
YouRight = "Your selection was correct!"
YouWrong = "Your selection was incorrect!"

#
CorrectInt = -1
Attempts = 0
Tries = IntVar()
Tries.set(Attempts)
index = 0

# All the buttons and what they do
def ButtonA():
    print "Button A was pressed"
    global CorrectInt, Attempts
    global index, YouRight, YouWrong
    global RightOrWrong, GameFinished, Tries, Next_Q, ImageIndex
    if 0 == CorrectInt:
        RightOrWrong.set(YouRight)
        Attempts += 1
        Tries.set(Attempts)
        if index >= 9:
            GameFinished()
        else:
            index += 1
            Next_Q()
            ImageIndex()
    else:
        RightOrWrong.set(YouWrong)
        Attempts += 1
        Tries.set(Attempts)
def ButtonB():
    print "Button B was pressed"
    global CorrectInt, Attempts
    global index, YouRight, YouWrong
    global RightOrWrong, GameFinished, Tries, Next_Q, ImageIndex
    if 1 == CorrectInt:
        RightOrWrong.set(YouRight)
        Attempts += 1
        Tries.set(Attempts)
        if index >= 9:
            GameFinished()
        else:
            index += 1
            Next_Q()
            ImageIndex()
    else:
        RightOrWrong.set(YouWrong)
        Attempts += 1
        Tries.set(Attempts)
def ButtonC():
    print "Button C was pressed"
    global CorrectInt, Attempts
    global index, YouRight, YouWrong
    global RightOrWrong, GameFinished, Tries, Next_Q, ImageIndex
    if 2 == CorrectInt:
        RightOrWrong.set(YouRight)
        Attempts += 1
        Tries.set(Attempts)
        if index >= 9:
            GameFinished()
        else:
            index += 1
            Next_Q()
            ImageIndex()
    else:
        RightOrWrong.set(YouWrong)
        Attempts += 1
        Tries.set(Attempts)
def ButtonD():
    print "Button D was pressed"
    global CorrectInt, Attempts
    global index, YouRight, YouWrong
    global RightOrWrong, GameFinished, Tries, Next_Q, ImageIndex
    if 3 == CorrectInt:
        RightOrWrong.set(YouRight)
        Attempts += 1
        Tries.set(Attempts)
        if index >= 9:
            GameFinished()
        else:
            index += 1
            Next_Q()
            ImageIndex()
    else:
        RightOrWrong.set(YouWrong)
        Attempts += 1
        Tries.set(Attempts)
def ButtonE():
    print "Button E was pressed"
    global CorrectInt, Attempts
    global index, YouRight, YouWrong
    global RightOrWrong, GameFinished, Tries, Next_Q, ImageIndex
    if 4 == CorrectInt:
        RightOrWrong.set(YouRight)
        Attempts += 1
        Tries.set(Attempts)
        if index >= 9:
            GameFinished()
        else:
            index += 1
            Next_Q()
            ImageIndex()
    else:
        RightOrWrong.set(YouWrong)
        Attempts += 1
        Tries.set(Attempts)
        print Attempts


# The next question
def Next_Q():
    global index
    global CorrectInt
    global Questions, QuestionLabel
    global Message, AnsAlpha, AnsBravo, AnsCharlie, AnsDelta, AnsEcho
    QuestionLabel.config(text="Question Number: #%s" %str(index+1), font=('ocr a std', 10), )
    Message.set(Questions[index][0])
    AnsAlpha.set(Questions[index][1][0])
    AnsBravo.set(Questions[index][1][1])
    AnsCharlie.set(Questions[index][1][2])
    AnsDelta.set(Questions[index][1][3])
    AnsEcho.set(Questions[index][1][4])
    CorrectInt = Questions[index][2]
    #print CorrectInt


#Ends game; displays attempt counter
def GameFinished():
    global profile_main, Attempts
    global name, score1, score2, score3, score4, score5
    import pickle
    root.destroy()
    newroot = Toplevel()
    newroot.title("Attempts Count")
    newroot.geometry('%dx%d+%d+%d' % (450,
                                   100,
                                   newroot.winfo_screenwidth() / 2 - 225,
                                   newroot.winfo_screenheight() / 2 - 50))
    NewAttempts = Attempts
    NewAttemptsLabel = Label(newroot, font=('ocr a std', 10), text = "Your final number of attempts:")
    NewAttemptsLabel.grid(row = 0, column = 0)
    NewAttemptsNumberLabel = Label(newroot, font=('ocr a std', 10), text=NewAttempts)
    NewAttemptsNumberLabel.grid(row = 0, column = 1)
    ScoreLabel = Label(newroot, font=('ocr a std', 10), text = "Your final score is:")
    ScoreLabel.grid(row = 1, column = 0)
    final_score = (50 - NewAttempts) * 10
    ScoreValueLabel = Label(newroot, font=('ocr a std', 10), text = final_score)
    ScoreValueLabel.grid(row = 1, column = 1)
    # Adding score to profile
    score3 = max(score3, final_score)
    nprofile = {'name': name, 'score1': score1, 'score2': score2, 'score3': score3, 'score4': score4, 'score5': score5}
    spath = 'profiles\\' + name + '.p'
    pickle.dump(nprofile, open(spath, 'wb'))
    profile_main = nprofile
    # score screen showing calculations for score
    newroot.mainloop()


# Loading in Images
# All images taken from NASA Image of the Day Gallery; hyperlinks provided below
# https://www.nasa.gov/multimedia/guidelines/index.html
# https://www.nasa.gov/multimedia/imagegallery/iotd.html
Image1 = Image.open("images/Image1.jpg")
Photo1 = ImageTk.PhotoImage(Image1)
Image2 = Image.open("images/Image2.jpg")
Photo2 = ImageTk.PhotoImage(Image2)
Image3 = Image.open("images/Image3.jpg")
Photo3 = ImageTk.PhotoImage(Image3)
Image4 = Image.open("images/Image4.jpg")
Photo4 = ImageTk.PhotoImage(Image4)
Image5 = Image.open("images/Image5.jpg")
Photo5 = ImageTk.PhotoImage(Image5)
Image6 = Image.open("images/Image6.jpg")
Photo6 = ImageTk.PhotoImage(Image6)
Image7 = Image.open("images/Image7.jpg")
Photo7 = ImageTk.PhotoImage(Image7)
Image8 = Image.open("images/Image8.jpg")
Photo8 = ImageTk.PhotoImage(Image8)
Image9 = Image.open("images/Image9.jpg")
Photo9 = ImageTk.PhotoImage(Image9)
Image10 = Image.open("images/Image10.jpg")
Photo10 = ImageTk.PhotoImage(Image10)
ChosenPhoto = Photo1
ImageLabel = Label(root, image=ChosenPhoto)

# Changes image display
def ImageIndex():
    global index
    global ChosenPhoto, ImageLabel, root
    global Photo1, Photo2, Photo3, Photo4, Photo5, Photo6, Photo7, Photo8, Photo9, Photo10
    ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 0:
        ImageLabel.destroy()
        ChosenPhoto = Photo1
        ImageLabel = Label(root, image=ChosenPhoto)
        ImageLabel.image = Photo1
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 1:
        ImageLabel.destroy()
        ChosenPhoto = Photo2
        ImageLabel = Label(root, image=ChosenPhoto)
        ImageLabel.image = Photo2
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 2:
        ImageLabel.destroy()
        ChosenPhoto = Photo3
        ImageLabel = Label(root, image=ChosenPhoto)
        ImageLabel.image = Photo3
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 3:
        ChosenPhoto = Photo4
        ImageLabel.config(image=ChosenPhoto)
        ImageLabel.image = Photo4
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 4:
        ChosenPhoto = Photo5
        ImageLabel.config(image=ChosenPhoto)
        ImageLabel.image = Photo5
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 5:
        ChosenPhoto = Photo6
        ImageLabel.config(image=ChosenPhoto)
        ImageLabel.image = Photo6
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 6:
        ChosenPhoto = Photo7
        ImageLabel.config(image=ChosenPhoto)
        ImageLabel.image = Photo7
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 7:
        ChosenPhoto = Photo8
        ImageLabel.config(image=ChosenPhoto)
        ImageLabel.image = Photo8
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 8:
        ChosenPhoto = Photo9
        ImageLabel.config(image=ChosenPhoto)
        ImageLabel.image = Photo9
        ImageLabel.grid(row=4, column=0, rowspan=5)
    if index == 9:
        ChosenPhoto = Photo10
        ImageLabel.config(image=ChosenPhoto)
        ImageLabel.image = Photo10
        ImageLabel.grid(row=4, column=0, rowspan=5)


# Questions
# All gathered from the hyperlink below
# http://www.orau.gov/orise/sciencebowl/questions/astrset2.pdf
Q1 = ["Which Apollo flight was the first manned landing on the moon?", ["Apollo 13", "Apollo 8", "Apollo 11", "Apollo 10", "Apollo 12"], 2]
Q2 = ["Which planet seems to be turned on its side with an axis tilt of 98 degrees?", ["Pluto", "Neptune", "Saturn", "Mars", "Uranus"], 4]
Q3 = ["The period from one full moon to the next is:", ["30.3 days", "30 days", "29.5 days", "28 days", "25 days"], 2]
Q4 = ["The andromeda Galaxy is which of the following types of galaxies?", ["Elliptical", "Spiral", "Barred - Spiral", "Irregular", "Circular"], 1]
Q5 = ["In the Milky Way there are approximately", ["2 million stars", "100 million stars", "400 million stars", "200 billion stars", "over 9000 stars"], 3]
Q6 = ["PRESENTLY, what is the farthest planet from the sun?", ["Neptune", "Pluto", "Uranus", "Saturn", "None of the above"], 0]
Q7 = ["Andromeda, the nearest galaxy which is similar to the Milky Way, is how far from the Earth?", ["200,000 light years", "2,000,000 light years", "20,000,000 light years", "200,000,000 light years", "200,000,000,000 light years"], 1]
Q8 = ["The comet known as Halley's Comet has an average period of:", ["56 years", "66 years", "96 years", "86 years", "76 years"], 4]
Q9 = ["Which one of the following planets has no moons?", ["Mars", "Neptune", "Venus", "Jupiter", "Earth"], 2]
Q10 = ["In kilometers, the earth's average distance from the sun is roughly which of the following distances?", ["250 million", "91 million", "150 million", "350 million", "100 million"], 2]
Questions = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]

# All the text labels needed for the question and buttons
QuestionLabel = Label(root, text = "Question Number: #1", font=('ocr a std', 10))
QuestionLabel.grid(row = 0, column = 0, columnspan = 5)
QuestionTextLabel = Label(root, font=('ocr a std', 10), textvariable = Message)
QuestionTextLabel.grid(row = 1, column = 0, rowspan = 2, columnspan = 5)
AttemptsLabel = Label(root, text = "Your number of attempts:",font=('ocr a std', 10), justify = RIGHT)
AttemptsLabel.grid(row = 0, column = 6)
AttemptsNumberLabel= Label(root, textvariable = Tries, font=('ocr a std', 10), justify = LEFT)
AttemptsNumberLabel.grid(row = 0, column = 7)
CorrectnessLabel = Label(root, textvariable = RightOrWrong, font=('ocr a std', 10), justify = LEFT)
CorrectnessLabel.grid(row = 1, column = 6, columnspan = 2)

BlankSpaceLabel = Label(root, text = " ")
BlankSpaceLabel.grid(row = 3, column = 0, columnspan = 7)
LabelChoiceA = Label(root, textvariable = AnsAlpha, font=('ocr a std', 10), justify = LEFT)
LabelChoiceA.grid(row = 4, column = 7)
LabelChoiceB = Label(root, textvariable = AnsBravo, font=('ocr a std', 10), justify = LEFT)
LabelChoiceB.grid(row = 5, column = 7)
LabelChoiceC = Label(root, textvariable = AnsCharlie, font=('ocr a std', 10), justify = LEFT)
LabelChoiceC.grid(row = 6, column = 7)
LabelChoiceD = Label(root, textvariable = AnsDelta, font=('ocr a std', 10), justify = LEFT)
LabelChoiceD.grid(row = 7, column = 7)
LabelChoiceE = Label(root, textvariable = AnsEcho, font=('ocr a std', 10), justify = LEFT)
LabelChoiceE.grid(row = 8, column = 7)

# All the labeled buttons to click
AnsAlpha_Button = Button(root, text = "A", font=('ocr a std', 12), command = ButtonA, bg='RoyalBlue3')
AnsAlpha_Button.grid(row = 4, column = 6, ipadx = 50, ipady = 50)
AnsBravo_Button = Button(root, text = "B", font=('ocr a std', 12), command = ButtonB, bg='RoyalBlue3')
AnsBravo_Button.grid(row = 5, column = 6, ipadx = 50, ipady = 50)
AnsCharlie_Button = Button(root, text = "C", font=('ocr a std', 12), command = ButtonC, bg='RoyalBlue3')
AnsCharlie_Button.grid(row = 6, column = 6, ipadx = 50, ipady = 50)
AnsDelta_Button = Button(root, text = "D", font=('ocr a std', 12), command = ButtonD, bg='RoyalBlue3')
AnsDelta_Button.grid(row = 7, column = 6, ipadx = 50, ipady = 50)
AnsEcho_Button = Button(root, text = "E", font=('ocr a std', 12), command = ButtonE, bg='RoyalBlue3')
AnsEcho_Button.grid(row = 8, column = 6, ipadx = 50, ipady = 50)

Next_Q()
ImageIndex()


root.mainloop()