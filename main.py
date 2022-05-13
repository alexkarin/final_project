import random
from tkinter import *

from PIL import Image, ImageTk


# Start Button <--------
###### choose number of rounds, quit button, or play as long as you wish. still add quit button
#### keep track of score but clear last rounds choice
# i don't like the text box, id rather have something like " x wins"  and an update on score count
# contents of window should expand with window


# game class that handles all scores, and player moves #
class Game:
    def __init__(self):
        self._name = None
        self.playerScore = 0
        self.computerScore = 0
        self.draw = 0
        self.window = None
        #self.label = None
        self.computer_label = None
        self.player_label = None
        self.draw_label = None


    def show_window(self):
        # labels the window
        self.window = Toplevel(master)
        self.window.title("Rock Paper Scissors")
        # sets the window size
        self.window.geometry("400x500")
        self.window.resizable(height = 0, width = 0) #

        # changes the background color
        self.window.configure(bg='light blue')
        self.label = Text(self.window, height=10, width=30)
        # score label for computer
        self.computer_label = Label(self.window, text=" Computer: ")
        self.computer_label.place(x=75, y=175)
        # score label for Player
        self.player_label = Label(self.window, text=" Player: ")
        self.player_label.place(x=250, y=175)

        # number of draws
        self.draw_label = Label(self.window, text="Draw: ")
        # playerLabel.place(x=90,y=120)

        #label(text="any text here", font=('Helvetica', '14')


        # Creates a rock button
        rock_image = Image.open(r"images\Rock.png")
        rock_image = rock_image.resize((80, 90))
        rock = ImageTk.PhotoImage(rock_image)

        # lambda will execute commands one by one
        rock_button = Button(
            self.window,
            image=rock,
            command=lambda: [self.display("rock"), self.play_computer("rock")]
        )

        # places rock  the button
        rock_button.place(x=60, y=50,)

        # Creates a paper button
        paper_image = Image.open(r"images\paper.png")
        paper_image = paper_image.resize((80, 90))
        paper = ImageTk.PhotoImage(paper_image)

        # lambda will execute commands one by one
        paper_button = Button(
            self.window,
            image=paper,
            command=lambda: [self.display("paper"), self.play_computer("paper")]
        )

        # places the paper button
        paper_button.place(x=155, y=50)

        # Creates a scissors button
        scissors_image = Image.open(r"images\scissors.png")
        scissors_image = scissors_image.resize((80, 90))
        scissors = ImageTk.PhotoImage(scissors_image)

        # lambda will execute commands one by one
        scissors_button = Button(
            self.window,
            image=scissors,
            command=lambda: [self.display("scissors"), self.play_computer("scissors")]
        )

        # places the scissors button
        scissors_button.place(x=250, y=50)

        # places the textbox widget   get rid of this
        self.label.place(x=40, y=220)  #  this is the text box

        #Label  for  buttons
        import tkinter as tk

        class ToolTip(object):
            def __init__(self, widget, text):
                self.widget = widget
                self.text = text

                def enter(event):
                    self.showTooltip()

                def leave(event):
                    self.hideTooltip()

                widget.bind('<Enter>', enter)
                widget.bind('<Leave>', leave)

            def showTooltip(self):
                self.tooltipwindow = tw = tk.Toplevel(self.widget)
                tw.wm_overrideredirect(1)  # window without border and no normal means of closing
                tw.wm_geometry("+{}+{}".format(self.widget.winfo_rootx(), self.widget.winfo_rooty()))
                label = tk.Label(tw, text=self.text, background="#ffffe0", relief='solid', borderwidth=1).pack()

            def hideTooltip(self):
                tw = self.tooltipwindow
                tw.destroy()
                self.tooltipwindow = None

                from tooltip import ToolTip

                root = tk.Tk()
                # this is the call for the button label
                your_widget = rock_button(root,text="Rock")
                ToolTip(widget=your_widget, text="Rock")

        ##Button to reset the Game## ##not added yet##


        self.window.mainloop()

    def display(self, name):
        self._name = name
        print(self._name)
        self.label.insert(1.0, "Your choice: {}".format(name) + '\n')

# Computer choice  PLayer Choice
    def play_computer(self, player):
        options = ["rock", "paper", "scissors"]
        num = random.randint(0, 2)
        self.label.insert(1.0, "Computers choice: {}".format(options[num] + '\n'))
        self.label.insert(1.0, player + '\n')


        if player == "rock" and options[num] == "scissors":
            self.playerScore = self.playerScore + 1
            self.label.insert(1.0, "Player beat computer with ", player + '\n')
            #self.player_label['text'] = ("Player: ", self.playerScore)

        elif player == "rock" and options[num] == "paper":
            self.computerScore = self.computerScore + 1
            self.label.insert(1.0, "Computer beat player with ", player + '\n')
           # self.computer_label['text'] = ("Computer: ", self.computerScore)

        elif player == "rock" and options[num] == "rock":
            self.label.insert(1.0, "Draw" + '\n')
            self.draw = self.draw + 1
            #self.draw_label['text'] = ("draw: ", self.draw)
        elif player == "paper" and options[num] == "rock":
            self.playerScore = self.playerScore + 1
            self.player_label['text'] = ("Player: ", self.playerScore)
            #self.label.insert(1.0, "Player beat computer with ", player + '\n')
#
        elif player == "paper" and options[num] == "paper":
            self.label.insert(1.0, "Draw" + '\n')
            self.draw = self.draw + 1
            #self.draw_label['text'] = ("draw: ", self.draw)
        elif player == "paper" and options[num] == "scissors":
            self.computerScore = self.computerScore + 1
            self.computer_label['text'] = ("Computer: ", self.computerScore)
            #self.label.insert(1.0, "Computer beat player with ", player + '\n')
        elif player == "scissors" and options[num] == "rock":
            self.computerScore = self.computerScore + 1
            self.computer_label['text'] = ("Computer: ", self.computerScore)
            #self.label.insert(1.0, "Computer beat player with ", player + '\n')
        elif player == "scissors" and options[num] == "paper":
            self.playerScore = self.playerScore + 1

            self.player_label['text'] = ("Player: ", self.playerScore)
            #self.label.insert(1.0, "Player beat computer with ", player + '\n')
        else:
            self.label.insert(1.0, "Draw" + '\n')
            self.draw = self.draw + 1
            #self.draw_label['text'] = ("draw: ", self.draw) ```

# instance of the game class
g = Game()

# creates a Tk() object
master = Tk()

# title
master.title("Start Rock Paper Scissors")

# sets the geometry of main
# root window
master.geometry('600x600')
# font
master.option_add('*Font', 'Times 15')
#master.resizable
label = Label(master,
              text="ROCK PAPER SCISSORS"
            )

label.pack(pady=55)


#'''Game Rules"
#"In this game 2 players throw a choice simultaneously  Rock,  Paper,  or  Scissors."
#"The rules of the game are  simple"
#"rock beats scissors"
#"paper beats rock"
#"scissors beats paper"
#"If players choose the same it is a draw and no points are awarded")'''
# You will play against the computer, the computer is not AI (yet) so  will choose at random.


# changes the background color
master.configure(bg='aliceblue')

# a button widget which will open
# new window on button click

start_button = Button(master,
             text="START",
             command=lambda: g.show_window())
start_button.pack(pady=80,)



master.mainloop()