"""
    TKINTER AND PYGAME GROUP PROJECT

    --- ENDING MENU ---

    Flanders, Ian Alexander
    Patrick, Brenan
"""
from functools import partial
from tkinter import messagebox
import tkinter as tk
import tkinter.font as font
import sys

# Global variables
GAMETITLE = "Sample Text"
RESOLUTIONS = ["1280x720", "1920x1080", "2560x1440"]
WIDTH = 1280
HEIGHT = 720
FRAMERATE = 30
FRAMES = {}

# Function for creating the base tkinter window
def createBaseWindow():
    root = tk.Tk()
    root.title(GAMETITLE)
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    wInfo = [int((screenWidth/2) - (WIDTH/2)), int((screenHeight/2) - (HEIGHT/2))]
    root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, wInfo[0], wInfo[1]))

    return root

# Function for creating a frame to place buttons and widgets onto
def createBaseFrame(root):
    frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
    
    return frame

# Function for creating buttons onto the tkinter window
def createButton(base, MYFONT, buttonText, buttonCommand, buttonSide, buttonPadYTop, buttonPadYBottom):
    button = tk.Button(base, text=buttonText, width=int(.016*WIDTH), height=int(.00125*HEIGHT), command=buttonCommand)
    button.pack(side=buttonSide, pady=(buttonPadYTop, buttonPadYBottom))
    button["font"] = MYFONT

# Function that sets up the frame for the main menu design
def createMenu(root, MYFONT):
    menuFrame = createBaseFrame(root)
    FRAMES["menu"] = menuFrame

    quitButton = createButton(menuFrame, MYFONT, "Quit", root.destroy, tk.BOTTOM, 0, 0)
    winningLabel = tk.Label(menuFrame, text="You Win!", width=int(.016*WIDTH), height=int(.00125*HEIGHT))
    winningLabel.pack(side=tk.BOTTOM, pady=(.5*HEIGHT, .016*HEIGHT))
    winningLabel["font"] = MYFONT

# Function for hiding all frames except the one specified by 'frame' to be opened
def openFrame(frame):
    for key, value in FRAMES.items():
        if key == frame:
            value.pack()
        else:
            value.pack_forget()

# Function for creating the a new Ending Menu
def createMenuFromLevel():
    root = createBaseWindow()
    MYFONT = font.Font(size=30)
    createMenu(root, MYFONT)
    openFrame("menu")
    root.mainloop()
    sys.exit()

# Setup and running of the window when MainMenu.py is the first file launched
if __name__ == "__main__":
    createMenuFromLevel()
