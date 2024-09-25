#Variables
#Dealer
currentDealerHand = 0

#Player
playerBalance = 0
currentPlayerHand = 0
hitOrFoldChoice = ""

#Game
gameIsActive = False
winner = ""

#------
def decideBetAmount():
    print("Test")

    gameIsActive = True

def dealing():
    print("Dealer is dealing")

def givePlayerInput():
    print("Player decides hit or fold")
    playerChoice = "" #Can be either Hit or Fold
    return playerChoice

def checkForWinOrLoss():
    print("Check for win or loss")
    if winner == "player":
        gameIsActive == False
        print("Player won")
    
#Game Loop
decideBetAmount()

while gameIsActive == True:
    dealing()
    
    checkForWinOrLoss()

    hitOrFoldChoice = givePlayerInput()
    if (hitOrFoldChoice) == "Hit":
        dealing()
    elif (hitOrFoldChoice) == "Fold":
        checkForWinOrLoss()