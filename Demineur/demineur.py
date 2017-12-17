from Tkinter import *
from random import randint
from PIL import Image, ImageTk
root = Tk()

can = Canvas(root, width = 1920, height = 1080)
can.grid()

image = Image.open("grid.png")
gridTexture = ImageTk.PhotoImage(image)

image = Image.open("0.png")
mine0 = ImageTk.PhotoImage(image)

image = Image.open("1.png")
mine1 = ImageTk.PhotoImage(image)

image = Image.open("2.png")
mine2 = ImageTk.PhotoImage(image)

image = Image.open("3.png")
mine3 = ImageTk.PhotoImage(image)

image= Image.open("4.png")
mine4 = ImageTk.PhotoImage(image)

image = Image.open("5.png")
mine5 = ImageTk.PhotoImage(image)

image = Image.open("6.png")
mine6 = ImageTk.PhotoImage(image)

image = Image.open("7.png")
mine7 = ImageTk.PhotoImage(image)

image = Image.open("8.png")
mine8 = ImageTk.PhotoImage(image)

image = Image.open("_0.png")
digit0 = ImageTk.PhotoImage(image)

image = Image.open("_1.png")
digit1 = ImageTk.PhotoImage(image)

image = Image.open("_2.png")
digit2 = ImageTk.PhotoImage(image)

image = Image.open("_3.png")
digit3 = ImageTk.PhotoImage(image)

image= Image.open("_4.png")
digit4 = ImageTk.PhotoImage(image)

image = Image.open("_5.png")
digit5 = ImageTk.PhotoImage(image)

image = Image.open("_6.png")
digit6 = ImageTk.PhotoImage(image)

image = Image.open("_7.png")
digit7 = ImageTk.PhotoImage(image)

image = Image.open("_8.png")
digit8 = ImageTk.PhotoImage(image)

image = Image.open("_9.png")
digit9 = ImageTk.PhotoImage(image)

image = Image.open("flag.png")
flag = ImageTk.PhotoImage(image)

image = Image.open("mine.png")
mineTexture = ImageTk.PhotoImage(image)

global grid
grid=[ [0 for i in range (20)] for j in range(20)]

global playerGrid
playerGrid=[ [11 for i in range (20)] for j in range(20)]



mines = 0

while mines != 50:
    x = randint(0, 19)
    y = randint(0, 19)
    if grid[x][y] == 0:
        mines += 1
        grid[x][y] = 9 #Les 9 sont des mines, les autres chiffres sont le nombre de mines qui entourent la case

global mineCountdown
mineCountdown = mines

can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit5)
can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit0)

def drawGrid():
    for j in range(20):
        for i in range (20):
            can.create_image(j * 50, i * 50, anchor = NW, image=gridTexture)

def showMines():

    i = -1
    for column in grid:
        i+=1
        j = -1
        for frame in column:
            j+=1
            if frame == 0:
                counter = mines(i, j)
                
                if counter != 0:
                    grid[i][j] = counter
        
def mines(i, j):

    counter = 0 
    if i+1 <= 19:
        if grid[i+1][j] == 9:
            counter+=1
    if i+1 <= 19 and j+1 <= 19:
        if grid[i+1][j+1] == 9:
            counter+=1
    if j+1 <= 19:
        if grid[i][j+1] == 9:
            counter+=1
    if 0 <= i-1 and 0 <= j-1:        
        if grid[i-1][j-1] == 9:
            counter+=1
    if 0 <= i-1:
        if grid[i-1][j] == 9:
            counter+=1
    if 0 <= j-1:
        if grid[i][j-1] == 9:
            counter+=1
    if 0 <= i-1 and j+1 <= 19:
        if grid[i-1][j+1] == 9:
            counter+=1
    if 0 <= j-1 and i+1 <= 19:
        if grid[i+1][j-1] == 9:
            counter+=1

    return counter
    
    
def rightClick(evt):

    global mineCountdown
    
    j = int(evt.x / 50)
    i = int(evt.y / 50)
    if playerGrid[i][j] == "flag":
        playerGrid[i][j] = 11
        can.create_image(j * 50, i * 50, anchor = NW, image=gridTexture)
        mineCountdown += 1
        
    elif playerGrid[i][j] == 11:
        can.create_image(j * 50, i * 50, anchor = NW, image=flag)
        playerGrid[i][j] = "flag"
        mineCountdown -= 1

    showMinesLeft()

    
    
def leftClick(evt):
    j = int(evt.x / 50)
    i = int(evt.y / 50)
    x = whatDigit(i, j)
    if x == 0:
        spread(i,j)
    else:
        printMines(i, j)

def showMinesLeft():

    firstDigit = mineCountdown/10
    lastDigit = mineCountdown%10
    
    if firstDigit == 9:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit9)
    elif firstDigit == 8:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit8)
    elif firstDigit == 7:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit7)
    elif firstDigit == 6:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit6)
    elif firstDigit == 5:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit5)
    elif firstDigit == 4:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit4)
    elif firstDigit == 3:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit3)
    elif firstDigit ==2:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit2)
    elif firstDigit == 1:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit1)
    elif firstDigit == 0:
        can.create_image(25 * 50, 10 * 50, anchor = NW, image=digit0)

    if lastDigit == 9:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit9)
    elif lastDigit == 8:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit8)
    elif lastDigit == 7:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit7)
    elif lastDigit == 6:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit6)
    elif lastDigit == 5:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit5)
    elif lastDigit == 4:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit4)
    elif lastDigit == 3:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit3)
    elif lastDigit == 2:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit2)
    elif lastDigit == 1:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit1)
    elif lastDigit == 0:
        can.create_image(25 * 50 + 50, 10 * 50, anchor = NW, image=digit0)

    
def printMines(i, j):

    x = grid[i][j]

    if x == 1:
        can.create_image(j * 50, i * 50, anchor = NW, image=mine1)
        playerGrid[i][j] = 1
    if x == 2:
        can.create_image(j * 50, i * 50, anchor = NW, image=mine2)
        playerGrid[i][j] = 2
    if x == 3:
        can.create_image(j * 50, i * 50, anchor = NW, image=mine3)
        playerGrid[i][j] = 3
    if x == 4:
        can.create_image(j * 50, i * 50, anchor = NW, image=mine4)
        playerGrid[i][j] = 4
    if x == 5:
        can.create_image(j * 50, i * 50, anchor = NW, image=mine5)
        playerGrid[i][j] = 5
    if x == 6:
        can.create_image(j * 50, i * 50, anchor = NW, image=mine6)
        playerGrid[i][j] = 6
    if x == 7:
        can.create_image(j * 50, i * 50, anchor = NW, image=mine7)
        playerGrid[i][j] = 7
    if x == 8:
        can.create_image(j * 50, i * 50, anchor = NW, image=mine8)
        playerGrid[i][j] = 8
    if x == 9:
        playerGrid[i][j] = 9
        can.create_image(j * 50, i * 50, anchor = NW, image=mineTexture)


def whatDigit(i, j):
    x = grid[i][j]
    return x

def spread(i ,j):

    can.create_image(j * 50, i * 50, anchor = NW, image=mine0)
    if playerGrid[i][j] !=0:
        
        playerGrid[i][j] = 0
        if i < 19:
            if grid[i+1][j] == 0:
                spread(i+1, j)
            else:
                printMines(i+1, j)
        if j < 19:
            if grid[i][j+1] == 0:
                spread(i, j+1)
            else:
                printMines(i, j+1)
        if i > 0:
            if grid[i-1][j] == 0:
                spread(i-1, j)
            else:
                printMines(i-1, j)
        if j > 0:
            if grid[i][j-1] == 0:
                spread(i, j-1)
            else:
                printMines(i, j-1)
        if i < 19 and j < 19:
            if grid[i+1][j+1] == 0:
                spread(i+1, j+1)
            else:
                printMines(i+1, j+1)
        if i < 19 and j > 0:
            if grid[i+1][j-1] == 0:
                spread(i+1, j-1)
            else:
                printMines(i+1, j-1)
        if i > 0 and j > 0:
            if grid[i-1][j-1] == 0:
                spread(i-1, j-1)
            else:
                printMines(i-1, j-1)
        if i > 0 and j < 19:
            if grid[i-1][j+1] == 0:
                spread(i-1,j+1)
            else:
                printMines(i-1, j+1)

drawGrid()
showMines()
for i in grid:
    print i
    
can.bind("<Button-3>", rightClick)
can.bind("<Button-1>", leftClick)

root.mainloop()
