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
currentDealerHand = 0

# Player
playerBalance = 100  # Starting balance for the player
currentPlayerHand = []  # List to hold player's cards
currentPlayerDeck = []  # Player's current deck
playerHasPassed = False

# Game
gameIsActive = False
winner = ""

# ------

def decideBetAmount():
    global gameIsActive
    print("Test")
    gameIsActive = True

def dealing():
    print("Dealer is dealing")
    # Dealing
    if not playerHasPassed:
        print("Deal to Player and Dealer")
    else:
        print("Deal to dealer only")

def display_deck(currentPlayerDeck):
    print("\nYour current hand:")
    # Initialize a list to hold each line of the displayed cards
    card_lines = ["", "", "", "", ""]  # There are 5 lines in each card display
    for card in currentPlayerDeck:
        for i, line in enumerate(card.split('\n')):
            card_lines[i] += line + "  "  # Add space between cards
    for line in card_lines:
        print(line)  # Print each line of the cards

def givePlayerInput():
    global playerHasPassed
    print("Player decides hit or pass")

    # Let player make input before continuing code
    playerChoice = input("Type 'hit' to draw a card or 'pass' to end your turn: ").strip().lower()

    if playerChoice == "hit":
        print("Player hits")
        card = pick_random_card()
        currentPlayerDeck.append(card)  # Add the picked card to the player's deck
        display_deck(currentPlayerDeck)  # Display the updated deck
    elif playerChoice == "pass":
        playerHasPassed = True
    else:
        print("Invalid choice. Try again.")
        givePlayerInput()  # Repeat until valid input

def checkForWinOrLoss():
    global gameIsActive
    print("Check for win or loss")

    if winner == "player":
        gameIsActive = False
        print("Player won")
    elif winner == "dealer":
        gameIsActive = False
        print("Dealer won")
    else:
        print("Continue Game")

# Game Loop
decideBetAmount()

while gameIsActive:
    dealing()
    checkForWinOrLoss()
    givePlayerInput()
