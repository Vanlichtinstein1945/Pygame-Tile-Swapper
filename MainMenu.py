"""
    TKINTER AND PYGAME GROUP PROJECT

    --- MAIN MENU ---

    Flanders, Ian Alexander
    Patrick, Brenan
"""
from functools import partial
from tkinter import messagebox
import tkinter as tk
import tkinter.font as font
import sys, Level1

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
def createBaseFrame():
    frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
    
    return frame

# Function for creating buttons onto the tkinter window
def createButton(base, buttonText, buttonCommand, buttonSide, buttonPadYTop, buttonPadYBottom):
    button = tk.Button(base, text=buttonText, width=int(.016*WIDTH), height=int(.00125*HEIGHT), command=buttonCommand)
    button.pack(side=buttonSide, pady=(buttonPadYTop, buttonPadYBottom))
    button["font"] = MYFONT

# Function that sets up the frame for the main menu design
def createMenu():
    menuFrame = createBaseFrame()
    FRAMES["menu"] = menuFrame

    quitButton = createButton(menuFrame, "Quit", root.destroy, tk.BOTTOM, 0, 0)
    settingsButton = createButton(menuFrame, "Settings", partial(openFrame, "settings"), tk.BOTTOM, 0, .016*HEIGHT)
    startButton = createButton(menuFrame, "Start", gameStart, tk.BOTTOM, .5*HEIGHT, .016*HEIGHT)

# Function that sets up the frame for the settings design
def createSettings():
    settingsFrame = createBaseFrame()
    FRAMES["settings"] = settingsFrame

    backButton = createButton(settingsFrame, "Back", partial(openFrame, "menu"), tk.BOTTOM, 0, 0)

    framerateFrame = tk.Frame(settingsFrame)
    framerateTick = tk.Scale(framerateFrame, from_=15, to=144, orient=tk.HORIZONTAL)
    framerateTick.set(FRAMERATE)
    framerateTick.config(font=MYFONT)
    framerateLabel = tk.Label(framerateFrame, text="Framerate:")
    framerateLabel.config(font=MYFONT)

    variable = tk.StringVar(settingsFrame)
    variable.set(str(WIDTH) + "x" + str(HEIGHT))
    varArr = [variable, framerateTick]
    
    applyButton = createButton(settingsFrame, "Apply", partial(applySettings, varArr), tk.BOTTOM, 0, .016*HEIGHT)

    framerateTick.pack(side=tk.RIGHT, padx=(10, 0))
    framerateLabel.pack(side=tk.LEFT, padx=(0, 10))
    framerateFrame.pack(side=tk.BOTTOM, pady=(0, .016*HEIGHT))

    dropboxFrame = tk.Frame(settingsFrame)
    dropboxLabel = tk.Label(dropboxFrame, text="Resolution:")
    dropboxLabel.config(font=MYFONT)
    dropboxLabel.pack(side=tk.LEFT, padx=(0, 10))
    dropboxBox = tk.OptionMenu(dropboxFrame, variable, *RESOLUTIONS)
    dropboxBox.pack(side=tk.RIGHT, padx=(10, 0))
    dropboxBox.config(font=MYFONT)
    dropboxBoxName = dropboxFrame.nametowidget(dropboxBox.menuname)
    dropboxBoxName.config(font=MYFONT)
    dropboxFrame.pack(side=tk.BOTTOM, pady=(.45*HEIGHT, .016*HEIGHT))

# Function for applying options changed in the 'settings' menu
def applySettings(varArr):
    global WIDTH, HEIGHT, FRAMERATE
    tempWidth = WIDTH
    tempHeight = HEIGHT
    tempFramerate = FRAMERATE
    WIDTH, HEIGHT = map(int, varArr[0].get().split("x"))
    FRAMERATE = int(varArr[1].get())
    resetWindow("settings")
    apply = messagebox.askquestion("Apply Settings", "Keep the current settings?")
    if apply == "no":
        WIDTH, HEIGHT = tempWidth, tempHeight
        FRAMERATE = tempFramerate
        resetWindow("settings")
    root.mainloop()
    
# Function for resetting the window in instances like resolution update
def resetWindow(openingFrame):
    global root, MYFONT
    root.destroy()
    root = createBaseWindow()
    MYFONT = font.Font(size=30)
    createMenu()
    createSettings()
    openFrame(openingFrame)

# Function for hiding all frames except the one specified by 'frame' to be opened
def openFrame(frame):
    for key, value in FRAMES.items():
        if key == frame:
            value.pack()
        else:
            value.pack_forget()

# Function that kills the tkinter window and loads level 1
def gameStart():
    root.destroy()
    Level1.Level1Start(GAMETITLE, WIDTH, HEIGHT, FRAMERATE)

# Setup and running of the window when MainMenu.py is the first file launched
if __name__ == "__main__":
    root = createBaseWindow()
    MYFONT = font.Font(size=30)
    createMenu()
    createSettings()
    openFrame("menu")
    root.mainloop()
    sys.exit()
