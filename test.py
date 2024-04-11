from math import *



bonusStack = []
throwBonus = []
frameBonus = []

class iBowlingField:
    
    def pinsKnockedOver(knocked) -> None:
         pass
    
    def pinsLeft() -> int:
         pass



class bowlingField(iBowlingField):

    def __init__(self) -> None:
        self.pinsAvailable = 10

    def pinsKnockedOver(self, knocked) -> None:
        self.pinsAvailable-=knocked

    def pinsLeft(self) -> int:
        return self.pinsAvailable






def bowlingScore(frames):
    frameArray = frames.split('|')
    score = 0.0

    for frame in frameArray:
        bowlingBane = bowlingField()

        if(len(frame)==0):
            continue

        pinsInFrame = 0
        throwBonus = 0
        strikeBonus = 0

        for throw in frame:
            throwBonus += solveThrow(throw, bowlingBane)
            print("throwbonus"  + str(throwBonus))
 
        pinsInFrame = 10 - bowlingBane.pinsLeft()
        if(hasBonus()):
            if(bonusStack[0] == "X"):
                strikeBonus = pinsInFrame
                bonusStack.pop(0)    

        if(bowlingBane.pinsLeft() == 0):
            bonusStack.append(throw)


        score += pinsInFrame + throwBonus + strikeBonus
        print(str(score) + " so far by this frame: " + frame)
    print(score)
    return score

def hasBonus():
    return len(bonusStack) > 0


def solveThrow(throw, bowlingBane) -> int:
                pins=pinsKnockedDown(throw, bowlingBane.pinsLeft())
                bowlingBane.pinsKnockedOver(pins)
                sparebonus = 0

                if(hasBonus()):
                    if(bonusStack[0] == "/"):
                        sparebonus += pins
                        bonusStack.pop(0)
                return sparebonus


def solveBonus(addedBonus, bonustype):
    bonusStack.pop(0)
    return addedBonus   

def pinsKnockedDown(frame, pinsAvailable):  
    score = 0.0

    if(frame.isnumeric()):
        score +=float(frame)
    elif(frame == "-"):
        score = 0
    else:
        score = pinsAvailable
    return score




framesSingleSpare = "1/|1/|11|11|11|11|11|11|11|11||"
score = bowlingScore(framesSingleSpare)
assert score == 38.0

framesSingleStrike = "X|11|--|--|--|--|--|--|--|--||"
score = bowlingScore(framesSingleStrike)
assert score == 14

framesSpareIntoStrike = "1/|X|--|--|--|--|--|--|--|--||"
score = bowlingScore(framesSpareIntoStrike)
assert score == 30.0

framesStrikeIntoSpare = "--|X|1/|--|--|--|--|--|--|--||"
score = bowlingScore(framesStrikeIntoSpare)
assert score == 30.0

framesStrike = "1-|11|11|11|11|11|11|11|11|11||"
score = bowlingScore(framesStrike)
assert score == 19.0

