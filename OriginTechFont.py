import pygame


class originTechFont():
    def __init__(self, text, rect, window, textSize=24, textColor=(240,240,240), textBGColor=None,leftAlign=False):
        ## Storing Details
        self.textColor=textColor
        self.textBGColor=textBGColor
        self.rect=rect
        self.leftAlign=leftAlign

        ## Working
        self.font=pygame.font.Font("Assets\Font\Origin Tech\OriginTech personal use.ttf", textSize)
        if textBGColor!=None:
            self.fontSurfaceObject=self.font.render(text,True,self.textColor,self.textBGColor)
        else:
            self.fontSurfaceObject=self.font.render(text,True,self.textColor)
        self.fontSurfaceRectangleObject=self.fontSurfaceObject.get_rect()
        self.fontSurfaceRectangleObject.center=self.rect
        window.blit(self.fontSurfaceObject,self.fontSurfaceRectangleObject)
    
    ## Function For Updating View In The Window
    def update(self,window):
        window.blit(self.fontSurfaceObject,self.fontSurfaceRectangleObject)

    ## Function For Changing Text
    def changeText(self,text,window):
        if self.textBGColor!=None:
            self.fontSurfaceObject=self.font.render(text,True,self.textColor,self.textBGColor)
        else:
            self.fontSurfaceObject=self.font.render(text,True,self.textColor)
        if not(self.leftAlign):
            self.fontSurfaceRectangleObject=self.fontSurfaceObject.get_rect()
            self.fontSurfaceRectangleObject.center=self.rect
        self.update(window)