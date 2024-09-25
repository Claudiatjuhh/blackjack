import random

CARD_VALUES = [
    # Aces
    [
        ".-------.\n|A      |\n|   ♠   |\n|      A|\n'-------'",  # Ace of Spades
        ".-------.\n|A      |\n|   ♥   |\n|      A|\n'-------'",  # Ace of Hearts
        ".-------.\n|A      |\n|   ♦   |\n|      A|\n'-------'",  # Ace of Diamonds
        ".-------.\n|A      |\n|   ♣   |\n|      A|\n'-------'"   # Ace of Clubs
    ],

    # 2s
    [
        ".-------.\n|2      |\n|   ♠   |\n|      2|\n'-------'",  # 2 of Spades
        ".-------.\n|2      |\n|   ♥   |\n|      2|\n'-------'",  # 2 of Hearts
        ".-------.\n|2      |\n|   ♦   |\n|      2|\n'-------'",  # 2 of Diamonds
        ".-------.\n|2      |\n|   ♣   |\n|      2|\n'-------'"   # 2 of Clubs
    ],

    # 3s
    [
        ".-------.\n|3      |\n|   ♠   |\n|      3|\n'-------'",  # 3 of Spades
        ".-------.\n|3      |\n|   ♥   |\n|      3|\n'-------'",  # 3 of Hearts
        ".-------.\n|3      |\n|   ♦   |\n|      3|\n'-------'",  # 3 of Diamonds
        ".-------.\n|3      |\n|   ♣   |\n|      3|\n'-------'"   # 3 of Clubs
    ],

    # 4s
    [
        ".-------.\n|4      |\n|   ♠   |\n|      4|\n'-------'",  # 4 of Spades
        ".-------.\n|4      |\n|   ♥   |\n|      4|\n'-------'",  # 4 of Hearts
        ".-------.\n|4      |\n|   ♦   |\n|      4|\n'-------'",  # 4 of Diamonds
        ".-------.\n|4      |\n|   ♣   |\n|      4|\n'-------'"   # 4 of Clubs
    ],

    # 5s
    [
        ".-------.\n|5      |\n|   ♠   |\n|      5|\n'-------'",  # 5 of Spades
        ".-------.\n|5      |\n|   ♥   |\n|      5|\n'-------'",  # 5 of Hearts
        ".-------.\n|5      |\n|   ♦   |\n|      5|\n'-------'",  # 5 of Diamonds
        ".-------.\n|5      |\n|   ♣   |\n|      5|\n'-------'"   # 5 of Clubs
    ],

    # 6s
    [
        ".-------.\n|6      |\n|   ♠   |\n|      6|\n'-------'",  # 6 of Spades
        ".-------.\n|6      |\n|   ♥   |\n|      6|\n'-------'",  # 6 of Hearts
        ".-------.\n|6      |\n|   ♦   |\n|      6|\n'-------'",  # 6 of Diamonds
        ".-------.\n|6      |\n|   ♣   |\n|      6|\n'-------'"   # 6 of Clubs
    ],

    # 7s
    [
        ".-------.\n|7      |\n|   ♠   |\n|      7|\n'-------'",  # 7 of Spades
        ".-------.\n|7      |\n|   ♥   |\n|      7|\n'-------'",  # 7 of Hearts
        ".-------.\n|7      |\n|   ♦   |\n|      7|\n'-------'",  # 7 of Diamonds
        ".-------.\n|7      |\n|   ♣   |\n|      7|\n'-------'"   # 7 of Clubs
    ],

    # 8s
    [
        ".-------.\n|8      |\n|   ♠   |\n|      8|\n'-------'",  # 8 of Spades
        ".-------.\n|8      |\n|   ♥   |\n|      8|\n'-------'",  # 8 of Hearts
        ".-------.\n|8      |\n|   ♦   |\n|      8|\n'-------'",  # 8 of Diamonds
        ".-------.\n|8      |\n|   ♣   |\n|      8|\n'-------'"   # 8 of Clubs
    ],

    # 9s
    [
        ".-------.\n|9      |\n|   ♠   |\n|      9|\n'-------'",  # 9 of Spades
        ".-------.\n|9      |\n|   ♥   |\n|      9|\n'-------'",  # 9 of Hearts
        ".-------.\n|9      |\n|   ♦   |\n|      9|\n'-------'",  # 9 of Diamonds
        ".-------.\n|9      |\n|   ♣   |\n|      9|\n'-------'"   # 9 of Clubs
    ],

    # 10s
    [
        ".-------.\n|10     |\n|   ♠   |\n|     10|\n'-------'",  # 10 of Spades
        ".-------.\n|10     |\n|   ♥   |\n|     10|\n'-------'",  # 10 of Hearts
        ".-------.\n|10     |\n|   ♦   |\n|     10|\n'-------'",  # 10 of Diamonds
        ".-------.\n|10     |\n|   ♣   |\n|     10|\n'-------'"   # 10 of Clubs
    ],

    # Jacks
    [
        ".-------.\n|J      |\n|   ♠   |\n|      J|\n'-------'",  # Jack of Spades
        ".-------.\n|J      |\n|   ♥   |\n|      J|\n'-------'",  # Jack of Hearts
        ".-------.\n|J      |\n|   ♦   |\n|      J|\n'-------'",  # Jack of Diamonds
        ".-------.\n|J      |\n|   ♣   |\n|      J|\n'-------'"   # Jack of Clubs
    ],

    # Queens
    [
        ".-------.\n|Q      |\n|   ♠   |\n|      Q|\n'-------'",  # Queen of Spades
        ".-------.\n|Q      |\n|   ♥   |\n|      Q|\n'-------'",  # Queen of Hearts
        ".-------.\n|Q      |\n|   ♦   |\n|      Q|\n'-------'",  # Queen of Diamonds
        ".-------.\n|Q      |\n|   ♣   |\n|      Q|\n'-------'"   # Queen of Clubs
    ],

    # Kings
    [
        ".-------.\n|K      |\n|   ♠   |\n|      K|\n'-------'",  # King of Spades
        ".-------.\n|K      |\n|   ♥   |\n|      K|\n'-------'",  # King of Hearts
        ".-------.\n|K      |\n|   ♦   |\n|      K|\n'-------'",  # King of Diamonds
        ".-------.\n|K      |\n|   ♣   |\n|      K|\n'-------'"   # King of Clubs
    ]
]

def pick_random_card():
    suit_index = random.choice([0, 1, 2, 3])
    card = random.choice(CARD_VALUES)
    for line in card[suit_index].split('\n'):
        print(line)

#Variables
#Dealer
currentDealerHand = 0
dealerHasPassed = False

#Player
playerBalance = 1000
totalBet = 0
currentPlayerHand = 0
playerHasPassed = False

#Game
gameIsActive = False
finalCheck = False
winner = ""

#------
def decideBetAmount():
    # Player's starting balance
    global playerBalance
    global totalBet
    
    # Coin types with their prices
    coinTypes = {
        "Red": 100,   # Red coin costs 100
        "Blue": 200,  # Blue coin costs 200
        "Black": 500  # Black coin costs 500
    }
    
    selectedCoins = []  # List to track selected coins

    print("\nWelcome to Blackjack! You can choose multiple coins to bet on by entering numbers separated by spaces.")
    print(f"Your current balance is:{playerBalance}")
    print("1. Red coin (100)")
    print("2. Blue coin (200)")
    print("3. Black coin (500)")
    print("Type 'done' after your selection.")
    # Get choices from the user (once)
    choice = input("\nEnter your choices (e.g., '1 2 3' or '1 1 2') followed by 'done' to finish: ").split()

    if 'done' in choice:
        choice.remove('done')  # Remove 'done' from the list of choices

        # Calculate the total bet based on the choices
        for coin in choice:
            if coin == "1":
                selectedCoins.append("Red")
                totalBet += coinTypes["Red"]
            elif coin == "2":
                selectedCoins.append("Blue")
                totalBet += coinTypes["Blue"]
            elif coin == "3":
                selectedCoins.append("Black")
                totalBet += coinTypes["Black"]
            else:
                print(f"Invalid choice '{coin}', skipping...")

        # Check if player has enough balance for the total bet
        if playerBalance >= totalBet:
            playerBalance -= totalBet  # Deduct the total bet from the player's balance
            gameIsActive = True  # Set the game as active
            print("\nBetting complete.")
            print(f"You selected: {', '.join(selectedCoins)}")
            print(f"Total bet: {totalBet}")
            print(f"Remaining balance: {playerBalance}")
        else:
            print(f"\nSorry, you do not have enough balance for this total bet of {totalBet}.")
            print(f"Your balance is only {playerBalance}. No bet was placed.")
    else:
        print("You need to type 'done' after your selection.")

def recieveProfit(totalBet):
    global playerBalance
    profit = totalBet * 2
    playerBalance += profit
    print(f"Profit: {profit}")
    print(f"New balance after adding profit: {playerBalance}")


def dealing():
    print("Dealer is dealing")

    # Dealing
    if playerHasPassed == False:
        print("Deal to Player and Dealer")

    elif playerHasPassed == True and currentDealerHand >= 17:
        print("Don't deal to anyone")
        finalCheck = True
    else:
        print("Deal to dealer only")


def givePlayerInput():
    print("Player decides hit or pass")

    #Let player make input before continuing code
    playerChoice = input("Hit or Pass")
    choice = playerChoice.lower()

    if (choice) == "hit":
        print ("Player hit")
    elif (choice) == "pass":
        playerHasPassed = True
    else:
        print("invalid input")
        return givePlayerInput()
    

def checkForWinOrLoss():
    print("Check for win or loss")

    if currentPlayerHand <= 21 and currentDealerHand > 21:
        winner = "player"
    elif currentPlayerHand > 21 and currentDealerHand <= 22:
        winner = "dealer"
    elif finalCheck == True:
        if currentPlayerHand - currentDealerHand > 0:
            winner = "player"
        elif currentPlayerHand - currentDealerHand < 0:
            winner = "dealer"
        elif currentPlayerHand - currentDealerHand == 0:
            winner = "tie"

    if winner == "player":
        print("Player won")
        gameIsActive == False
        recieveProfit(totalBet)
    elif winner == "dealer":
        print ("Dealer won")
        gameIsActive == False
    elif winner == "tie":
        print ("The game has ended in a tie!")
        gameIsActive == False
    else:
        print("Continue Game")
    
#Game Loop
decideBetAmount()

pick_random_card()

while gameIsActive == True:
    dealing()
    
    checkForWinOrLoss()

    if (playerHasPassed == False and currentDealerHand < 21 and currentPlayerHand < 21):
        givePlayerInput()
