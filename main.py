import random
# Code here
CARD_VALUES = [
    # Aces
    [
        ".-------.\n|A      |\n|   ♠   |\n|      A|\n'-------'",  # Ace of Spades
        ".-------.\n|A      |\n|   ♥   |\n|      A|\n'-------'"   # Ace of Hearts
    ],

    # 2s
    [
        ".-------.\n|2      |\n|   ♠   |\n|      2|\n'-------'",  # 2 of Spades
        ".-------.\n|2      |\n|   ♥   |\n|      2|\n'-------'"   # 2 of Hearts
    ],

    # 3s
    [
        ".-------.\n|3      |\n|   ♠   |\n|      3|\n'-------'",  # 3 of Spades
        ".-------.\n|3      |\n|   ♥   |\n|      3|\n'-------'"   # 3 of Hearts
    ],

    # 4s
    [
        ".-------.\n|4      |\n|   ♠   |\n|      4|\n'-------'",  # 4 of Spades
        ".-------.\n|4      |\n|   ♥   |\n|      4|\n'-------'"   # 4 of Hearts
    ],

    # 5s
    [
        ".-------.\n|5      |\n|   ♠   |\n|      5|\n'-------'",  # 5 of Spades
        ".-------.\n|5      |\n|   ♥   |\n|      5|\n'-------'"   # 5 of Hearts
    ],

    # 6s
    [
        ".-------.\n|6      |\n|   ♠   |\n|      6|\n'-------'",  # 6 of Spades
        ".-------.\n|6      |\n|   ♥   |\n|      6|\n'-------'"   # 6 of Hearts
    ],

    # 7s
    [
        ".-------.\n|7      |\n|   ♠   |\n|      7|\n'-------'",  # 7 of Spades
        ".-------.\n|7      |\n|   ♥   |\n|      7|\n'-------'"   # 7 of Hearts
    ],

    # 8s
    [
        ".-------.\n|8      |\n|   ♠   |\n|      8|\n'-------'",  # 8 of Spades
        ".-------.\n|8      |\n|   ♥   |\n|      8|\n'-------'"   # 8 of Hearts
    ],

    # 9s
    [
        ".-------.\n|9      |\n|   ♠   |\n|      9|\n'-------'",  # 9 of Spades
        ".-------.\n|9      |\n|   ♥   |\n|      9|\n'-------'"   # 9 of Hearts
    ],

    # 10s
    [
        ".-------.\n|10     |\n|   ♠   |\n|     10|\n'-------'",  # 10 of Spades
        ".-------.\n|10     |\n|   ♥   |\n|     10|\n'-------'"   # 10 of Hearts
    ],

    # Jacks
    [
        ".-------.\n|J      |\n|   ♠   |\n|      J|\n'-------'",  # Jack of Spades
        ".-------.\n|J      |\n|   ♥   |\n|      J|\n'-------'"   # Jack of Hearts
    ],

    # Queens
    [
        ".-------.\n|Q      |\n|   ♠   |\n|      Q|\n'-------'",  # Queen of Spades
        ".-------.\n|Q      |\n|   ♥   |\n|      Q|\n'-------'"   # Queen of Hearts
    ],

    # Kings
    [
        ".-------.\n|K      |\n|   ♠   |\n|      K|\n'-------'",  # King of Spades
        ".-------.\n|K      |\n|   ♥   |\n|      K|\n'-------'"   # King of Hearts
    ]
]

def pick_random_card():
  suit_index = random.choice([0, 1])
  card = random.choice(CARD_VALUES)
  for line in card[suit_index].split('\n'):
    print(line)

pick_random_card()
