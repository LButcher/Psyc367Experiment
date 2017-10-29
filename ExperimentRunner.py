import pygame
import os
import random

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
testData = {'270':[],
            '280':[],
            '290':[],
            '300':[],
            '310':[],
            '320':[],
            '330':[]}
#Completed sizes are placed in tempData, removed from testData
tempData = {}

#To make sure pygame screen is loaded in right place
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#Initialize Pygame game engine
pygame.init()


#Creating the window
screen_size = (1920, 1080)
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
    return len(testData[size])<20

#Get our random circle size from available testData options


#*******Main*******
while not closed:

    #Screen Clear
    screen.fill(WHITE)

    #Drawings
    #Title
    drawText("Press 1 if Reference is larger, 0 if Test Circle is larger",
             500,150,50,BLACK)
    #Refence Circle Info
    drawText("Reference Circle",420,250,50,BLACK)
    pygame.draw.circle(screen, BLACK, (560,500),150)
    #Test Circle Info
    drawText("Test Circle",1250,250,50,BLACK)
    pygame.draw.circle(screen, BLACK, (1340,500),150)
    
    #Screen update
    pygame.display.flip()
    #Limiting to 60fps
    clock.tick(60)

    #User Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True
        if event.type == pygame.KEYDOWN:     
            print(event.unicode)
        
pygame.display.quit()
pygame.quit()
