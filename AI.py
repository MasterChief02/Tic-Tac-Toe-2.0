import random


class AI():
    def __init__(self,isEven=True,level=0):  ## 0->Hard; 1->Moderate; 2->Easy
        ## Stroring Attributes
        self.storedLevel=level
        self.level=0
        self.currentMoves=[]
        self.isEven=isEven
        self.state=5

        ## Storing Generated Data
        outputList,statsDict=[],{}
        self.moves(outputList,statsDict)
        self.outputList=outputList
        self.statsDict=statsDict
        
    ## Function To Generate All Possible Moves And Their Outcomes
    def moves(self,outputList,statsDict,currentMoves=[]):
        def win(currentMovesList):
            oddMoves=list(currentMovesList[i] for i in range(len(currentMovesList)) if i%2==1)
            evenMoves=list(currentMovesList[i] for i in range(len(currentMovesList)) if i%2==0)
            if (1 in oddMoves and 2 in oddMoves and 3 in oddMoves) or (4 in oddMoves and 5 in oddMoves and 6 in oddMoves) or (7 in oddMoves and 8 in oddMoves and 9 in oddMoves) or (1 in oddMoves and 4 in oddMoves and 7 in oddMoves) or (2 in oddMoves and 5 in oddMoves and 8 in oddMoves) or (3 in oddMoves and 6 in oddMoves and 9 in oddMoves) or (1 in oddMoves and 5 in oddMoves and 9 in oddMoves) or (3 in oddMoves and 5 in oddMoves and 7 in oddMoves):
                return("odd")
            elif (1 in evenMoves and 2 in evenMoves and 3 in evenMoves) or (4 in evenMoves and 5 in evenMoves and 6 in evenMoves) or (7 in evenMoves and 8 in evenMoves and 9 in evenMoves) or (1 in evenMoves and 4 in evenMoves and 7 in evenMoves) or (2 in evenMoves and 5 in evenMoves and 8 in evenMoves) or (3 in evenMoves and 6 in evenMoves and 9 in evenMoves) or (1 in evenMoves and 5 in evenMoves and 9 in evenMoves) or (3 in evenMoves and 5 in evenMoves and 7 in evenMoves):
                return("even")
            else:
                return("na")

        
        availbleMoves=list(i for i in range(1,10) if i not in currentMoves)
        if win(currentMoves)=="na" and availbleMoves!=[]:
            returnList=[]
            for i in availbleMoves:
                tempcurrentMoves=currentMoves.copy()
                tempcurrentMoves.append(i)
                resultList=self.moves(outputList,statsDict,tempcurrentMoves)
                returnList.extend(resultList)
                wins,loss,draw=0,0,0
                for movesList in resultList:
                    try:
                        print(int(movesList))
                    except:
                        pass
                    result=win(movesList)
                    if result=="even":
                        wins+=1
                    elif result=="odd":
                        loss+=1
                    else:
                        draw+=1
                    statsDict[str(tempcurrentMoves)]=[wins/len(resultList),loss/len(resultList),draw/len(resultList)]
            return(returnList)
        else:
            result=win(currentMoves)
            if result=="even":
                statsDict[str(currentMoves)]=[1,0,0]
            elif result=="odd":
                statsDict[str(currentMoves)]=[0,1,0]
            else:
                statsDict[str(currentMoves)]=[0,0,1]
            return([currentMoves])

    def nextMove(self):
        availbleMoves=list(i for i in range(1,10) if i not in self.currentMoves)
        if len(availbleMoves)==9:
            return(random.randint(1,9))
        tempDict={}
        for i in availbleMoves:
            if self.isEven:
                score=self.statsDict[str(self.currentMoves+[i])][0]-self.statsDict[str(self.currentMoves+[i])][1]+self.statsDict[str(self.currentMoves+[i])][2]
            else:
                score=self.statsDict[str(self.currentMoves+[i])][1]-self.statsDict[str(self.currentMoves+[i])][0]+self.statsDict[str(self.currentMoves+[i])][2]
            tempDict[score]=i
        scoreList=list(tempDict.keys())
        scoreList.sort(reverse=True)
        self.levelUpdate()
        if len(scoreList)==1:
            self.currentMoves.append(availbleMoves[0])
        elif len(scoreList)==2:
            if self.level==0:
                self.currentMoves.append(tempDict[scoreList[0]])
            else:
                self.currentMoves.append(tempDict[scoreList[1]])
        else:
            self.currentMoves.append(tempDict[scoreList[self.level]])
        self.stateUpdate()
        return(self.currentMoves[-1])

    def levelUpdate(self):
        self.level=(self.level+1)%(self.storedLevel+1)

    def stateUpdate(self):
        if self.isEven:
            c=10
        else:
            c=-10
        self.state=c*(self.statsDict[str(self.currentMoves)][0]-self.statsDict[str(self.currentMoves)][1]+self.statsDict[str(self.currentMoves)][2])%(2)

if __name__=="__main__":
    bot=AI()
    print(bot.nextMove())