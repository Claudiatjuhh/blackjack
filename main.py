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
    return card[suit_index]

# Variables
# Dealer

    for line in card[suit_index].split('\n'):
        print(line)

#Variables
#Dealer

currentDealerHand = 0
dealerHasPassed = False


# Player
playerBalance = 1000  # Starting balance for the player
currentPlayerDeck = []  # Player's current deck
currentScore = 0  # Current score of the player
totalBet = 0
currentPlayerHand = 0

playerHasPassed = False

# Game
gameIsActive = False
finalCheck = False
winner = ""

# ------

def decideBetAmount():
    # Player's starting balance
    global playerBalance
    global totalBet
    global gameIsActive
    
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
    global currentScore
    print("Dealer is dealing")
    # Dealing one card to the player
    card = pick_random_card()
    currentPlayerDeck.append(card)  # Add the picked card to the player's deck
    currentScore += calculate_card_value(card)  # Update score
    display_deck(currentPlayerDeck)  # Display the initial hand
    print(f"Your current score: {currentScore}")  # Show the current score

    # Dealing one more card to the player
    card = pick_random_card()
    currentPlayerDeck.append(card)  # Add the picked card to the player's deck
    currentScore += calculate_card_value(card)  # Update score
    display_deck(currentPlayerDeck)  # Display the initial hand
    print(f"Your current score: {currentScore}")  # Show the current score

def calculate_card_value(card):
    if "A" in card:  # If the card is an Ace
        return 11 if currentScore + 11 <= 21 else 1  # Choose 11 if it doesn't bust
    if "K" in card or "Q" in card or "J" in card or "10" in card:  # 10, J, Q, K
        return 10
    # Extract the numeric value for 2-9
    for char in card:
        if char.isdigit():
            return int(char)
    return 0

def display_deck(currentPlayerDeck):
    print("\nYour current hand:")
    card_lines = ["", "", "", "", ""]  # There are 5 lines in each card display
    for card in currentPlayerDeck:
        for i, line in enumerate(card.split('\n')):
            card_lines[i] += line + "  "  # Add space between cards
    for line in card_lines:
        print(line)  # Print each line of the cards

def update_current_score():
    global currentScore
    currentScore = sum(calculate_card_value(card) for card in currentPlayerDeck)

    # Dealing
    if playerHasPassed == False:
        print("Deal to Player and Dealer")

    elif playerHasPassed == True and currentDealerHand >= 17:
        print("Don't deal to anyone")
        finalCheck = True
    else:
        print("Deal to dealer only")


def givePlayerInput():
    global playerHasPassed
    print("Player decides hit or pass")

    # Let player make input before continuing code
    playerChoice = input("Type 'hit' to draw a card or 'pass' to end your turn: ").strip().lower()

    if playerChoice == "hit":
        print("Player hits")
        card = pick_random_card()
        currentPlayerDeck.append(card)  # Add the picked card to the player's deck
        update_current_score()  # Update current score
        display_deck(currentPlayerDeck)  # Display the updated deck
        print(f"Your current score: {currentScore}")  # Display updated score
        if currentScore > 21:  # Check for bust
            print("You busted! Current score exceeded 21.")
            return False  # Signal that the game should end
    elif playerChoice == "pass":
        playerHasPassed = True
    else:
        print("Invalid choice. Try again.")
        givePlayerInput()  # Repeat until valid input

    return True  # Continue the game if player hasn't busted or passed
  
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
    global gameIsActive
    global winner

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

# Game Loop
decideBetAmount()

while gameIsActive:
    if(currentPlayerDeck == []):
      dealing()
    if not givePlayerInput():  # Check if the player busted after hitting
        break  # Exit loop if player busts
    checkForWinOrLoss()
    if (playerHasPassed == False and currentDealerHand < 21 and currentPlayerHand < 21):
        givePlayerInput()
