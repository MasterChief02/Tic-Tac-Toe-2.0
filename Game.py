import pygame, time, random, _thread
import OriginTechFont, AI, GUI, Character, networking, Resources, firebase


def againstAI(window,characterID=0,level=0,isEven=True):
    print(level,isEven)
    bot=AI.AI(not(isEven),level)
    Resources.againstAIReady=True
    game=GUI.board((200,200,300,300),borderWidth=5,userActive=isEven,autoRotate=True)
    botChar=Character.Raymond((50,50,100,100),maxSpeechFrames=48)
    botSpeech=["","Grrrrrrrrrrrrr","HaHaHaHa","Hhhhmmmmm","Ahhhh","Noiceee"]
    botState={0:1,1:4,2:3,3:5,4:2,5:0}
    storedMoves=game.currentMoves.copy()
    if characterID==0:
        userChar=Character.Kiaria((50,550,100,100))
    elif characterID==1:
        userChar=Character.Lochem((50,550,100,100))
    elif characterID==2:
        userChar=Character.Mayvheen((50,550,100,100))
    elif characterID==3:
        userChar=Character.Raymond((50,550,100,100))
    elif characterID==4:
        userChar=Character.Veera((50,550,100,100))
    buttons=GUI.guiGroup([GUI.button((525,25,50,50),"",bgImage="Assets\GUI\PNG\Buttons\BTNs\Replay_BTN.png",borderWidth=-2),GUI.button((625,25,50,50),"",bgImage="Assets\GUI\PNG\Buttons\BTNs\Close_BTN.png",borderWidth=-2)])
    clock=pygame.time.Clock()
    frames=0
    maxFrames=random.randint(24,48)
    controlVariable=True
    while controlVariable:
        userChar.userActive=game.userActive
        #botChar.userActive=not(game.userActive)
        clock.tick(24)
        events=pygame.event.get()
        window.fill((0,0,0))
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                keys=pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    bot.currentMoves=[]
                    game.reset()
            if event.type==pygame.MOUSEBUTTONDOWN:
                xPos,yPos=pygame.mouse.get_pos()
                if buttons.guiObjects[0].rect.collidepoint(xPos,yPos):
                    bot.currentMoves=[]
                    game.reset()
                elif buttons.guiObjects[1].rect.collidepoint(xPos,yPos):
                    controlVariable=False
                    Resources.againstAIReady=False
        if len(game.currentMoves)>len(bot.currentMoves):
            bot.currentMoves=game.currentMoves.copy()
            bot.stateUpdate()
            botChar.speechText=botSpeech[botState[5-int(bot.state)]]
            botChar.state=int(bot.state)
        elif len(game.currentMoves)<len(bot.currentMoves):
            game.currentMoves=bot.currentMoves.copy()
        game.eventHandler(events,window)
        game.update()
        game.draw(window)
        botChar.update()
        botChar.draw(window)
        userChar.update()
        userChar.draw(window)
        buttons.update()
        buttons.draw(window)
        pygame.display.update()
        if not(game.userActive):
            frames+=1
            if maxFrames==frames:
                game.userActive=True
                maxFrames=random.randint(24,48)
                frames=0
                if game.winner==None:
                    game.currentMoves.append(bot.nextMove())
                    botChar.speechText=botSpeech[botState[5-int(bot.state)]]
                    botChar.state=int(bot.state)
        if game.gameEnded:
            game.userActive=False

def localhost(window,characterID,characterName):
    ## Selecting Host Or Client Mode ##
    isHost=None
    ## Loading Buttons
    buttons=GUI.guiGroup([GUI.button((175,325,150,50),"Host",bgImage="Assets\GUI\PNG\Level_Menu\Table.png",borderWidth=-2),GUI.button((375,325,150,50),"Join",bgImage="Assets\GUI\PNG\Level_Menu\Table.png",borderWidth=-2)])
    backButton=GUI.button((50,50,50,50),"",bgImage="Assets\GUI\PNG\Buttons\BTNs_Active\Backward_BTN.png",borderWidth=-2)
    ## Initializing Clock
    clock=pygame.time.Clock()
    while isHost==None:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                xPos,yPos=pygame.mouse.get_pos()
                ## Checking For Host Mode Selection
                if 175<=xPos<=325 and 325<=yPos<=375:
                    isHost=True
                    break
                ## Checking For Client Mode Selection
                elif 375<=xPos<=525 and 325<=yPos<=375:
                    isHost=False
                    break
                ## Checking For Back Button
                if backButton.rect.collidepoint(xPos,yPos):
                    return()
        ## Updating Display
        window.fill((0,0,0))
        buttons.update()
        buttons.draw(window)
        backButton.draw(window)
        pygame.display.update()
    ## Getting Host Or Client Specific Needs ##
    if isHost:
        ## Starting Network
        network=networking.localhostHost(characterID,characterName)
        lastStatus=network.status
        _thread.start_new_thread(network.connection,())
    else:
        ipText=OriginTechFont.originTechFont("Please Enter The Number Shown To Host",(300,350),window,textSize=16)
        ipTextbox=GUI.inputBox((525,325,50,50),"OriginTech",window)
        ipButton=GUI.button((600,325,50,50),bgImage="Assets\GUI\PNG\Level_Menu\Play_BTN.png",borderWidth=-2,textSize=16)
        ipActive=True
        print(ipActive)
        while ipActive:
            clock.tick(24)
            events=pygame.event.get()
            for event in events:
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    xPos,yPos=pygame.mouse.get_pos()
                    if 600<=xPos<=650 and 325<=yPos<=375:
                        ipActive=False
                    elif backButton.rect.collidepoint(xPos,yPos):
                        network.endGame()
                        return()
            ## Update Screen
            window.fill((0,0,0))
            ipText.update(window)
            ipTextbox.update(window)
            ipTextbox.eventHandler(events,window)
            ipButton.update()
            ipButton.draw(window)
            backButton.draw(window)
            pygame.display.update()
        network=networking.localhostClient(str(".".join(Resources.localhostServer.split(".")[:-1])+"."+ipTextbox.text),characterID,characterName)
        lastStatus=network.status
        _thread.start_new_thread(network.connection,())
    ## GUI Data
    loader=GUI.loadingBar((100,300,490,50),window,6)
    loaderText=OriginTechFont.originTechFont(lastStatus,(350,375),window)
    ## Loading Window
    breakCounter=0
    maxBreakCounter=48
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        window.fill((0,0,0))
        ## Updating Loader
        if network.status!=lastStatus:
            loaderText.changeText(network.status,window)
            loader.counter+=1
            lastStatus=network.status
        loaderText.update(window)
        loader.update()
        ## Updating Screen
        pygame.display.update()
        ## Override Condition
        if network.connected!=None:
            breakCounter+=1
            if breakCounter>=maxBreakCounter:
                break
            if network.status=="GTG":
                break
    ## Setting Up Game ##
    ## Creating Opponent Character
    if network.opponentCharacterID==0:
        opponentChar=Character.Kiaria((50,50,100,100))
    elif network.opponentCharacterID==1:
        opponentChar=Character.Lochem((50,50,100,100))
    elif network.opponentCharacterID==2:
        opponentChar=Character.Mayvheen((50,50,100,100))
    elif network.opponentCharacterID==3:
        opponentChar=Character.Raymond((50,50,100,100))
    elif network.opponentCharacterID==4:
        opponentChar=Character.Veera((50,50,100,100))
    ## Creating User Character
    if characterID==0:
        userChar=Character.Kiaria((50,550,100,100))
    elif characterID==1:
        userChar=Character.Lochem((50,550,100,100))
    elif characterID==2:
        userChar=Character.Mayvheen((50,550,100,100))
    elif characterID==3:
        userChar=Character.Raymond((50,550,100,100))
    elif characterID==4:
        userChar=Character.Veera((50,550,100,100))
    ## Creating Board
    gameBoard=GUI.board((200,200,300,300),userActive=isHost)
    ## Creating New Buttons
    buttons=GUI.guiGroup([GUI.button((525,25,50,50),"",bgImage="Assets\GUI\PNG\Buttons\BTNs\Replay_BTN.png",borderWidth=-2),GUI.button((625,25,50,50),"",bgImage="Assets\GUI\PNG\Buttons\BTNs\Close_BTN.png",borderWidth=-2)])
    ## Game Loop
    controlVariable=True
    while controlVariable:
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                xPos,yPos=pygame.mouse.get_pos()
                if buttons.guiObjects[1].rect.collidepoint(xPos,yPos):
                    controlVariable=False
        ## Updating Netowrk And Board
        if gameBoard.userActive:
            if gameBoard.currentMoves!=network.game:
                network.game=gameBoard.currentMoves.copy()
                network.state=0
                gameBoard.userActive=False
        else:
            if network.game!=gameBoard.currentMoves:
                gameBoard.currentMoves=network.game.copy()
                gameBoard.userActive=True
        ## Updating Window
        userChar.userActive=gameBoard.userActive
        opponentChar.userActive=not(gameBoard.userActive)
        window.fill((0,0,0))
        userChar.update()
        userChar.draw(window)
        opponentChar.update()
        opponentChar.draw(window)
        gameBoard.update()
        gameBoard.draw(window)
        buttons.guiObjects[1].draw(window)
        pygame.display.update()
        gameBoard.eventHandler(events,window)

def online(window,characterID,characterName):
    ## Initializing Network
    network=firebase.Network(characterName,characterID)
    lastStatus=network.status
    ## Creating GUI For Loading Screen
    loader=GUI.loadingBar((100,300,500,50),window,6)
    loaderText=OriginTechFont.originTechFont(network.status,(350,375),window)
    backButton=GUI.button((50,50,50,50),"",bgImage="Assets\GUI\PNG\Buttons\BTNs_Active\Backward_BTN.png",borderWidth=-2)
    ## Initializing Control Variables
    controlVariable=0
    maxControlVariable=72
    changeControlVariable=False
    ## Connecting To Firebase
    _thread.start_new_thread(network.connect,())
    ## Initializing Clock
    clock=pygame.time.Clock()
    while controlVariable<=maxControlVariable:
        #print(controlVariable,network.override,network.status)
        clock.tick(24)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                network.endGame()
                pygame.quit()
                quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                xPos,yPos=pygame.mouse.get_pos()
                if backButton.rect.collidepoint(xPos,yPos):
                    network.endGame()
                    return()
        ## Updating GUI
        window.fill((0,0,0))
        if network.status!=lastStatus:
            loader.counter+=1
            lastStatus=network.status
        loader.update()
        loaderText.changeText(network.status,window)
        loaderText.update(window)
        backButton.draw(window)
        pygame.display.update()
        ## Changing Control Variables
        if changeControlVariable:
            controlVariable+=1
        ## Checking For Network Override
        if network.override:
            loaderText.textColor=(240,50,50)
            changeControlVariable=True
        ## Checking For Completion 
        if network.gameOnGoing==True:
            controlVariable=maxControlVariable+1
        elif network.gameOnGoing==False:
            changeControlVariable=True
    print(network.gameID)
    ## Creating GUI For Game Screen
    gameBoard=GUI.board((200,200,300,300),userActive=bool(network.playerID%2))
    print(gameBoard.userActive)
    ## Creating Opponent Character
    if network.opponentChar==0:
        opponentChar=Character.Kiaria((50,50,100,100),72)
    elif network.opponentChar==1:
        opponentChar=Character.Lochem((50,50,100,100),72)
    elif network.opponentChar==2:
        opponentChar=Character.Mayvheen((50,50,100,100),72)
    elif network.opponentChar==3:
        opponentChar=Character.Raymond((50,50,100,100),72)
    elif network.opponentChar==4:
        opponentChar=Character.Veera((50,50,100,100),72)
    opponentChar.speechText=f"Hi I Am {network.opponentName}"
    ## Creating User Character
    if characterID==0:
        userChar=Character.Kiaria((50,550,100,100))
    elif characterID==1:
        userChar=Character.Lochem((50,550,100,100))
    elif characterID==2:
        userChar=Character.Mayvheen((50,550,100,100))
    elif characterID==3:
        userChar=Character.Raymond((50,550,100,100))
    elif characterID==4:
        userChar=Character.Veera((50,550,100,100))
    ## Text GUI Elements
    timerText=OriginTechFont.originTechFont("30/30",(625,50),window,textColor=(240,50,50))
    loaderText=OriginTechFont.originTechFont(network.status,(350,350),window)
    ## Timer Contoller Variable
    controlVariable,changeControlVariable=0,False
    timerValue=0
    while controlVariable<=maxControlVariable:
        clock.tick(24)
        events=pygame.event.get()
        for event in events:
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        ## Changing Control Variables
        if changeControlVariable:
            controlVariable+=1
            if controlVariable==maxControlVariable:
                network.endGame()
        ## Game Board Override
        if gameBoard.gameEnded:
            timerValue-=1
            changeControlVariable=True
        ## Updating GUI
        userChar.userActive=gameBoard.userActive
        opponentChar.userActive=not(gameBoard.userActive)
        window.fill((0,0,0))
        gameBoard.update()
        gameBoard.draw(window)
        userChar.update()
        userChar.draw(window)
        opponentChar.update()
        opponentChar.draw(window)
        timerText.update(window)
        pygame.display.update()
        ## Updating Timer Controller
        timerValue+=1
        timerText.changeText(str(int(30-timerValue//24))+"/30",window)
        if timerValue==24*30:
            ## Special Condition For No Moves
            if len(gameBoard.currentMoves)==0 and network.playerID==1:
                timerValue-=1
                loaderText.changeText("You Lost By Timeout",window)
                loaderText.update(window)
                pygame.display.update()
                gameBoard.userActive=False
                changeControlVariable=True
            ## Condition For User Wins
            elif (len(gameBoard.currentMoves)*network.playerID)%2==1 or (len(gameBoard.currentMoves)*network.playerID)%4==0 and not(len(gameBoard.currentMoves)==0 and network.playerID==2):
                timerValue-=1
                loaderText.changeText("You Won By Timeout",window)
                loaderText.update(window)
                pygame.display.update()
                gameBoard.userActive=False
                changeControlVariable=True
            ## Condition For User Loose
            else:
                timerValue-=1
                loaderText.changeText("You Lost By Timeout",window)
                loaderText.update(window)
                pygame.display.update()
                gameBoard.userActive=False
                changeControlVariable=True
        ## Updating Game
        if not(changeControlVariable):
            if gameBoard.userActive:
                gameBoard.eventHandler(events,window)
                if gameBoard.currentMoves!=network.currentMoves:
                    network.currentMoves=gameBoard.currentMoves.copy()
                    network.sendGame()
                    gameBoard.userActive=False
                    timerValue=0
            else:
                ## Getting Game Moves
                if not(network.threadStarted):
                    _thread.start_new_thread(network.getGame,())
                    network.threadStarted=True
                if network.currentMoves!=gameBoard.currentMoves:
                    gameBoard.currentMoves=network.currentMoves.copy()
                    gameBoard.userActive=True
                    network.threadStarted=False
                    timerValue=0

        
        
        



if __name__=="__main__":
    pygame.init()
    window=pygame.display.set_mode((700,700))
    againstAI(window,isEven=False)
