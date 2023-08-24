import pygame
import sys
import numpy
import random
import time
import math

#Setting icon
icon = pygame.image.load('icon2.png')

pygame.display.set_icon(icon)

#Init
mainClock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Visualisierte Algorithmen")

screen = pygame.display.set_mode((700, 700),0,32)

#fonts and colors
titleFont = pygame.font.SysFont(None, 50, bold=True, italic=False)

subtitleFont = pygame.font.SysFont(None, 20, bold=False, italic=True)

menuFont = pygame.font.SysFont(None, 35, bold=False, italic=False)

smallButtonFont = pygame.font.SysFont(None, 30, bold=False, italic=False)

descriptionFont = pygame.font.SysFont(None, 40, bold=True, italic=False)

primaryColor = pygame.Color('0x1B2133')

secondaryColor = pygame.Color('0x354063')

highlightColor = pygame.Color('0x355C82')

barStandardColor = pygame.Color('0x849BBA')

barSelectedColor = pygame.Color('0xD14545')

barSuccesColor = pygame.Color('0x36BA5B')

barGreyedColor = pygame.Color('0xBECADA')

buttonBorderRadius = 15

arrowPolygon = ((0, 150), (100, 300), (100,200), (200,200), (200,100),(100,100), (100,0))





#Main logik
def menu():
     
     while True:

        buttonWidth = 400

        buttonHeight = 100

        screen.fill(primaryColor)
        
        #Draw Title Text
        drawText('Visualisierte Algorithmen', titleFont, (255, 255, 255), screen, 350, 30)

        drawText('von Finn Wolf', subtitleFont, (255,255,255), screen, 550, 55)

        #Create buttons
        button_1 = pygame.Rect(150, 100, buttonWidth, buttonHeight)

        button_2 = pygame.Rect(150, 250, buttonWidth, buttonHeight)

        button_3 = pygame.Rect(150, 400, buttonWidth, buttonHeight)

        button_4 = pygame.Rect(150, 550, buttonWidth, buttonHeight)

        #Draw buttons
        pygame.draw.rect(screen, secondaryColor, button_1, border_radius = buttonBorderRadius)

        pygame.draw.rect(screen, secondaryColor, button_2, border_radius = buttonBorderRadius)

        pygame.draw.rect(screen, secondaryColor, button_3, border_radius = buttonBorderRadius)

        pygame.draw.rect(screen, secondaryColor, button_4, border_radius = buttonBorderRadius)

        #Mouse position/collision logic
        mx, my = pygame.mouse.get_pos()

        if button_1.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, button_1, border_radius = buttonBorderRadius)

            if click:

                searchingAlgorythms()

        if button_2.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, button_2, border_radius = buttonBorderRadius)

            if click:

                pass

        if button_3.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, button_3, border_radius = buttonBorderRadius)

            if click:

                pass

        if button_4.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, button_4, border_radius = buttonBorderRadius)

            if click:

                pass

        #Event logic
        click = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        drawText('Suchalgorithmen', menuFont, (255,255,255), screen, 350, (100+(0*(buttonHeight+50))+(buttonHeight/2)))

        drawText('Sortieralgorithmen', menuFont, (255,255,255), screen, 350, (100+(1*(buttonHeight+50))+(buttonHeight/2)))

        drawText('Maze Algorithmen', menuFont, (255,255,255), screen, 350, (100+(2*(buttonHeight+50))+(buttonHeight/2)))

        drawText('Pathfinding Algorithmen', menuFont, (255,255,255), screen, 350, (100+(3*(buttonHeight+50))+(buttonHeight/2)))

        pygame.display.update()

        mainClock.tick(60)

def searchingAlgorythms():

    running = True

    processing = False #Is algorythm beeing processed?

    mode = 0

    modes = ("Linear", "Binary")

    speed = 1

    onSpeed = False #Is mouse on button? => for scroll wheel logik

    ellapsedTime = 0 #Time since last update

    size = 7

    onSize = False #Is mouse on button? => for scroll wheel logik

    data = createRandomArray(size=size) #Data array for diagram

    searchedNumber = data[random.randint(0, len(data)-1)]

    steps = 0 #Counts number of steps taken

    linearIndex = None

    binaryRange = [0, len(data)]

    binaryPivot = round((binaryRange[0] + binaryRange[1]) / 2)

    #Debugging
    print("size "+str(size))
    print("len "+str(len(data)))
    print("arr "+str(data))

    while running:

        #Drawing ui base
        screen.fill(primaryColor)
        
        backButton = pygame.Rect(50, 20, 100, 100)

        algoRect = pygame.Rect(50,140, 600, 420)

        algoChoice = pygame.Rect(50,580, 120, 100)

        speedChoice = pygame.Rect(190,580, 100, 100)

        sizeChoice = pygame.Rect(310,580, 100, 100)

        resetButton = pygame.Rect(430,580, 100, 100)

        startButton = pygame.Rect(550,580, 100, 100)

        pygame.draw.ellipse(screen, secondaryColor, backButton, width=0)

        pygame.draw.rect(screen, secondaryColor, algoRect, border_radius = buttonBorderRadius)

        pygame.draw.rect(screen, secondaryColor, algoChoice, border_radius = buttonBorderRadius)

        pygame.draw.rect(screen, secondaryColor, speedChoice, border_radius = buttonBorderRadius)

        pygame.draw.rect(screen, secondaryColor, sizeChoice, border_radius = buttonBorderRadius)

        pygame.draw.rect(screen, secondaryColor, resetButton, border_radius = buttonBorderRadius)

        pygame.draw.rect(screen, secondaryColor, startButton, border_radius = buttonBorderRadius)

        #Reseting values
        onSpeed = False

        onSize = False

        #Mouse position/collision logic
        mx, my = pygame.mouse.get_pos()

        if backButton.collidepoint((mx, my)):

            pygame.draw.ellipse(screen, highlightColor, backButton, width=0)

            if click:

                running = False

        if algoChoice.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, algoChoice, border_radius = buttonBorderRadius)

            if click:

                linearIndex = 0

                binaryRange = [0, len(data)]

                mode += 1

                if mode >= len(modes):

                    mode = 0

                #Reset important to update
                processing = False

                steps = 0

                linearIndex = None

                if mode == 0:

                    data = createRandomArray(size=size)

                elif mode == 1:

                    data = createSortedArray(size=size)

                    binaryRange = [0, len(data)]

                    binaryPivot = round((binaryRange[0] + binaryRange[1]) / 2)

                searchedNumber = data[random.randint(0, len(data)-1)]

        if speedChoice.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, speedChoice, border_radius = buttonBorderRadius)

            onSpeed = True

            if click:

                speed += 0.2

                if speed > 8:

                    speed = 0.2

        if sizeChoice.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, sizeChoice, border_radius = buttonBorderRadius)

            onSize = True

            if click:

                size += 1

                if size > 50:
                    
                    size = 1

        if resetButton.collidepoint((mx, my)):

            #always update reset in algo choice
            pygame.draw.rect(screen, highlightColor, resetButton, border_radius = buttonBorderRadius)

            if click:

                processing = False

                steps = 0

                linearIndex = None

                if mode == 0:

                    data = createRandomArray(size=size)

                elif mode == 1:

                    data = createSortedArray(size=size)

                searchedNumber = data[random.randint(0, len(data)-1)]

                binaryRange = [0, len(data)]

                binaryPivot = round((binaryRange[0] + binaryRange[1]) / 2)

        if startButton.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, startButton, border_radius = buttonBorderRadius)

            if click:

                if processing:

                    processing = False
                
                else:

                    processing = True
        
        #Drawing algorythm button text
        drawText(modes[mode]+"-", smallButtonFont, (255,255,255), screen, 110, 610)

        drawText("search", smallButtonFont, (255,255,255), screen, 110, 650)

        #Drawing speed button text
        drawText("Pause:", smallButtonFont, (255,255,255), screen, 240, 610)

        drawText(str(round(speed,1))+" Sek", smallButtonFont, (255,255,255), screen, 240, 650)

        #Drawing size button text
        drawText("Größe:", smallButtonFont, (255,255,255), screen, 360, 610)

        drawText(str(size), smallButtonFont, (255,255,255), screen, 360, 650)

        #Drawing reset button text
        drawText("Zurück-", smallButtonFont, (255,255,255), screen, 480, 610)

        drawText("setzen", smallButtonFont, (255,255,255), screen, 480, 650)

        #Processing algorythm
        if processing:

            drawText("Stop", smallButtonFont, (255,255,255), screen, 600, 630)

            #Check if pause has ellapsed and reset timer
            if ellapsedTime + speed <= time.time():

                ellapsedTime = time.time()

                #Check which mode to process
                if mode == 0:

                    if linearIndex == None:

                        linearIndex = 0

                    else:

                        linearIndex += 1

                    steps += 1
            
                    processing = processLinearSearch(data, linearIndex, searchedNumber)

                elif mode == 1:

                    #Determine pivot
                    binaryPivot = round((binaryRange[0] + binaryRange[1])/2)

                    steps += 1

                    binaryRange, processing = processBinarySearch(data, binaryRange, searchedNumber, binaryPivot)

        else:

            drawText("Start", smallButtonFont, (255,255,255), screen, 600, 630)

        #Draw algorythm state
        if mode == 0:
    
            drawLinearSearch(data, linearIndex, searchedNumber, steps)

        elif mode == 1:

            drawBinarySearch(data, binaryRange, searchedNumber, steps, binaryPivot)


        #Event logik
        click = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()

                sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    click = True

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 4:   

                    if onSize:

                        size -= 1

                        if size < 1:
                    
                            size = 50

                    if onSpeed:

                        speed -= 0.2

                        if speed < 0.2:

                            speed = 8


                if event.button == 5:   

                    if onSize:

                        size += 1

                        if size > 50:
                    
                             size = 1

                    if onSpeed:

                        speed += 0.20

                        if speed > 8:

                            speed = 0.2
        
        
        pygame.display.update()

        mainClock.tick(60)

def sortingAlgorythms():

    running = True

    while running:

        screen.fill(primaryColor)
        
        drawText('game', titleFont, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()

        mainClock.tick(60)

def mazeAlgorythms():

    running = True

    while running:

        screen.fill(primaryColor)

        #draw

        if button_1.collidepoint((mx, my)):

            pygame.draw.rect(screen, highlightColor, button_1, border_radius = buttonBorderRadius)

            if click:

                sortingAlgorythms()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()

        mainClock.tick(60)

def pathfindingAlgorythms():

    running = True

    while running:

        screen.fill(primaryColor)
        
        drawText('game', titleFont, (255, 255, 255), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()

        mainClock.tick(60)








#Helper
def drawText(text, font, color, surface, x, y):

    textobj = font.render(text, 1, color)

    textrect = textobj.get_rect()

    textrect.center = (x, y)

    surface.blit(textobj, textrect)

def createRandomArray(size):

    arr = []

    for index in range(0, size):

        arr.insert(index, index+1)

    numpy.random.shuffle(arr)

    return arr

def createSortedArray(size):

    arr = []

    for index in range(0, size):

        arr.insert(index, index+1)

    return arr



#Linear search
def drawLinearSearch(arr, currentIndex, searched, step):

    length = len(arr)

    #Dynamic font and space between bars
    if length > 40:

        space = 2

        font = pygame.font.SysFont(None, 15, bold=False, italic=False)

    elif length > 30:

        space = 5

        font = pygame.font.SysFont(None, 15, bold=False, italic=False)

    elif length > 20:

        space = 10

        font = pygame.font.SysFont(None, 15, bold=False, italic=False)

    elif length > 10:

        space = 20

        font = pygame.font.SysFont(None, 25, bold=False, italic=False)   

    else:

        space = 25

        font = pygame.font.SysFont(None, 30, bold=False, italic=False)

    #Necessary global bar calculations
    width = (560 - ((length-1) * space)) / length

    unitHeight = 330 / length

    description = "Gesucht " + str(searched)

    #Draw Bars
    for index in range(0,length):

        #Necessary individual bar calculations
        height = arr[index] * unitHeight

        xOffset = 70 + (index * (width + space))

        yOffset = 160 + 330 - height

        #Determine color 
        if index == currentIndex:

            if arr[index] == searched:

                #green
                tempRect = pygame.Rect(xOffset, yOffset, width, height)

                pygame.draw.rect(screen, barSuccesColor, tempRect)

                description = "Gesucht " + str(searched) + " - Step "  + str(step) + ": " + str(arr[index]) + " = " + str(searched)

            else:

                #red
                tempRect = pygame.Rect(xOffset, yOffset, width, height)

                pygame.draw.rect(screen, barSelectedColor, tempRect)

                description = "Gesucht " + str(searched) + " - Step "  + str(step) + ": " + str(arr[index]) + " != " + str(searched)

        else:

            #grey
            tempRect = pygame.Rect(xOffset, yOffset, width, height)

            pygame.draw.rect(screen, barStandardColor, tempRect)
        
        label = arr[index]

        drawText(str(label), font, (255,255,255), screen, xOffset+(width/2),515 )

    #Draw description text
    drawText(description, descriptionFont, (255,255,255), screen, 425, 70)

def processLinearSearch(arr, currentIndex, searched):

    if currentIndex >= len(arr):

        return False

    if arr[currentIndex] == searched:

        return False
    
    else:

        return True



#Binary search
def drawBinarySearch(arr, binaryRange, searched, step, pivot):

    length = len(arr)

    #Dynamic font and space between bars
    if length > 40:

        space = 2

        font = pygame.font.SysFont(None, 15, bold=False, italic=False)

    elif length > 30:

        space = 5

        font = pygame.font.SysFont(None, 15, bold=False, italic=False)

    elif length > 20:

        space = 10

        font = pygame.font.SysFont(None, 15, bold=False, italic=False)

    elif length > 10:

        space = 20

        font = pygame.font.SysFont(None, 25, bold=False, italic=False)   

    else:

        space = 25

        font = pygame.font.SysFont(None, 30, bold=False, italic=False)

    #Necessary global bar calculations
    width = (560 - ((length-1) * space)) / length

    unitHeight = 330 / length

    description = "Gesucht " + str(searched)

    #Draw Bars
    for index in range(0,length):

        #Necessary individual bar calculations
        height = arr[index] * unitHeight

        xOffset = 70 + (index * (width + space))

        yOffset = 160 + 330 - height

        #Determine color 
        #is in range?
        if index >= binaryRange[0] and index <= binaryRange[1]:
            
            #is pivot?
            if arr[index] == arr[pivot]:
                    
                if arr[index] == searched:

                    #green
                    tempRect = pygame.Rect(xOffset, yOffset, width, height)

                    pygame.draw.rect(screen, barSuccesColor, tempRect)

                    description = "Gesucht " + str(searched) + " - Step "  + str(step) + ": " + str(arr[pivot]) + " = " + str(searched)

                else:

                    #red
                    tempRect = pygame.Rect(xOffset, yOffset, width, height)

                    pygame.draw.rect(screen, barSelectedColor, tempRect)

                    if pivot < searched:

                        description = "Gesucht " + str(searched) + " - Step "  + str(step) + ": " + str(arr[pivot]) + " < " + str(searched)

                    elif pivot > searched:

                        description = "Gesucht " + str(searched) + " - Step "  + str(step) + ": " + str(arr[pivot]) + " > " + str(searched)

            else:

                #grey
                tempRect = pygame.Rect(xOffset, yOffset, width, height)

                pygame.draw.rect(screen, barStandardColor, tempRect)

        else:

                #greyed out
                tempRect = pygame.Rect(xOffset, yOffset, width, height)

                pygame.draw.rect(screen, barGreyedColor, tempRect)
        
        label = arr[index]

        drawText(str(label), font, (255,255,255), screen, xOffset+(width/2),515 )

    #Draw description text
    drawText(description, descriptionFont, (255,255,255), screen, 425, 70)

def processBinarySearch(arr, binaryRange, searched, pivot):

    if arr[pivot] == searched:

        return binaryRange, False
    
    elif arr[pivot] < searched:

        return [pivot, binaryRange[1]], True
    
    elif arr[pivot] > searched:

        return [binaryRange[0], pivot], True

menu()