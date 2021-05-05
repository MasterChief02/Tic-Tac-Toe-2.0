## Importing External Dependencies
import pygame, _thread

## Importing Libraries
import OriginTechFont, GUI, Resources, Game, firebase

####################
## Loading Screen ##
####################
def loadingScreen(window):
    ## Game Name and Description
    gameName=OriginTechFont.originTechFont("TIC-TAC-TOE",(350,150),window,textSize=100,textColor=Resources.colorHeading1)
    gameDesc=OriginTechFont.originTechFont("An Online Multiplayer Game",(350,225),window,textSize=25,textColor=Resources.colorHeading2)
    ## Loader Bar and Text
    loaderBar=GUI.loadingBar((46,430,608,20),window,sections=20,margin=4)
    loaderText=OriginTechFont.originTechFont("Initilaizing",(350,475),window,textColor=Resources.colorHeading3)
    ## Credits Text
    creditText=OriginTechFont.originTechFont("Developed and maintained by Yogesh Kaushik",(350,660),window,textSize=15,textColor=Resources.colorHeading4)
    clock=pygame.time.Clock()
    c=0
    while loaderBar.counter<=20:
        clock.tick(24)
        c+=4
        window.fill((0,0,0))
        ## Updating Game Name and Description
        gameName.update(window)
        gameDesc.update(window)
        ## Updating Loader Bar and Text
        loaderBar.update()
        loaderText.update(window)
        ## Updating Credits Text
        creditText.update(window)
        ## Updating Display
        pygame.display.update()
        if c%24==0:
            loaderBar.counter+=1
        if c%96==0:
            loaderText.changeText(f"Stage {c//96}", window)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


##################
## Login Screen ##
##################
def loginScreen(window,currentState=False):    ## currentState=True->Login
    ## Login Flag
    loginFlag=True
    ## Background Image
    bgImage=pygame.image.load("Assets\GUI\PNG\Main_Menu\BG.png")
    bgImage=pygame.transform.scale(bgImage,(700,700))
    ## Game Name
    gameName=OriginTechFont.originTechFont("TIC-TAC-TOE",(350,100),window,textSize=100,textColor=Resources.colorHeading1)
    if currentState:
        ## Login Page Elements
        loginBGImage=pygame.image.load("D:\Project\Python\Tic-Tac-Toe 2.0\Assets\GUI\PNG\Hangar\Window.png")
        loginBGImage=pygame.transform.scale(loginBGImage,(300,400))
        loginText=OriginTechFont.originTechFont("Login",(350,220),window,textSize=30,textColor=Resources.colorHeading5)
        ## Login Section Elements
        usernameText=OriginTechFont.originTechFont("Username",(270,280),window,textSize=20,textColor=Resources.colorHeading5)
        usernameInput=GUI.inputBox((220,310,260,40),"OriginTech",window,textSize=18,maxWords=20,boxColor=Resources.colorInputBox,borderColor=Resources.colorInputBoxBorder)
        passwordText=OriginTechFont.originTechFont("Password",(270,380),window,textSize=20,textColor=Resources.colorHeading5)
        passwordInput=GUI.inputBox((220,410,260,40),"OriginTech",window,textSize=18,maxWords=20,boxColor=Resources.colorInputBox,borderColor=Resources.colorInputBoxBorder,isPassword=True)
        ## Login Button
        loginButtonBGImage=pygame.image.load("Assets\GUI\PNG\Hangar\Table_02.png")
        loginButtonBGImage=pygame.transform.scale(loginButtonBGImage,(100,40))
        loginButtonText=OriginTechFont.originTechFont("Login",(250,522),window,textSize=20,textColor=Resources.colorHeading5)
        loginButtonRect=pygame.Rect(225,500,100,50)
        ## Opposite Button
        oppositeButtonObject=GUI.button((375,507,100,30),"Sign Up",textSize=16)
        oppositeButtonRect=pygame.Rect(375,507,100,30)
    else:
        ## Signup Page Elements
        loginBGImage=pygame.image.load("D:\Project\Python\Tic-Tac-Toe 2.0\Assets\GUI\PNG\Hangar\Window.png")
        loginBGImage=pygame.transform.scale(loginBGImage,(300,500))
        loginText=OriginTechFont.originTechFont("Sign Up",(350,175),window,textSize=30,textColor=Resources.colorHeading5)
        ## Sign Up Section Elements
        usernameText=OriginTechFont.originTechFont("Username",(270,230),window,textSize=20,textColor=Resources.colorHeading5)
        usernameInput=GUI.inputBox((220,250,260,40),"OriginTech",window,textSize=18,maxWords=20,boxColor=Resources.colorInputBox,borderColor=Resources.colorInputBoxBorder)
        passwordText=OriginTechFont.originTechFont("Password",(270,310),window,textSize=20,textColor=Resources.colorHeading5)
        passwordInput=GUI.inputBox((220,330,260,40),"OriginTech",window,textSize=18,maxWords=20,boxColor=Resources.colorInputBox,borderColor=Resources.colorInputBoxBorder,isPassword=True)
        ## Sign Up Character Selector
        selector=GUI.characterSelector((250,390,200,190), textSize=16)
        ## Sign Up Button
        loginButtonBGImage=pygame.image.load("Assets\GUI\PNG\Hangar\Table_02.png")
        loginButtonBGImage=pygame.transform.scale(loginButtonBGImage,(100,40))
        loginButtonText=OriginTechFont.originTechFont("Sign Up",(275,607),window,textSize=20,textColor=Resources.colorHeading5)
        loginButtonRect=pygame.Rect(225,585,150,40)
        ## Opposite Button
        oppositeButtonObject=GUI.button((375,592,100,30),"Login",textSize=16,margin=0)
        oppositeButtonRect=pygame.Rect(375,592,100,30)
    ## Initializing Clock
    clock=pygame.time.Clock()
    ## State Change Controller
    stateChanged=False
    while True:
        ## CHANGING STATE
        if stateChanged:
            stateChanged=False
            if currentState:
                ## Login Page Elements
                loginBGImage=pygame.image.load("Assets\GUI\PNG\Hangar\Window.png")
                loginBGImage=pygame.transform.scale(loginBGImage,(300,400))
                loginText=OriginTechFont.originTechFont("Login",(350,220),window,textSize=30,textColor=Resources.colorHeading5)
                ## Login Section Elements
                usernameText=OriginTechFont.originTechFont("Username",(270,280),window,textSize=20,textColor=Resources.colorHeading5)
                usernameInput=GUI.inputBox((220,310,260,40),"OriginTech",window,textSize=18,maxWords=20,boxColor=Resources.colorInputBox,borderColor=Resources.colorInputBoxBorder)
                passwordText=OriginTechFont.originTechFont("Password",(270,380),window,textSize=20,textColor=Resources.colorHeading5)
                passwordInput=GUI.inputBox((220,410,260,40),"OriginTech",window,textSize=18,maxWords=20,boxColor=Resources.colorInputBox,borderColor=Resources.colorInputBoxBorder,isPassword=True)
                ## Login Button
                loginButtonBGImage=pygame.image.load("Assets\GUI\PNG\Hangar\Table_02.png")
                loginButtonBGImage=pygame.transform.scale(loginButtonBGImage,(100,40))
                loginButtonText=OriginTechFont.originTechFont("Login",(275,522),window,textSize=20,textColor=Resources.colorHeading5)
                loginButtonRect=pygame.Rect(225,500,100,50)
                ## Opposite Button
                oppositeButtonObject=GUI.button((375,507,100,30),"Sign Up",textSize=16)
                oppositeButtonRect=pygame.Rect(375,507,100,30)
            else:
                ## Signup Page Elements
                loginBGImage=pygame.image.load("Assets\GUI\PNG\Hangar\Window.png")
                loginBGImage=pygame.transform.scale(loginBGImage,(300,500))
                loginText=OriginTechFont.originTechFont("Sign Up",(350,175),window,textSize=30,textColor=Resources.colorHeading5)
                ## Sign Up Section Elements
                usernameText=OriginTechFont.originTechFont("Username",(270,230),window,textSize=20,textColor=Resources.colorHeading5)
                usernameInput=GUI.inputBox((220,250,260,40),"OriginTech",window,textSize=18,maxWords=20,boxColor=Resources.colorInputBox,borderColor=Resources.colorInputBoxBorder)
                passwordText=OriginTechFont.originTechFont("Password",(270,310),window,textSize=20,textColor=Resources.colorHeading5)
                passwordInput=GUI.inputBox((220,330,260,40),"OriginTech",window,textSize=18,maxWords=20,boxColor=Resources.colorInputBox,borderColor=Resources.colorInputBoxBorder,isPassword=True)
                ## Sign Up Character Selector
                selector=GUI.characterSelector((250,390,200,190), textSize=16)
                ## Sign Up Button
                loginButtonBGImage=pygame.image.load("Assets\GUI\PNG\Hangar\Table_02.png")
                loginButtonBGImage=pygame.transform.scale(loginButtonBGImage,(100,40))
                loginButtonText=OriginTechFont.originTechFont("Sign Up",(275,607),window,textSize=20,textColor=Resources.colorHeading5)
                loginButtonRect=pygame.Rect(225,585,150,40)
                ## Opposite Button
                oppositeButtonObject=GUI.button((375,592,100,30),"Login",textSize=16,margin=0)
                oppositeButtonRect=pygame.Rect(375,592,100,30)
        ##
        clock.tick(24)
        window.fill((0,0,0))
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONUP:
                mousePosition=pygame.mouse.get_pos()
                if loginButtonRect.collidepoint(mousePosition[0],mousePosition[1]):
                    ## For SignUp
                    if currentState==False:
                        return(firebase.authentication(usernameInput.text.upper(),passwordInput.text.upper(),selector.currentObject))
                    ## For Login
                    else:
                        return(firebase.authentication(usernameInput.text.upper(),passwordInput.text.upper(),isSignUp=False))
                elif oppositeButtonRect.collidepoint(mousePosition[0],mousePosition[1]):
                    currentState=not(currentState)
                    stateChanged=True
        ## Adding Images
        window.blit(bgImage,(0,0))
        ## Updating Login Elements
        if currentState:
            window.blit(loginBGImage,(200,200))
            window.blit(loginButtonBGImage,(225,503))
        ## Updating Sign Up Elements
        else:
            window.blit(loginBGImage,(200,150))
            window.blit(loginButtonBGImage,(225,588))
            selector.draw(window)
            selector.eventHandler(events,window)
        ## Login Button Text
        loginButtonText.update(window)
        ## Updating Opposite Button
        oppositeButtonObject.draw(window)
        ## Updating Game Name and Environment
        gameName.update(window)
        loginText.update(window)
        usernameInput.update(window)
        passwordText.update(window)
        passwordInput.update(window)
        ## Updating Login Section
        usernameText.update(window)
        pygame.display.update()
        ## Event Handling For Input Boxes
        usernameInput.eventHandler(events,window)
        passwordInput.eventHandler(events,window)



#################
## Main Screen ##
#################
def mainScreen(window):
    ## Loading Text
    gameName1=OriginTechFont.originTechFont("Tic-Tac-Toe",(350,200),window,100,textColor=Resources.colorHeading2)
    gameName2=OriginTechFont.originTechFont("2.0",(350,325),window,100,textColor=Resources.colorHeading2)
    ## Loading Buttons
    buttons=GUI.guiGroup([GUI.button((225,450,250,50),"Play Online",bgImage="Assets\GUI\PNG\Level_Menu\Table.png", borderWidth=-2), GUI.button((225,525,250,50),"Play Locally",bgImage="Assets\GUI\PNG\Level_Menu\Table.png", borderWidth=-2), GUI.button((225,600,250,50),"Play Against AI",bgImage="Assets\GUI\PNG\Level_Menu\Table.png", borderWidth=-2), GUI.button((550,25,50,50),bgImage="Assets\GUI\PNG\Main_Menu\Settings_BTN.png",borderWidth=-2), GUI.button((625,25,50,50),bgImage="Assets\GUI\PNG\Main_Menu\Info_BTN.png",borderWidth=-2)])
    ## Initializing Timer
    clock=pygame.time.Clock()
    while True:
        clock.tick(24)
        ## Updating Window
        window.fill((0,0,0))
        gameName1.update(window)
        gameName2.update(window)
        buttons.update()
        buttons.draw(window)
        pygame.display.update()
        ## Checking For Events
        for event in pygame.event.get():
            ## Checking For Quit
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            ## Checking For Mouse Clicks
            elif event.type==pygame.MOUSEBUTTONDOWN:
                xPos,yPos=pygame.mouse.get_pos()
                ## Checking For Play Local Button
                if 225<=xPos<=475 and 450<=yPos<=500:
                    return(0)
                elif 225<=xPos<=475 and 525<=yPos<=575:
                    return(1)
                elif 225<=xPos<=475 and 600<=yPos<=650:
                    return(2)


#######################
## Against AI Loader ##
#######################
def againstAILoader(window):
    loader=GUI.loadingBar((100,300,500,50),window,30)
    loaderText=OriginTechFont.originTechFont("Building Game",(350,375),window)
    counter=0
    clock=pygame.time.Clock()
    while not(Resources.againstAIReady):
        clock.tick(24)
        counter+=1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                xPos,yPos=pygame.mouse.get_pos()
        if counter%25==0:
            loader.counter+=1
        window.fill((0,0,0))
        loader.update()
        loaderText.update(window)
        pygame.display.update()


if __name__=="__main__":
    pygame.init()
    window=pygame.display.set_mode((700,700))
    loadingScreen(window)
    window.fill((0,0,0))
    loginData=False
    ## Getting Login Data
    while loginData==False:
        loginData=loginScreen(window)
        if loginData==False:
            failureText=OriginTechFont.originTechFont("Login/Sign Up Failed. Please Try Again",(350,350),window,textColor=(240,50,50))
            frameCounter=0
            clock=pygame.time.Clock()
            while frameCounter<=72:
                clock.tick(24)
                frameCounter+=1
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                window.fill((0,0,0))
                failureText.update(window)
                pygame.display.update()
    if loginData!=False:
        while True:
            cmd=mainScreen(window)
            if cmd==0:
                Game.online(window,loginData[1],loginData[0])
            elif cmd==1:
                Game.localhost(window,loginData[1],loginData[0])
            elif cmd==2:
                clock=pygame.time.Clock()
                data=[0,0]
                controlVariable=True
                firstList=GUI.guiGroup([GUI.button((100,275,200,50),"AI First",bgImage="Assets\GUI\PNG\Level_Menu\Table.png"),GUI.button((400,275,200,50),"User First",bgImage="Assets\GUI\PNG\Level_Menu\Table.png",borderWidth=-2)])
                difficulty=GUI.guiGroup([GUI.button((75,375,150,50),"Easy",bgImage="Assets\GUI\PNG\Level_Menu\Table.png"),GUI.button((275,375,150,50),"Medium",bgImage="Assets\GUI\PNG\Level_Menu\Table.png",borderWidth=-2),GUI.button((475,375,150,50),"Hard",bgImage="Assets\GUI\PNG\Level_Menu\Table.png",borderWidth=-2)])
                playButton=GUI.button((300,475,100,50),"Start",bgImage="Assets\GUI\PNG\Level_Menu\Table.png",borderWidth=-2)
                while controlVariable:
                    clock.tick(24)
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type==pygame.MOUSEBUTTONDOWN:
                            xPos,yPos=pygame.mouse.get_pos()
                            for i in range(2):
                                if firstList.guiObjects[i].rect.collidepoint(xPos,yPos):
                                    data[0]=i
                                elif difficulty.guiObjects[i].rect.collidepoint(xPos,yPos):
                                    data[1]=i
                            if difficulty.guiObjects[2].rect.collidepoint(xPos,yPos):
                                data[1]=2
                            if playButton.rect.collidepoint(xPos,yPos):
                                controlVariable=False
                    for i in range(2):
                        if i==data[0]:
                            firstList.guiObjects[i].borderWidth=2
                        else:
                            firstList.guiObjects[i].borderWidth=-2
                    for i in range(3):
                        if i==data[1]:
                            difficulty.guiObjects[i].borderWidth=2
                        else:
                            difficulty.guiObjects[i].borderWidth=-2
                    window.fill((0,0,0))
                    firstList.update()
                    firstList.draw(window)
                    difficulty.update()
                    difficulty.draw(window)
                    playButton.draw(window)
                    pygame.display.update()

                _thread.start_new_thread(againstAILoader,(window,))
                print(data)
                Game.againstAI(window,loginData[1],int(2-data[1]),bool(data[0]))