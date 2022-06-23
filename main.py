
#! The Game of Life is a cellular automaton devised by Dr. John Conway in 1970.

#* The rules of life:
#* 1. Any live cell with fewer than two live neighbours dies, as if by needs
#* caused by underpopulation.
#* 2. Any live cell with more than three live neighbours dies, as if by overcrowding.
#* 3. Any live cell with two or three live neighbours lives, unchanged, to the next
#* generation.
#* 4. Any dead cell with exactly three live neighbours cells will come to life.

# import modules and libraries
import cv2
import random
from GameofLife import GameofLife

# define parameters
width=1366
height=768
x=0
y=0


# setup the mouse event call
def mouseEvent(evnt,X,Y,*args):
    global x,y
    if evnt==cv2.EVENT_LBUTTONDOWN:
        if X>=20 and X<=50 and Y>=height-50 and height-20:
            if game.menustate:
                game.menustate=False
            else:
                game.menustate=True
        
        elif game.menustate and X>=20 and X<=140 and Y>=height-150 and Y<=height-110:
            if game.play:
                game.play=False
            else:
                game.play=True
        
        elif X>=20 and X<=140 and Y>=height-200 and Y<=height-160:
            game.randomstate=True
        
        elif X>=20 and X<=140 and Y>=height-100 and Y<=height-60:
            game.clearstate=True
        
        elif X>=20 and X<=140 and Y>=height-250 and Y<=height-210:
            if game.gridstate:
                game.gridstate=False
            else:
                game.gridstate=True
        
        else:
            x=X-X%8
            y=Y-Y%8
            game.clickstate=True

game=GameofLife()

# set basic window property
cv2.namedWindow('Game of Life',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Game of Life',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.setMouseCallback('Game of Life', mouseEvent)

frame=game.createbackground()

# begin the program loop
while True:

    # create a temporary layer for non destructive work
    layer1=frame.copy()

    # creating grid lines
    if game.gridstate:
        for i in range(width):
            if i%8==0:
                cv2.line(layer1,(i,0),(i,height),(0,0,0),1)
        for i in range(height):
            if i%8==0:
                cv2.line(layer1,(0,i),(width,i),(0,0,0),1)

    # simulate the game
    if game.play:
        frame=game.generateNextgencells(layer1)
        layer1=frame.copy()

    # check the random button state
    if game.randomstate:
        frame=game.createbackground()
        layer1=game.fillRandom(frame)
        game.randomstate=False

    # check the clear state button
    if game.clearstate:
        frame=game.createbackground()
        game.clearstate=False
    
    # create alive cell if user clicks on the deadcell
    if not game.menustate and game.clickstate:
        if frame[y+4][x+4][0]==game.deadcellcolour[0]:
            frame[y:y+8,x:x+8]=game.alivecellcolour
        else:
            frame[y:y+8,x:x+8]=game.deadcellcolour
        game.clickstate=False
    
    # create the menu button
    cv2.rectangle(layer1,(20,height-50),(50,height-20),game.menuButtoncolor,-1)
    cv2.circle(layer1,(35,height-30),3,(0,0,0),-1)
    cv2.circle(layer1,(35,height-40),3,(0,0,0),-1)

    # show options if menustate is ON
    if game.menustate:
        cv2.rectangle(layer1,(20,height-250),(140,height-210),game.menuoptioncolor,-1)
        cv2.rectangle(layer1,(20,height-200),(140,height-160),game.menuoptioncolor,-1)
        cv2.rectangle(layer1,(20,height-150),(140,height-110),game.menuoptioncolor,-1)
        cv2.rectangle(layer1,(20,height-100),(140,height-60),game.menuoptioncolor,-1)
        cv2.putText(layer1,'Grid',(48,height-220),game.myFont,0.9,(0,0,0),2)
        cv2.putText(layer1,'Random',(23,height-170),game.myFont,0.9,(0,0,0),2)
        if game.play:
            cv2.putText(layer1,'Pause',(36,height-120),game.myFont,0.9,(0,0,0),2)
        else:
            cv2.putText(layer1,'Play',(48,height-120),game.myFont,0.9,(0,0,0),2)
        cv2.putText(layer1,'Clear',(40,height-70),game.myFont,0.9,(0,0,0),2)

    # output the processed frame
    cv2.imshow('Game of Life',layer1)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cv2.destroyAllWindows()