import cv2
import numpy as np
import random

# define parameters
width=1366
height=768
x=0
y=0

class GameofLife:
    def __init__(self):
        self.menuButtoncolor=(250,250,250)
        self.menuoptioncolor=(200,200,200)
        self.myFont=cv2.FONT_HERSHEY_SIMPLEX
        self.menustate:bool=False
        self.play:bool=False
        self.userinput:bool=False
        self.randomstate:bool=False
        self.clearstate:bool=False
        self.clickstate:bool=False
        self.gridstate:bool=False
        self.alivecellcolour=(41, 204, 33)
        self.deadcellcolour=(30,30,30)

    # create random function
    def fillRandom(self,frame):
        x=np.zeros([height,width,3],dtype=np.uint8)
        for i in range(0,frame.shape[1],8):
            for j in range(0,frame.shape[0],8):
                if random.choice([0,1,0,0,0,0]):
                    frame[j:j+8,i:i+8]=self.alivecellcolour
        return x

    # generate next gen cells
    def generateNextgencells(self,layer1):
        x=self.createbackground()

        # left upper corner point
        s=0
        if layer1[12][4][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[4][12][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[12][12][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[4][4][0]==self.deadcellcolour[0]:
            if s==3:
                x[:8,:8]=self.alivecellcolour
        else:
            if not(s==2 or s==3):
                x[:8,:8]=self.deadcellcolour
        
        # right upper point
        s=0
        if layer1[4][width-8][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[12][width-8][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[12][width-4][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[4][width-4][0]==self.deadcellcolour[0]:
            if s==3:
                x[:8,1360:]=self.alivecellcolour
        else:
            if not(s==2 or s==3):
                x[:8,1360:]=self.deadcellcolour
        
        # lower left point
        s=0
        if layer1[height-12][4][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[height-12][12][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[height-4][12][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[height-4][4][0]==self.deadcellcolour[0]:
            if s==3:
                x[height-8:,:8]=self.alivecellcolour
        else:
            if not(s==2 or s==3):
                x[height-8:,:8]=self.deadcellcolour
        
        # lower right point
        s=0
        if layer1[height-12][width-4][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[height-12][width-8][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[height-4][width-8][0]==self.alivecellcolour[0]:
            s+=1
        if layer1[height-4][width-4][0]==self.deadcellcolour[0]:
            if s==3:
                x[height-8:,1360:]=self.alivecellcolour
        else:
            if not(s==2 or s==3):
                x[height-8:,1360:]=self.deadcellcolour
        
        # the topmost row
        for i in range(8,layer1.shape[1]-8,8):
            s=0
            if layer1[4][i-4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[4][i+12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[12][i-4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[12][i+12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[12][i+4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[4][i+4][0]==self.deadcellcolour[0]:
                if s==3:
                    x[:8,i:i+8]=self.alivecellcolour
            else:
                if not(s==2 or s==3):
                    x[:8,i:i+8]=self.deadcellcolour
        
        # the bottommost row
        for i in range(8,layer1.shape[1]-8,8):
            s=0
            if layer1[height-4][i-4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[height-4][i+12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[height-12][i-4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[height-12][i+4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[height-12][i+12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[height-4][i+4][0]==self.deadcellcolour[0]:
                if s==3:
                    x[height-8:,i:i+8]=self.alivecellcolour
            else:
                if not(s==2 or s==3):
                    x[height-8:,i:i+8]=self.deadcellcolour
        
        # the leftmost column
        for i in range(8,layer1.shape[0]-8,8):
            s=0
            if layer1[i-4][4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i-4][12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i+4][12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i+12][12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i+12][4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i+4][4][0]==self.deadcellcolour[0]:
                if s==3:
                    x[i:i+8,:8]=self.alivecellcolour
            else:
                if not(s==2 or s==3):
                    x[i:i+8,:8]=self.deadcellcolour
        
        # the rightmost column
        for i in range(8,layer1.shape[0]-8,8):
            s=0
            if layer1[i-4][width-4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i-4][width-12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i+4][width-12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i+12][width-12][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i+12][width-4][0]==self.alivecellcolour[0]:
                s+=1
            if layer1[i+4][width-4][0]==self.deadcellcolour[0]:
                if s==3:
                    x[i:i+8,1360:]=self.alivecellcolour
            else:
                if not(s==2 or s==3):
                    x[i:i+8,1360:]=self.deadcellcolour
        
        # the central region
        for i in range(8,layer1.shape[1]-8,8):
            for j in range(8,layer1.shape[0]-8,8):
                s=0
                if layer1[j-4][i-4][0]==self.alivecellcolour[0]:
                    s+=1
                if layer1[j+4][i-4][0]==self.alivecellcolour[0]:
                    s+=1
                if layer1[j+12][i-4][0]==self.alivecellcolour[0]:
                    s+=1
                if layer1[j+12][i+4][0]==self.alivecellcolour[0]:
                    s+=1
                if layer1[j+12][i+12][0]==self.alivecellcolour[0]:
                    s+=1
                if layer1[j+4][i+12][0]==self.alivecellcolour[0]:
                    s+=1
                if layer1[j-4][i+12][0]==self.alivecellcolour[0]:
                    s+=1
                if layer1[j-4][i+4][0]==self.alivecellcolour[0]:
                    s+=1
                if layer1[j+4][i+4][0]==self.deadcellcolour[0]:
                    if s==3:
                        x[j:j+8,i:i+8]=self.alivecellcolour
                else:
                    if not(s==2 or s==3):
                        x[j:j+8,i:i+8]=self.deadcellcolour
                    else:
                        x[j:j+8,i:i+8]=self.alivecellcolour

        return x

    # create background function
    def createbackground(self):
        background=np.zeros([height,width,3],dtype=np.uint8)

        # Change the background lightness
        background[:,:]=self.deadcellcolour
        
        return background
