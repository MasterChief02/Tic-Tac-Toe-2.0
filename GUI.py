## Importing External Dependencies
import pygame

## Importing Libraries
import OriginTechFont, Character

#######################################
#####     STANDALONE ELEM3NTS     #####
#######################################

#################
## Loading Bar ##
#################
class loadingBar(pygame.sprite.Sprite):
    ## Background Bar ##
    class background(pygame.sprite.Sprite):
        def __init__(self,rect):
            super(loadingBar.background,self).__init__()
            self.image=pygame.image.load("Assets\GUI\PNG\Loading_Bar\Table.png")
            self.image=pygame.transform.scale(self.image,(rect[2],rect[3]))
            self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
    
    ## Starting Bar ##
    class startBar(pygame.sprite.Sprite):
        def __init__(self,rect):
            super(loadingBar.startBar,self).__init__()
            self.image=pygame.image.load("Assets\GUI\PNG\Loading_Bar\Loading_Bar_3_1.png")
            self.image=pygame.transform.scale(self.image,(rect[2],rect[3]))
            self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
    
    ## Ending Bar ##
    class endBar(pygame.sprite.Sprite):
        def __init__(self,rect):
            super(loadingBar.endBar,self).__init__()
            self.image=pygame.image.load("Assets\GUI\PNG\Loading_Bar\Loading_Bar_3_3.png")
            self.image=pygame.transform.scale(self.image,(rect[2],rect[3]))
            self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
            self.initX=rect[0]
            self.counter=0
            self.barWidth=rect[2]
        
        def update(self):
            self.rect=pygame.Rect(self.initX+(self.counter-1)*self.barWidth,self.rect.y,self.rect.width,self.rect.height)
    
    ## Middle Bar ##
    class midBar(pygame.sprite.Sprite):
        def __init__(self,rect):
            super(loadingBar.midBar,self).__init__()
            self.image=pygame.image.load("Assets\GUI\PNG\Loading_Bar\Loading_Bar_3_2.png")
            self.image=pygame.transform.scale(self.image,(rect[2],rect[3]))
            self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])


    def __init__(self,rect,window,sections=10,margin=2):
        super(loadingBar,self).__init__()

        ## Loading Bar Attributes
        self.barWidth=(rect[2]-2*margin)//sections
        self.barHeight=rect[3]-2*margin
        self.counter=2
        self.window=window
        self.sections=sections

        ## Misc Operations
        self.spriteGroupObjectList=[self.background(rect),self.endBar((rect[0]+margin,rect[1]+margin,self.barWidth,self.barHeight)),self.startBar((rect[0]+margin,rect[1]+margin,self.barWidth,self.barHeight))]
        self.spriteGroup=pygame.sprite.Group(self.spriteGroupObjectList)
        self.spriteGroup.draw(window)
    
    def update(self):
        # Checking For Max Limit Of Counter
        if self.counter<=self.sections:
            # Changing Position of Ending Bar
            self.spriteGroupObjectList[1].counter=self.counter
            # Adding New Middle Bar If Needed
            if len(self.spriteGroupObjectList)!=self.counter+1:
                self.spriteGroupObjectList.append(self.midBar((self.spriteGroupObjectList[-1].rect.x+self.barWidth,self.spriteGroupObjectList[-1].rect.y,self.barWidth,self.barHeight)))
                self.spriteGroup=pygame.sprite.Group(self.spriteGroupObjectList)
        # Updating Spirite Group
        self.spriteGroup.update()
        self.spriteGroup.draw(self.window)


###############
## Input Box ##
###############
class inputBox():
    def __init__(self,rect,font,window,padding=(5,10,5,10),maxWords=5,textSize=24,textColor=(0,0,0),boxColor=(255,255,255),borderColor=(0,0,0),width=2,borderRadius=2,isPassword=False):
        ## Storing Attributes ##
        self.text=""
        self.maxWords=maxWords-1
        self.boxColor=boxColor
        self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
        self.width=width
        self.borderRadius=borderRadius
        self.borderColor=borderColor
        self.isPassword=isPassword
        if font=="OriginTech":
            self.textObject=OriginTechFont.originTechFont(self.text,(int(rect[0]+rect[2]//2),int(rect[1]+rect[3]//2)),window,textSize=textSize,textColor=textColor)
        self.isActive=False
        self.cursorPosition=0
        self.cursorVisible=False
        self.counter=0

        ## Creating Rectangles ##
        pygame.draw.rect(window,self.boxColor,rect=self.rect,border_radius=self.borderRadius)
        pygame.draw.rect(window,self.borderColor,rect=self.rect,width=self.width,border_radius=self.borderRadius)

    def update(self,window):
        ## Updating Rectangles ##
        pygame.draw.rect(window,self.boxColor,rect=self.rect,border_radius=self.borderRadius)
        pygame.draw.rect(window,self.borderColor,rect=self.rect,width=self.width,border_radius=self.borderRadius)
        ## Updates Variables ##
        if self.isActive:
            self.counter+=1
            if self.counter%8==0:
                self.cursorVisible=not(self.cursorVisible)
            if self.cursorVisible:
                if not(self.isPassword):
                    self.textObject.changeText(self.text[:self.cursorPosition]+"|"+self.text[self.cursorPosition:],window)
                else:
                    self.textObject.changeText("*"*len(self.text[:self.cursorPosition])+"|"+"*"*len(self.text[self.cursorPosition:]),window)
            else:
                if not(self.isPassword):
                    self.textObject.changeText(self.text,window)
                else:
                    self.textObject.changeText("*"*len(self.text),window)
        if self.isPassword:
            self.textObject.changeText("*"*len(self.text),window)
        self.textObject.update(window)
    
    def keyHandler(self,event,window):
        if self.isActive:
            ## Checking For Alpha Numeric Values
            if len(self.text)<=self.maxWords and event.key==pygame.K_0:
                self.text=self.text[:self.cursorPosition]+"0"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_1:
                self.text=self.text[:self.cursorPosition]+"1"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_2:
                self.text=self.text[:self.cursorPosition]+"2"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_3:
                self.text=self.text[:self.cursorPosition]+"3"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_4:
                self.text=self.text[:self.cursorPosition]+"4"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_5:
                self.text=self.text[:self.cursorPosition]+"5"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_6:
                self.text=self.text[:self.cursorPosition]+"6"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_7:
                self.text=self.text[:self.cursorPosition]+"7"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_8:
                self.text=self.text[:self.cursorPosition]+"8"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_9:
                self.text=self.text[:self.cursorPosition]+"9"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_a:
                self.text=self.text[:self.cursorPosition]+"a"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_b:
                self.text=self.text[:self.cursorPosition]+"b"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_c:
                self.text=self.text[:self.cursorPosition]+"c"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_d:
                self.text=self.text[:self.cursorPosition]+"d"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_e:
                self.text=self.text[:self.cursorPosition]+"e"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_f:
                self.text=self.text[:self.cursorPosition]+"f"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_g:
                self.text=self.text[:self.cursorPosition]+"g"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_h:
                self.text=self.text[:self.cursorPosition]+"h"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_i:
                self.text=self.text[:self.cursorPosition]+"i"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_j:
                self.text=self.text[:self.cursorPosition]+"j"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_k:
                self.text=self.text[:self.cursorPosition]+"k"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_l:
                self.text=self.text[:self.cursorPosition]+"l"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_m:
                self.text=self.text[:self.cursorPosition]+"m"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_n:
                self.text=self.text[:self.cursorPosition]+"n"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_o:
                self.text=self.text[:self.cursorPosition]+"o"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_p:
                self.text=self.text[:self.cursorPosition]+"p"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_r:
                self.text=self.text[:self.cursorPosition]+"r"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_s:
                self.text=self.text[:self.cursorPosition]+"s"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_t:
                self.text=self.text[:self.cursorPosition]+"t"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_u:
                self.text=self.text[:self.cursorPosition]+"u"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_v:
                self.text=self.text[:self.cursorPosition]+"v"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_w:
                self.text=self.text[:self.cursorPosition]+"w"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_x:
                self.text=self.text[:self.cursorPosition]+"x"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_y:
                self.text=self.text[:self.cursorPosition]+"y"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            elif len(self.text)<=self.maxWords and event.key==pygame.K_z:
                self.text=self.text[:self.cursorPosition]+"z"+self.text[self.cursorPosition:]
                self.cursorPosition+=1
            ## Checking For Movement Keys ##
            elif event.key==pygame.K_LEFT:
                if self.cursorPosition>0:
                    self.cursorPosition-=1
            elif event.key==pygame.K_RIGHT:
                if self.cursorPosition<len(self.text):
                    self.cursorPosition+=1
            ## Checking For Backspace And Delete Key ##
            elif event.key==pygame.K_BACKSPACE:
                if self.cursorPosition>0:
                    self.text=self.text[:self.cursorPosition-1]+self.text[self.cursorPosition:]
                    self.cursorPosition-=1
            elif event.key==pygame.K_DELETE:
                if self.cursorPosition<len(self.text):
                    self.text=self.text[:self.cursorPosition]+self.text[self.cursorPosition+1:]
            ## Updating The Text
            self.textObject.changeText(self.text,window)

    def mouseHandler(self,window):
        mousePosition=pygame.mouse.get_pos()
        self.isActive=self.rect.collidepoint(mousePosition[0],mousePosition[1])
        if not(self.isActive):
            self.textObject.changeText(self.text.replace("|",""),window)

    def eventHandler(self,events,window):
        for event in events:
            if event.type==pygame.KEYDOWN:
                self.keyHandler(event,window)
            if event.type==pygame.MOUSEBUTTONUP:
                self.mouseHandler(window)


########################################################
######      ELEMENTS TO BE USED WITH GUI GROUP     #####
########################################################

###############
## GUI Group ##
###############
class guiGroup():
    def __init__(self,guiObjects):
        self.guiObjects=guiObjects
    def update(self):
        for i in self.guiObjects:
            i.update()
    def draw(self,window):
        for i in self.guiObjects:
            i.draw(window)

class characterSelector():
    def __init__(self,rect,textSize=24,textColor=(240,240,240),margin=10,buttonSize=20,saveAllowed=False):
        ## Storing Attributes
        self.rect=rect
        self.margin=margin
        self.saveAllowed=saveAllowed
        ## Storing Heading Text
        self.textSize=textSize
        self.textColor=textColor
        self.charSelectionText=None
        ## Storing Character Display Box
        if saveAllowed:
            extraButtomMargin=textSize+margin
        else:
            extraButtomMargin=margin
        self.charObjectList=[Character.Kiaria((rect[0]+buttonSize+2*margin,rect[1]+textSize+2*margin,rect[2]-4*margin-2*buttonSize,rect[3]-textSize-2*margin-extraButtomMargin)),
                                  Character.Lochem((rect[0]+buttonSize+2*margin,rect[1]+textSize+2*margin,rect[2]-4*margin-2*buttonSize,rect[3]-textSize-2*margin-extraButtomMargin)),
                                  Character.Mayvheen((rect[0]+buttonSize+2*margin,rect[1]+textSize+2*margin,rect[2]-4*margin-2*buttonSize,rect[3]-textSize-2*margin-extraButtomMargin)),
                                  Character.Raymond((rect[0]+buttonSize+2*margin,rect[1]+textSize+2*margin,rect[2]-4*margin-2*buttonSize,rect[3]-textSize-2*margin-extraButtomMargin)),
                                  Character.Veera((rect[0]+buttonSize+2*margin,rect[1]+textSize+2*margin,rect[2]-4*margin-2*buttonSize,rect[3]-textSize-2*margin-extraButtomMargin))]
        self.currentObject=0
        ## Storing Navigation Buttons
        self.navLeftButtonObject=button((rect[0]+margin,rect[1]+(rect[2]-buttonSize)//2,buttonSize,buttonSize),"",bgImage="Assets\GUI\PNG\Hangar\Backward_BTN.png",borderWidth=-1)
        self.navRightButtonObject=button((rect[0]+rect[2]-margin-buttonSize,rect[1]+(rect[2]-buttonSize)//2,buttonSize,buttonSize),"",bgImage="Assets\GUI\PNG\Hangar\Forward_BTN.png",borderWidth=-1)
        self.navLeftButtonRect=pygame.Rect(rect[0]+margin,rect[1]+(rect[2]-buttonSize)//2,buttonSize,buttonSize)
        self.navRightButtonRect=pygame.Rect(rect[0]+rect[2]-margin-buttonSize,rect[1]+(rect[2]-buttonSize)//2,buttonSize,buttonSize)
    
    def update(self):
        ## Updating Current Selected Character
        self.charObjectList[self.currentObject].update()


    def draw(self,window):
        pygame.draw.rect(window,(240,240,240),pygame.Rect(self.rect[0],self.rect[1],self.rect[2],self.rect[3]),2)
        ## Drawing Heading Text
        if self.charSelectionText==None:
            self.charSelectionText=OriginTechFont.originTechFont("Select a character",(self.rect[0]+self.rect[2]//2,self.rect[1]+self.margin+self.textSize//2),window ,textSize=self.textSize,textColor=self.textColor)
        self.charSelectionText.update(window)
        ## Drawing Currently Selected Character
        self.charObjectList[self.currentObject].draw(window)
        self.navLeftButtonObject.draw(window)
        self.navRightButtonObject.draw(window)

    def mouseHandler(self):
        mousePosition=pygame.mouse.get_pos()
        if self.navLeftButtonRect.collidepoint(mousePosition[0],mousePosition[1]) and self.currentObject>0:
            self.currentObject-=1
        elif self.navRightButtonRect.collidepoint(mousePosition[0],mousePosition[1]) and self.currentObject<len(self.charObjectList)-1:
            self.currentObject+=1

    def eventHandler(self,events,window):
        for event in events:
            if event.type==pygame.MOUSEBUTTONUP:
                self.mouseHandler()

class button():
    def __init__(self,rect,text="",textSize=24,textColor=(240,240,240),margin=5,bgImage=None,bgColor=(0,0,0),borderColor=(240,240,240),borderWidth=2):
        ## Storing Attributes
        self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
        self.margin=margin
        ## Text Attributes
        self.text=text
        self.textSize=min(textSize,self.rect.height-2*self.margin)
        self.textColor=textColor
        self.textObject=None
        ## Box Attributes
        self.bgImage=bgImage
        self.bgColor=bgColor
        self.borderColor=borderColor
        self.borderWidth=borderWidth
        if self.bgImage!=None:
            self.bgImage=pygame.image.load(self.bgImage)
            self.bgImage=pygame.transform.scale(self.bgImage,(self.rect.width,self.rect.height))
    
    def update(self):
        pass

    def draw(self,window):
        ## Drawing Background
        pygame.draw.rect(window,self.bgColor,self.rect)
        if self.bgImage!=None:
            window.blit(self.bgImage,(self.rect.x,self.rect.y))
        pygame.draw.rect(window,self.borderColor,(self.rect.x-self.borderWidth,self.rect.y-self.borderWidth,self.rect.width+2*self.borderWidth,self.rect.height+2*self.borderWidth),width=self.borderWidth)
        ## Text
        if self.textObject==None:
            self.textObject=OriginTechFont.originTechFont(self.text,(self.rect.x+self.rect.width//2,self.rect.y+9*self.rect.height//20),window,textSize=self.textSize,textColor=self.textColor)
        self.textObject.update(window)

class board():
    def __init__(self,rect,borderWidth=2,borderColor=(240,240,240),userActive=True,circleColor=(50,50,250),crossColor=(50,250,50),winLineColor=(100,100,100),winLineSpeed=5,autoRotate=False):
        ## Storing Attributes
        self.rect=rect
        self.borderWidth=borderWidth
        self.borderColor=borderColor
        self.currentMoves=[]
        self.userActive=userActive
        self.isEven=userActive
        self.circleColor=circleColor
        self.crossColor=crossColor
        self.gameEnded=False
        self.autoRotate=autoRotate

        ## Storing Winner Data
        self.winner=None
        self.winLineStored=[(0,0),(0,0)]
        self.winLineCurrent=[(0,0),(0,0)]
        self.winLineOrientation="H"      ## H->Horizontal; V->Vertical; S(+/-)->Slant
        self.winLineColor=winLineColor
        self.winLineSpeed=winLineSpeed
        self.winTextObject=None

        ## Storing Rectangles For Boxes 1..9 In Order
        self.rectList=[pygame.Rect(rect[0],rect[1],rect[2]//3,rect[3]//3),pygame.Rect(rect[0]+rect[2]//3,rect[1],rect[2]//3,rect[3]//3),pygame.Rect(rect[0]+2*rect[2]//3,rect[1],rect[2]//3,rect[3]//3),pygame.Rect(rect[0],rect[1]+rect[3]//3,rect[2]//3,rect[3]//3),pygame.Rect(rect[0]+rect[2]//3,rect[1]+rect[3]//3,rect[2]//3,rect[3]//3),pygame.Rect(rect[0]+2*rect[2]//3,rect[1]+rect[3]//3,rect[2]//3,rect[3]//3),pygame.Rect(rect[0],rect[1]+2*rect[3]//3,rect[2]//3,rect[3]//3),pygame.Rect(rect[0]+rect[2]//3,rect[1]+2*rect[3]//3,rect[2]//3,rect[3]//3),pygame.Rect(rect[0]+2*rect[2]//3,rect[1]+2*rect[3]//3,rect[2]//3,rect[3]//3)]
    
    def draw(self,window):
        ## Drawing Board
        pygame.draw.line(window,self.borderColor,(self.rect[0]+self.rect[2]//3,self.rect[1]),(self.rect[0]+self.rect[2]//3,self.rect[1]+self.rect[3]),self.borderWidth)
        pygame.draw.line(window,self.borderColor,(self.rect[0]+2*self.rect[2]//3,self.rect[1]),(self.rect[0]+2*self.rect[2]//3,self.rect[1]+self.rect[3]),self.borderWidth)
        pygame.draw.line(window,self.borderColor,(self.rect[0],self.rect[1]+self.rect[3]//3),(self.rect[0]+self.rect[2],self.rect[1]+self.rect[3]//3),self.borderWidth)
        pygame.draw.line(window,self.borderColor,(self.rect[0],self.rect[1]+2*self.rect[3]//3),(self.rect[0]+self.rect[2],self.rect[1]+2*self.rect[3]//3),self.borderWidth)

        ## Generating Odd And Even Moves
        oddMoves=list(self.currentMoves[i] for i in range(len(self.currentMoves)) if i%2==1)
        evenMoves=list(self.currentMoves[i] for i in range(len(self.currentMoves)) if i%2==0)

        ## Drawing Even Moves
        for i in evenMoves:
            tempRect=self.rectList[i-1]
            pygame.draw.circle(window,self.circleColor,(tempRect.x+tempRect.width//2,tempRect.y+tempRect.height//2),tempRect.height//4,self.borderWidth)
        ## Drawing Odd Moves
        for i in oddMoves:
            tempRect=self.rectList[i-1]
            pygame.draw.line(window,self.crossColor,(tempRect.x+3*tempRect.width//8,tempRect.y+3*tempRect.height//8),(tempRect.x+5*tempRect.width//8,tempRect.y+5*tempRect.height//8),self.borderWidth)
            pygame.draw.line(window,self.crossColor,(tempRect.x+3*tempRect.width//8,tempRect.y+5*tempRect.height//8),(tempRect.x+5*tempRect.width//8,tempRect.y+3*tempRect.height//8),self.borderWidth)
        
        ## Drawing Winner Data
        pygame.draw.line(window,self.winLineColor,tuple(self.winLineCurrent[0]),tuple(self.winLineCurrent[1]),self.borderWidth)
        if not((abs(self.winLineStored[0][0]-self.winLineCurrent[0][0])>self.winLineSpeed) or (abs(self.winLineStored[0][1]-self.winLineCurrent[0][1])>self.winLineSpeed) or (abs(self.winLineStored[1][0]-self.winLineCurrent[1][0])>self.winLineSpeed) or (abs(self.winLineStored[1][1]-self.winLineCurrent[1][1])>self.winLineSpeed)) and self.winner!=None:
            self.gameEnded=True
            if self.winTextObject==None:
                self.winTextObject=OriginTechFont.originTechFont("",(self.rect[0]+self.rect[2]//2,self.rect[1]+self.rect[3]//2),window,25)
            if (self.winner=="odd" and self.isEven) or (self.winner=="even" and not(self.isEven)):
                self.winTextObject.changeText("Better Luck Next Time Well Played",window)
            elif (self.winner=="even" and self.isEven) or (self.winner=="odd" and not(self.isEven)):
                self.winTextObject.changeText("Congratulations Well Played",window)
            elif self.winner=="na":
                self.winTextObject.changeText("Its A Draw",window)
            self.winTextObject.update(window)

    def update(self):
        if self.winner==None:
            oddMoves=list(self.currentMoves[i] for i in range(len(self.currentMoves)) if i%2==1)
            evenMoves=list(self.currentMoves[i] for i in range(len(self.currentMoves)) if i%2==0)
            if (1 in oddMoves and 2 in oddMoves and 3 in oddMoves) or (4 in oddMoves and 5 in oddMoves and 6 in oddMoves) or (7 in oddMoves and 8 in oddMoves and 9 in oddMoves) or (1 in oddMoves and 4 in oddMoves and 7 in oddMoves) or (2 in oddMoves and 5 in oddMoves and 8 in oddMoves) or (3 in oddMoves and 6 in oddMoves and 9 in oddMoves) or (1 in oddMoves and 5 in oddMoves and 9 in oddMoves) or (3 in oddMoves and 5 in oddMoves and 7 in oddMoves):
                self.winner="odd"
                evenMoves=oddMoves
                self.userActive=False
            elif (1 in evenMoves and 2 in evenMoves and 3 in evenMoves) or (4 in evenMoves and 5 in evenMoves and 6 in evenMoves) or (7 in evenMoves and 8 in evenMoves and 9 in evenMoves) or (1 in evenMoves and 4 in evenMoves and 7 in evenMoves) or (2 in evenMoves and 5 in evenMoves and 8 in evenMoves) or (3 in evenMoves and 6 in evenMoves and 9 in evenMoves) or (1 in evenMoves and 5 in evenMoves and 9 in evenMoves) or (3 in evenMoves and 5 in evenMoves and 7 in evenMoves):
                self.winner="even"
                self.userActive=False
            elif len(list(i for i in range(1,10) if i not in self.currentMoves))==0:
                self.winner="na"
                self.userActive=False
            if (1 in evenMoves and 2 in evenMoves and 3 in evenMoves):
                self.winLineOrientation="H"
                self.winLineCurrent=[[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//6],[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//6]]
                self.winLineStored=[[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//6],[self.rect[0]+5*self.rect[2]//6,self.rect[1]+self.rect[3]//6]]
            elif (4 in evenMoves and 5 in evenMoves and 6 in evenMoves):
                self.winLineOrientation="H"
                self.winLineCurrent=[[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//2],[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//2]]
                self.winLineStored=[[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//2],[self.rect[0]+5*self.rect[2]//6,self.rect[1]+self.rect[3]//2]]
            elif (7 in evenMoves and 8 in evenMoves and 9 in evenMoves):
                self.winLineOrientation="H"
                self.winLineCurrent=[[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6],[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6]]
                self.winLineStored=[[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6],[self.rect[0]+5*self.rect[2]//6,self.rect[1]+5*self.rect[3]//6]]
            elif (1 in evenMoves and 4 in evenMoves and 7 in evenMoves):
                self.winLineOrientation="V"
                self.winLineCurrent=[[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//6],[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6]]
                self.winLineStored=[[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//6],[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6]]
            elif (2 in evenMoves and 5 in evenMoves and 8 in evenMoves):
                self.winLineOrientation="V"
                self.winLineCurrent=[[self.rect[0]+self.rect[2]//2,self.rect[1]+self.rect[3]//6],[self.rect[0]+self.rect[2]//2,self.rect[1]+self.rect[3]//6]]
                self.winLineStored=[[self.rect[0]+self.rect[2]//2,self.rect[1]+self.rect[3]//6],[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6]]
            elif (3 in evenMoves and 6 in evenMoves and 9 in evenMoves):
                self.winLineOrientation="V"
                self.winLineCurrent=[[self.rect[0]+5*self.rect[2]//6,self.rect[1]+self.rect[3]//6],[self.rect[0]+5*self.rect[2]//6,self.rect[1]+self.rect[3]//6]]
                self.winLineStored=[[self.rect[0]+5*self.rect[2]//6,self.rect[1]+self.rect[3]//6],[self.rect[0]+5*self.rect[2]//6,self.rect[1]+5*self.rect[3]//6]]
            elif (1 in evenMoves and 5 in evenMoves and 9 in evenMoves):
                self.winLineOrientation="S+"
                self.winLineCurrent=[[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//6],[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//6]]
                self.winLineStored=[[self.rect[0]+self.rect[2]//6,self.rect[1]+self.rect[3]//6],[self.rect[0]+5*self.rect[2]//6,self.rect[1]+5*self.rect[3]//6]]
            elif (7 in evenMoves and 5 in evenMoves and 3 in evenMoves):
                self.winLineOrientation="S-"
                self.winLineCurrent=[[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6],[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6]]
                self.winLineStored=[[self.rect[0]+self.rect[2]//6,self.rect[1]+5*self.rect[3]//6],[self.rect[0]+5*self.rect[2]//6,self.rect[1]+self.rect[3]//6]]
            
        if (abs(self.winLineStored[0][0]-self.winLineCurrent[0][0])>self.winLineSpeed) or (abs(self.winLineStored[0][1]-self.winLineCurrent[0][1])>self.winLineSpeed) or (abs(self.winLineStored[1][0]-self.winLineCurrent[1][0])>self.winLineSpeed) or (abs(self.winLineStored[1][1]-self.winLineCurrent[1][1])>self.winLineSpeed):
            if self.winLineOrientation=="H":
                self.winLineCurrent[1][0]+=self.winLineSpeed
            elif self.winLineOrientation=="V":
                self.winLineCurrent[1][1]+=self.winLineSpeed
            elif self.winLineOrientation=="S+":
                self.winLineCurrent[1][0]+=self.winLineSpeed
                self.winLineCurrent[1][1]+=self.winLineSpeed
            elif self.winLineOrientation=="S-":
                self.winLineCurrent[1][0]+=self.winLineSpeed
                self.winLineCurrent[1][1]-=self.winLineSpeed

    def mouseHandler(self):
        mousePosition=pygame.mouse.get_pos()
        availbleMoves=list(i for i in range(0,10) if i not in self.currentMoves)
        if not(self.userActive):
            return()
        for i in range(0,9):
            if self.rectList[i].collidepoint(mousePosition[0],mousePosition[1]) and i+1 in availbleMoves:
                self.currentMoves.append(i+1)
                if self.autoRotate:
                    self.userActive=False

    def eventHandler(self,events,window):
        for event in events:
            if event.type==pygame.MOUSEBUTTONUP:
                self.mouseHandler()

    def reset(self):
        self.currentMoves=[]
        self.userActive=self.isEven
        self.gameEnded=False
        self.winner=None
        self.winLineStored=[(0,0),(0,0)]
        self.winLineCurrent=[(0,0),(0,0)]
        self.winLineOrientation="H"
        self.winTextObject=None
        self.update()


if __name__=="__main__":
    pygame.init()
    window=pygame.display.set_mode((700,700))
    selector=board((200,200,300,300),borderWidth=5,winLineSpeed=10)
    clock=pygame.time.Clock()
    c=0
    while True:
        clock.tick(24)
        window.fill((240,0,0))
        selector.update()
        selector.draw(window)
        pygame.display.update()
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                quit() 
        selector.eventHandler(events,window)       