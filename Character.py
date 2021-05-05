## Importing External Dependencies
import pygame

## Importing Libraries
import OriginTechFont, GUI

class Characters():
    def __init__(self):
        ## Storing Attributes
        self.maxStateFrames=24
        self.image=None
        self.imageList=None
        self.state=0
        self.counterState=0
        self.rect=pygame.Rect(0,0,10,10)
        ## Border Details
        self.borderColor=(255,255,255)
        self.borderWidth=2
        self.borderRect=pygame.Rect(self.rect.x-self.borderWidth,self.rect.y-self.borderWidth,self.rect.width+2*self.borderWidth,self.rect.height+self.borderWidth)
        ## Speech Details
        self.maxSpeechFrames=24
        self.counterSpeech=0
        self.speechRect=(0,0)
        self.speechText=""
        self.speechTextSize=24
        self.speechTextColor=(240,240,240)
        self.speechTextObject=None
        ## User Active
        self.userActive=False

    def update(self):
        self.image=self.imageList[self.state]
        self.counterState+=1
        self.counterSpeech+=1
        if self.counterState%self.maxStateFrames==0:
            self.counterState=0
            self.state=0
        if self.counterSpeech%self.maxSpeechFrames==0:
            self.counterSpeech=0
            self.speechText=""
        if self.userActive:
            self.borderColor=(20,255,20)
        else:
            self.borderColor=(255,255,255)
        
    def draw(self,window):
        ## Border Rectangle
        pygame.draw.rect(window,self.borderColor,rect=self.borderRect,width=self.borderWidth)
        window.blit(self.image,(self.rect.x,self.rect.y))
        if self.speechTextObject==None:
            self.speechTextObject=OriginTechFont.originTechFont(self.speechText,self.speechRect,window,textSize=self.speechTextSize,textColor=self.speechTextColor,leftAlign=True)
        self.speechTextObject.changeText(self.speechText,window)
        self.speechTextObject.update(window)


class Veera(Characters):
    def __init__(self,rect,maxStateFrames=24,borderColor=(255,255,255),borderWidth=2,textSize=24,textColor=(240,240,240),maxSpeechFrames=24):
        super(Veera,self).__init__()

        ## Storing Images
        self.maxFrames=maxStateFrames
        self.imageList=[pygame.image.load("Assets\Characters\Veera\Veera_02_Side_Armor_Helmet_Neutral.png"),
                        pygame.image.load("Assets\Characters\Veera\Veera_02_Side_Armor_Helmet_Angry.png"),
                        pygame.image.load("Assets\Characters\Veera\Veera_02_Side_Armor_Helmet_Happy.png"),
                        pygame.image.load("Assets\Characters\Veera\Veera_02_Side_Armor_Helmet_Sad.png"),
                        pygame.image.load("Assets\Characters\Veera\Veera_02_Side_Armor_Helmet_Scared.png"),
                        pygame.image.load("Assets\Characters\Veera\Veera_02_Side_Armor_Helmet_Suprised.png")]
        self.imageList=list(pygame.transform.scale(i,(rect[2],rect[3])) for i in self.imageList)
        self.image=self.imageList[2]
        ## Storing Border Details
        self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
        self.borderRect=pygame.Rect(self.rect.x-self.borderWidth,self.rect.y-self.borderWidth,self.rect.width+2*self.borderWidth,self.rect.height+2*self.borderWidth)
        ## Storing Text Details
        self.maxSpeechFrames=maxSpeechFrames
        self.speechTextSize=textSize
        self.speechTextColor=textColor
        self.speechRect=(int(self.rect.x+3*self.rect.width//5),int(self.rect.y+2*self.rect.height//3))

class Lochem(Characters):
    def __init__(self,rect,maxStateFrames=24,borderColor=(255,255,255),borderWidth=2,textSize=24,textColor=(240,240,240),maxSpeechFrames=24):
        super(Lochem,self).__init__()

        ## Storing Images
        self.maxFrames=maxStateFrames
        self.imageList=[pygame.image.load("Assets\Characters\Lochem\Lochem_01_Side_Uniform_Neutral.png"),
                        pygame.image.load("Assets\Characters\Lochem\Lochem_01_Side_Uniform_Angry.png"),
                        pygame.image.load("Assets\Characters\Lochem\Lochem_01_Side_Uniform_Happy.png"),
                        pygame.image.load("Assets\Characters\Lochem\Lochem_01_Side_Uniform_Sad.png"),
                        pygame.image.load("Assets\Characters\Lochem\Lochem_01_Side_Uniform_Scared.png"),
                        pygame.image.load("Assets\Characters\Lochem\Lochem_01_Side_Uniform_Suprised.png")]
        self.imageList=list(pygame.transform.scale(i,(rect[2],rect[3])) for i in self.imageList)
        self.image=self.imageList[2]
        ## Storing Border Details
        self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
        self.borderRect=pygame.Rect(self.rect.x-self.borderWidth,self.rect.y-self.borderWidth,self.rect.width+2*self.borderWidth,self.rect.height+2*self.borderWidth)
        ## Storing Text Details
        self.maxSpeechFrames=maxSpeechFrames
        self.speechTextSize=textSize
        self.speechTextColor=textColor
        self.speechRect=(int(self.rect.x+self.rect.width//2),int(self.rect.y+2*self.rect.height//3))

class Mayvheen(Characters):
    def __init__(self,rect,maxStateFrames=24,borderColor=(255,255,255),borderWidth=2,textSize=24,textColor=(240,240,240),maxSpeechFrames=24):
        super(Mayvheen,self).__init__()

        ## Storing Images
        self.maxFrames=maxStateFrames
        self.imageList=[pygame.image.load("Assets\Characters\Mayvheen\Mayvheen_01_Side_Uniform_Neutral.png"),
                        pygame.image.load("Assets\Characters\Mayvheen\Mayvheen_01_Side_Uniform_Angry.png"),
                        pygame.image.load("Assets\Characters\Mayvheen\Mayvheen_01_Side_Uniform_Happy.png"),
                        pygame.image.load("Assets\Characters\Mayvheen\Mayvheen_01_Side_Uniform_Sad.png"),
                        pygame.image.load("Assets\Characters\Mayvheen\Mayvheen_01_Side_Uniform_Scared.png"),
                        pygame.image.load("Assets\Characters\Mayvheen\Mayvheen_01_Side_Uniform_Suprised.png")]
        self.imageList=list(pygame.transform.scale(i,(rect[2],rect[3])) for i in self.imageList)
        self.image=self.imageList[2]
        ## Storing Border Details
        self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
        self.borderRect=pygame.Rect(self.rect.x-self.borderWidth,self.rect.y-self.borderWidth,self.rect.width+2*self.borderWidth,self.rect.height+2*self.borderWidth)
        ## Storing Text Details
        self.maxSpeechFrames=maxSpeechFrames
        self.speechTextSize=textSize
        self.speechTextColor=textColor
        self.speechRect=(int(self.rect.x+13*self.rect.width//20),int(self.rect.y+2*self.rect.height//3))  

class Kiaria(Characters):
    def __init__(self,rect,maxStateFrames=24,borderColor=(255,255,255),borderWidth=2,textSize=24,textColor=(240,240,240),maxSpeechFrames=24):
        super(Kiaria,self).__init__()

        ## Storing Images
        self.maxFrames=maxStateFrames
        self.imageList=[pygame.image.load("Assets\Characters\Kiaria\Kiaria_01_Side_Uniform_Glasses_Neutral.png"),
                        pygame.image.load("Assets\Characters\Kiaria\Kiaria_01_Side_Uniform_Glasses_Angry.png"),
                        pygame.image.load("Assets\Characters\Kiaria\Kiaria_01_Side_Uniform_Glasses_Happy.png"),
                        pygame.image.load("Assets\Characters\Kiaria\Kiaria_01_Side_Uniform_Glasses_Sad.png"),
                        pygame.image.load("Assets\Characters\Kiaria\Kiaria_01_Side_Uniform_Glasses_Scared.png"),
                        pygame.image.load("Assets\Characters\Kiaria\Kiaria_01_Side_Uniform_Glasses_Suprised.png")]
        self.imageList=list(pygame.transform.scale(i,(rect[2],rect[3])) for i in self.imageList)
        self.image=self.imageList[2]
        ## Storing Border Details
        self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
        self.borderRect=pygame.Rect(self.rect.x-self.borderWidth,self.rect.y-self.borderWidth,self.rect.width+2*self.borderWidth,self.rect.height+2*self.borderWidth)
        ## Storing Text Details
        self.maxSpeechFrames=maxSpeechFrames
        self.speechTextSize=textSize
        self.speechTextColor=textColor
        self.speechRect=(int(self.rect.x+13*self.rect.width//20),int(self.rect.y+2*self.rect.height//3))  

class Raymond(Characters):
    def __init__(self,rect,maxStateFrames=24,borderColor=(255,255,255),borderWidth=2,textSize=24,textColor=(240,240,240),maxSpeechFrames=24):
        super(Raymond,self).__init__()

        ## Storing Images
        self.maxFrames=maxStateFrames
        self.imageList=[pygame.image.load("Assets\Characters\Raymond\Raymond_01_Side_Uniform_Neutral.png"),
                        pygame.image.load("Assets\Characters\Raymond\Raymond_01_Side_Uniform_Angry.png"),
                        pygame.image.load("Assets\Characters\Raymond\Raymond_01_Side_Uniform_Happy.png"),
                        pygame.image.load("Assets\Characters\Raymond\Raymond_01_Side_Uniform_Sad.png"),
                        pygame.image.load("Assets\Characters\Raymond\Raymond_01_Side_Uniform_Scared.png"),
                        pygame.image.load("Assets\Characters\Raymond\Raymond_01_Side_Uniform_Suprised.png")]
        self.imageList=list(pygame.transform.scale(i,(rect[2],rect[3])) for i in self.imageList)
        self.image=self.imageList[2]
        ## Storing Border Details
        self.rect=pygame.Rect(rect[0],rect[1],rect[2],rect[3])
        self.borderRect=pygame.Rect(self.rect.x-self.borderWidth,self.rect.y-self.borderWidth,self.rect.width+2*self.borderWidth,self.rect.height+2*self.borderWidth)
        ## Storing Text Details
        self.maxSpeechFrames=maxSpeechFrames
        self.speechTextSize=textSize
        self.speechTextColor=textColor
        self.speechRect=(int(self.rect.x+11*self.rect.width//20),int(self.rect.y+19*self.rect.height//30))

if __name__=="__main__":
    pygame.init()
    window=pygame.display.set_mode((700,700))
    charVeera=Raymond((200,200,300,300))
    spriteGroup=GUI.guiGroup([charVeera])
    charVeera.speechText="hhhhhhhfggghghghhjjjh"
    clock=pygame.time.Clock()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill((0,0,0))
        spriteGroup.update()
        spriteGroup.draw(window)
        pygame.display.update()

