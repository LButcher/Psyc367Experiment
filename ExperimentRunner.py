import pygame
import os
import random
#Our class to write data to csv
from DataWriter import DataWriter

#Screen load location
x = 0
y = 25

#Colour Constants (R,G,B)
BLACK = (0,0,0)
WHITE = (255,255,255)

#Pygame stuff
clock = pygame.time.Clock()
closed = False

#Experiment Data
#testData keyed by 'size':'user inputs'
age = input("Enter participant's age: \n")
gender = input("Enter participant's gender: \n")
stats = {
    'age':[age],
    'gender':[gender]
    }
trialSize = 20
testData = {141:[],
            144:[],
            147:[],
            150:[],
            153:[],
            156:[],
            159:[]}

completeAnswers = {}

#To make sure pygame screen is loaded in right place
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#Initialize Pygame game engine
pygame.init()


#Creating the window
screen_size = (1280, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PSYC 367 Experiment")
screen.fill(WHITE)

#Draw Text (Words, x location, y location, font size, colour)
def drawText(text,x,y,size,col):
    font=pygame.font.Font(None,size)
    textRender=font.render(text, 1,col)
    screen.blit(textRender, (x,y))

#Check if allowed to use that circle (circle size)
def checkSize(size):
    return len(testData[size])<trialSize
        

#Get our random circle size from available testData options
def getCircle():
    found = False
    goodCircle = None
    while not found:

        if 0<len(list(testData.keys())):
            possibleCircle = random.choice(list(testData.keys()))
        else:
            return None;
            ######## === END
        if checkSize(possibleCircle):
            found = True
            goodCircle = possibleCircle
        else:
            completeAnswers.update({possibleCircle:testData[possibleCircle]})
            del testData[possibleCircle]
    return goodCircle


#Get stuck in loop here to avoid refreshing
#Only finishes if user inputs 0 or 1
def waitForInput():
    answered = False
    while not answered:
        #User Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                closed = True
                answered=True
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN and (event.unicode=='0' or event.unicode == '1'):     
                testData[testCircle].append(event.unicode)
                answered=True
                drawScreen(0)
                pygame.display.flip()
                pygame.time.delay(500)

                
#Draws circles and other drawings onto screen
def drawScreen(testCircle):
    #Screen Clear
    screen.fill(WHITE)
    #Title
    drawText("Press 1 if Reference is larger, 0 if Test Circle is larger",
             200,150,50,BLACK)
    #Refence Circle Info
    drawText("Reference Circle",125,250,50,BLACK)
    pygame.draw.circle(screen, BLACK, (275,500),150)
    #Test Circle Info
    drawText("Test Circle",900,250,50,BLACK)
    pygame.draw.circle(screen, BLACK, (1000,500),testCircle)

    
#*******Main*******
while not closed:

    #Add Drawings to screen
    if 0<len(list(testData.keys())):
        testCircle = getCircle()
    else:
        testCircle = None
    if type(testCircle)==int:
        drawScreen(testCircle)
    else:
        print("Done Trials")
        closed= True
    
    #Screen update
    pygame.display.flip()
    #Limiting to 60fps
    clock.tick(60)

    #Wait for user to input before refreshing, then add input to data
    if not closed:
        waitForInput()
            
##Write to file here
dataFile = DataWriter(completeAnswers,stats)
dataFile.writeToCsv()

pygame.display.quit()
pygame.quit()
