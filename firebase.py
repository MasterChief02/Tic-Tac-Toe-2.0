import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("Assets\\test3-61fb0-firebase-adminsdk-r5f0b-1f4d6e4c2d.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://test3-61fb0-default-rtdb.firebaseio.com/"})







class Network():
    def __init__(self,userName,userChar):
        ## Storing Attributes
        self.userName=userName
        self.userChar=userChar
        self.opponentName=""
        self.opponentChar=0
        self.currentMoves=[]
        self.status=""
        self.override=False
        self.gameOnGoing=None
        self.gameID=None
        self.playerID=None
        self.threadStarted=False

    def connect(self):
        ## Find Game
        self.findGame()
        ## Check For isWaiting
        while self.gameOnGoing==None:
            self.isWaiting()

    def findGame(self):
        self.status="Searching Game"
        ## Retrieving Game Data
        rel=db.reference("/Game")
        data=rel.get()
        ## Scanning All The Games
        for i in range(50):
            ## Checking Availabilty For Game
            if not(data[i]["GameOnGoing"]):
                ## Checking Availability For Player 1
                if not(data[i]["Player1Present"]):
                    ## Updating Database
                    rel.child(str(i)).update({"Player1Present":True,"Player1Name":self.userName,"Player1Char":self.userChar})
                    ## Updating Status
                    self.status="Waiting For Opponent"
                    ## Updating Data
                    self.gameID=i
                    self.playerID=1
                    return()
                ## Checking Availability For Player 2
                elif not(data[i]["Player2Present"]):
                    ## Updating Database
                    rel.child(str(i)).update({"Player2Present":True,"Player2Name":self.userName,"Player2Char":self.userChar,"GameOnGoing":True})
                    ## Updating Status
                    self.status="Game Started"
                    ## Updating Data
                    self.gameOnGoing=True
                    self.gameID=i
                    self.playerID=2
                    self.opponentName=data[i]["Player1Name"]
                    self.opponentChar=int(data[i]["Player1Char"])
                    return()
        ## If Game Not Found
        self.status="No Game Found. Please Try Again Later"
        self.override=True
        self.gameOnGoing=False

    def isWaiting(self):
        ## Retrieving Game Data
        rel=db.reference(f"/Game/{self.gameID}")
        data=rel.get()
        ## Checking For Player 2
        if data["Player2Present"]:
            ## Updating Status
            self.status="Game Started"
            self.gameOnGoing=True
            self.opponentName=data["Player2Name"]
            self.opponentChar=int(data["Player2Char"])
        
    def sendGame(self):
        rel=db.reference("/Game")
        rel.child(str(self.gameID)).update({"CurrentMoves":"".join(list(map(str,self.currentMoves)))})

    def getGame(self):
        while self.threadStarted:
            rel=db.reference(f"/Game/{self.gameID}/CurrentMoves")
            self.currentMoves=list(map(int,list(rel.get())))
    
    def endGame(self):
        self.gameOnGoing=False
        rel=db.reference("/Game")
        rel.child(str(self.gameID)).update({"Player1Present":False,"Player1Name":"","Player1Char":0,"Player2Present":False,"Player2Name":"","Player2Char":0,"CurrentMoves":"","GameOnGoing":False})

def resetDB():
    ref = db.reference("/Game")
    data={}
    for i in range(50):
        print(i)
        data[str(i)]={
            "Player1Present":False,
            "Player1Name":"",
            "Player1Char":0,
            "Player2Present":False,
            "Player2Name":"",
            "Player2Char":0,
            "CurrentMoves":"",
            "GameOnGoing":False
        }
    ref.set(data)


def authentication(username,password,characterID=None,isSignUp=True): 
    ## Retrieving Data
    rel=db.reference("/Users")
    data=rel.get()   
    ## For SignUp
    if isSignUp:
        ## Checking For Availability Of Username
        usernameAvailable=(username!="")
        if usernameAvailable and data!=None:
            for key in data.keys():
                if data[key]["username"]==username:
                    usernameAvailable=False
                    break
        ## Pushing Data
        if usernameAvailable:
            rel.push({"username":username,"password":password,"charID":characterID})
            return((username,characterID))
        else:
            return(False)
    ## For Login
    else:
        if data!=None:
            for key in data.keys():
                if data[key]["username"]==username and data[key]["password"]==password:
                    return((username,data[key]["charID"]))
        return(False)


        



if __name__=="__main__":
    #pass
    resetDB()
    #rel=db.reference("/Game/0/CurrentMoves")
    #print(rel.get())
    #print(authentication("YogeshAI","pasword",isSignUp=False))



