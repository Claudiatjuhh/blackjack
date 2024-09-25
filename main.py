#Variables
#Dealer
currentDealerHand = 0

#Player
playerBalance = 0
currentPlayerHand = 0
playerHasPassed = False

#Game
gameIsActive = False
winner = ""

#------
def decideBetAmount():
    print("Test")

    gameIsActive = True

def dealing():
    print("Dealer is dealing")

    # Dealing
    if playerHasPassed == False:
        print("Deal to Player and Dealer")
    else:
        print("Deal to dealer only")


def givePlayerInput():
    print("Player decides hit or pass")

    #Let player make input before continuing code
    playerChoice = "" #Can be either Hit or Pass

    if (playerChoice) == "Hit":
        print ("Player hit")
    elif (playerChoice) == "Pass":
        playerHasPassed = True
    else:
        return givePlayerInput()
    

def checkForWinOrLoss():
    print("Check for win or loss")



    if winner == "player":
        gameIsActive == False
        print("Player won")
    elif winner == "dealer":
        gameIsActive == False
        print ("Dealer won")
    else:
        print("Continue Game")
    
#Game Loop
decideBetAmount()

while gameIsActive == True:
    dealing()
    
    checkForWinOrLoss()

    givePlayerInput()

    
    