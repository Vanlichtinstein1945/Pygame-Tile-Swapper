"""
    TKINTER AND PYGAME GROUP PROJECT

    --- LEVEL 1 ---

    Patrick, Brenan
"""
import sys, pygame, random
import Level2
#import EndingMenu

def Level1Start(t, w, h, f):
    pygame.init()
    Level1Object = Level1(t, w, h, f)
    Level1Object.startLevel()

# Function for setting sub-images of a given image
def clip(image, x, y, width, height):
    subImage = image.copy()
    clipRect = pygame.Rect(x, y, width, height)
    subImage.set_clip(clipRect)
    newImage = image.subsurface(subImage.get_clip())
    return newImage.copy()

class Level1:
    # Function for setting variables
    def __init__(self, t, w, h, f):
        self.TITLE = t
        self.WIDTH = w
        self.HEIGHT = h
        self.FRAMERATE = f
        self.WIDTHFACTOR = .39
        self.HEIGHTFACTOR = .07
        self.CLOCK = pygame.time.Clock()
        self.DELTATIME = 0
        self.MYFONT = pygame.font.SysFont('Arial', 30)
        self.SCREEN = None
        self.mouseX = 0
        self.mouseY = 0
        self.offsetX = 0
        self.offsetY = 0
        self.testImage = pygame.image.load('images/test.png')
        self.imageWidth = self.testImage.get_width()
        self.imageHeight = self.testImage.get_height()
        self.cutImage = [clip(self.testImage, 0, 0, self.imageWidth/2, self.imageHeight/2),
                         clip(self.testImage, self.imageWidth/2, 0, self.imageWidth/2, self.imageHeight/2),
                         clip(self.testImage, 0, self.imageHeight/2, self.imageWidth/2, self.imageHeight/2),
                         clip(self.testImage, self.imageWidth/2, self.imageHeight/2, self.imageWidth/2, self.imageHeight/2)]
        self.slot = [[self.WIDTH/2-self.imageWidth/2, self.HEIGHT/2-self.imageHeight/2],
                     [self.WIDTH/2-self.imageWidth/2+self.imageWidth/2, self.HEIGHT/2-self.imageHeight/2],
                     [self.WIDTH/2-self.imageWidth/2, self.HEIGHT/2],
                     [self.WIDTH/2-self.imageWidth/2+self.imageWidth/2, self.HEIGHT/2]]
        self.imageRects = [pygame.rect.Rect(self.slot[0][0], self.slot[0][1], self.imageWidth/2, self.imageHeight/2),
                           pygame.rect.Rect(self.slot[1][0], self.slot[1][1], self.imageWidth/2, self.imageHeight/2),
                           pygame.rect.Rect(self.slot[2][0], self.slot[2][1], self.imageWidth/2, self.imageHeight/2),
                           pygame.rect.Rect(self.slot[3][0], self.slot[3][1], self.imageWidth/2, self.imageHeight/2)]
        self.draggings = [False, False, False, False]
        self.imageSlotPos = [0, 1, 2, 3]
        while self.imageSlotPos == [0, 1, 2, 3]:
            random.shuffle(self.imageSlotPos)
        self.currRect = pygame.rect.Rect(0, 0, 0, 0)
    
    # Function for creating the main pygame window
    def startLevel(self):
        self.SCREEN = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption(self.TITLE)
        self.SCREEN.fill(pygame.Color("White"))
        self.main()

    # Function for handling the main backend of the game and main loop
    def main(self):
        while True:
            self.grabControls()
            self.drawOnScreen()
            self.updateScreenAndVars()
            self.checkWin()

    # Function for grabbing pygame events like keypresses
    def grabControls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Testing if mouse is pressed on image
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in range(len(self.imageRects)):
                        if self.imageRects[i].collidepoint(event.pos):
                            self.draggings[i] = True
                            self.mouseX, self.mouseY = event.pos
                            self.offsetX = self.imageRects[i].x - self.mouseX
                            self.offsetY = self.imageRects[i].y - self.mouseY
                            self.currRect = self.imageRects[i].copy()
            # Updating events based on image location
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for i in range(len(self.draggings)):
                        if self.draggings[i] == True:
                            found = False
                            self.draggings[i] = False
                            for j in range(len(self.imageRects)):
                                if self.imageRects[i].colliderect(self.imageRects[j]) and self.imageRects[j] != self.imageRects[i] and not found:
                                    tempSlotPos = self.imageSlotPos[i]
                                    self.imageSlotPos[i] = self.imageSlotPos[j]
                                    self.imageSlotPos[j] = tempSlotPos
                                    found = True
                            self.imageRects[i] = self.currRect
            # Updating image location to match mouse pos
            if event.type == pygame.MOUSEMOTION:
                for i in range(len(self.draggings)):
                    if self.draggings[i] == True:
                        self.mouseX, self.mouseY = event.pos
                        self.imageRects[i].x = self.mouseX + self.offsetX
                        self.imageRects[i].y = self.mouseY + self.offsetY

    # Function for drawing on the pygame display
    def drawOnScreen(self):
        self.SCREEN.fill(pygame.Color("White"))

        fpsText = self.MYFONT.render(str(int(self.CLOCK.get_fps())), True, pygame.Color("Black"))
        fpsTextRect = fpsText.get_rect()
        fpsTextRect.center = [self.WIDTHFACTOR+30, self.HEIGHTFACTOR+30]
        self.SCREEN.blit(fpsText, fpsTextRect)

        # Looping through twice so grabbed image is on top
        for i in range(len(self.draggings)):
            if not self.draggings[i]:
                self.SCREEN.blit(self.cutImage[self.imageSlotPos[i]], self.slot[i])

        for i in range(len(self.draggings)):
            if self.draggings[i]:
                self.SCREEN.blit(self.cutImage[self.imageSlotPos[i]], [self.imageRects[i].x, self.imageRects[i].y])

    # Function to update the screen with whatever moved or was newly drawn this frame
    def updateScreenAndVars(self):
        pygame.display.flip()
        self.DELTATIME = self.CLOCK.tick(self.FRAMERATE)

    # Function for checking if a win condition is met and starting LevelX.startGame()
    def checkWin(self):
        if self.imageSlotPos == [0, 1, 2, 3]:
            pygame.quit()
            try:
                Level2.Level2Start(self.TITLE, self.WIDTH, self.HEIGHT, self.FRAMERATE)
            except:
                EndingMenu.createMenuFromLevel()

# Sets default values for testing if not launched from MainMenu.py
if __name__ == "__main__":
    Level1Start("DEFAULT", 1280, 720, 30)
