from __future__ import division

import pygame

import knightsTour as KT

pygame.init()

pygame.display.set_caption("Knights Tour")

windowSize = H, W = [560, 560]
screen = pygame.display.set_mode([W+80, H+200])
black = pygame.color.Color('#9fa8da')
white = pygame.color.Color('#fafafa')
grey = pygame.color.Color('#ffffff')
clock = pygame.time.Clock()
count = 0
done = False


# scale(Surface, (width, height),)

imageObject = pygame.image.load('media/knight.png')
knightRect = imageObject.get_rect()


def drawKnight(position, sY, sX):
    if position == tourd[-1]:
        knightRect.center = (sY + (sqrW/2), sX + (sqrH/2))
        screen.blit(imageObject, knightRect)


def drawColorOverlay(position, sY, sX):
    atColor = ((37, 225, 158, 100) if position == tourd[0] or
                position == tourd[-1] else (230, 81, 84, 100))
    rect = pygame.Surface((sqrW, sqrH), pygame.SRCALPHA, 32)
    rect.fill(atColor)
    screen.blit(rect, (sY, sX))


def drawBoard(tourd, size):
    if tour:
        tourd.append(tour.pop(0))
    for x in range(size):
        drawNotation(numbers, x)
        drawNotation(letters, x)
        for y in range(size):
            sY = sqrW * y + 40
            sX = sqrH * x + 40
            position = (x, y)
            sqrColor = white if not x % 2 else black
            if not y % 2:
                sqrColor = white if sqrColor is black else black
            pygame.draw.rect(screen, sqrColor, (sY, sX, sqrW, sqrH))

            if position in tourd: 
                drawColorOverlay(position, sY, sX)
            if position == tourd[-1]: 
                drawKnight(position, sY, sX)
    return tourd


letters = "abcdefghi"
numbers = "123456789"

def tupleToChess(position):
    x, y = position
    return letters[y] + numbers[size-x-1]

def drawNotation(charset, p):

    notations = myfont2.render(charset[p], True, (99, 99, 99))
    inc = p * sqrH + 40 + sqrH / 2
    const = 0 + padd * 2
    if charset == numbers:
        X = const
        Y = inc
    else:
        X = inc - 5
        Y = const - 5
    screen.blit(notations, (X, Y))


def printTour(tour, cindex):

    tourText = [tupleToChess(t) for t in tour]
    lineheight = 20
    offset = H + padd + 60
    lineNum = 1
    displayText = ""
    ttext = []
    for i, x in enumerate(tourText):

        if i == cindex-1:
            displayText += "[ " + x + " ], "
        else:
            displayText += x + ",  "
        if (i + 1) % 18 == 0:
            ttext = myfont3.render(displayText, True, (99, 99, 99))
            screen.blit(ttext, (0 + 40, offset + lineheight * lineNum))
            lineNum += 1
            displayText = ""
    ttext = myfont3.render(displayText, True, (99, 99, 99))
    screen.blit(ttext, (0 + 40, offset + lineheight * lineNum))



if __name__ == '__main__':

    import sys

    

    start = (7,0)
    if len(sys.argv) >= 2:
        aStrt = sys.argv[1]
        if aStrt[0] in letters and aStrt[1] in numbers:
            y = letters.index(aStrt[0])
            x = numbers.index(aStrt[1])
            start = (x,y)


    size = int(sys.argv[2]) if len(sys.argv) == 3 else 8

    tour = KT.knightsTour(start, size)

    sqrW, sqrH = W / size, H / size

    pygame.font.init()
    myfont = pygame.font.SysFont('Roboto', 30)
    myfont2 = pygame.font.SysFont('Roboto', 26)
    myfont3 = pygame.font.SysFont('Roboto', 24)
    padd = 8

    tourd = []
    Tcount = 1
    tourrep = tour[:]
    while not done:  
        
        screen.fill(grey)
        tourd = drawBoard(tourd, size)
        textsurface = myfont.render("Tour: %s" % Tcount, True, (33, 33, 33))
        screen.blit(textsurface, (0 + 40, H + 60))
        printTour(tourrep, len(tourd))
        if not tour:
            Tcount += 1
            tour = KT.knightsTour(tourd[-1], size)
            tourd = []
            tourrep = tour[:]
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        clock.tick(3)
    pygame.quit()

