## Importing External Dependencies
import _thread, socket, sys

## Importing Libraries
import Resources


############################
## Localhost Host Network ##
############################
class localhostHost():
    def __init__(self,characterID,characterName,userActive=True):
        ## Storing Attributes
        self.status=""
        self.selfCharacterID=characterID
        self.selfCharacterName=characterName
        self.opponentCharacterID=None
        self.opponentName=None
        self.userActive=userActive
        self.game=[]
        self.gameRecord=[]
        self.state=None        ## 0->Send; 1->Receive
        self.connected=None

    
    def connection(self):
        ## Initializing Socket
        socketUsed=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.status="Socket Initialized"
        ## Binding Socket
        try:
            socketUsed.bind((Resources.localhostServer,Resources.localhostPort))
            self.status="Server Started Successfully"
        except:
            self.status="Server Startup Failed. Please Check The Settings"
            self.connected=False
            return(False)
        ## Listening For Connection
        socketUsed.listen(1)
        self.status=f"Waiting For Connections At {Resources.localhostServer.split('.')[3]}"
        while True:
            conn,addr=socketUsed.accept()
            self.status=f"Connected To IP Address: {str(addr)}"
            ## Recieving Opponents Data
            self.opponentCharacterID=int(conn.recv(1048).decode("utf-8"))
            self.opponentName=conn.recv(1048*4).decode("utf-8")
            ## Sendind User Data
            conn.sendall(str(self.selfCharacterID).encode())
            conn.sendall(str(self.selfCharacterName).encode())
            self.status="GTG"
            self.connected=True
            break
        ## Trans-Recieving Game Data
        while True:
            if self.userActive:
                if self.state==0:
                    conn.sendall("".join(list(map(str,self.game))).encode())
                    self.userActive=False
                    self.state=1
                    print(self.userActive,"".join(list(map(str,self.game))))
            else:
                self.game=list(map(int, list(conn.recv(1048*2).decode("utf-8"))))
                self.userActive=True               
                print(self.game)


##############################
## Localhost Client Network ##
##############################
class localhostClient():
    def __init__(self,gameServer,characterID,characterName,userActive=False):
        ## Storing Attributes
        self.status=""
        self.gameServer=gameServer
        self.selfCharacterID=characterID
        self.selfCharacterName=characterName
        self.opponentCharacterID=None
        self.opponentName=None
        self.userActive=userActive
        self.game=[]
        self.state=None        ## 0->Send; 1->Receive
        self.connected=None

    def connection(self):
        ## Initializing Socket
        socketUsed=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.status="Socket Initialized"
        ## Connecting To Server
        try:
            socketUsed.connect((self.gameServer,Resources.localhostPort))
            self.status="Connected To Server Successfully"
        except:
            self.status="Couldn't Connect To Server"
            self.connected=False
            return(False)
        ## Sendind User Data
        socketUsed.sendall(str(self.selfCharacterID).encode())
        socketUsed.sendall(str(self.selfCharacterName).encode())
        ## Recieving Opponents Data
        self.opponentCharacterID=int(socketUsed.recv(1048).decode("utf-8"))
        self.opponentName=socketUsed.recv(1048*4).decode("utf-8")
        self.status="GTG"
        self.connected=True
        ## Trans-Recieving Game Data
        while True:
            if self.userActive:
                if self.state==0:
                    socketUsed.sendall("".join(list(map(str,self.game))).encode())
                    self.userActive=False
                    self.state=1
                    print(self.userActive)
            else:
                self.game=list(map(int, list(socketUsed.recv(1048*2).decode("utf-8"))))
                self.userActive=True               
                print(self.game)