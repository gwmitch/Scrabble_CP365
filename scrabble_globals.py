
# Size of tile images
TILE_SIZE = 38

# Border between each tile location on the board
BORDER_SIZE = 2

# Show the graphics or not?
VISUALIZE = False

# Which word list to use
WORDLIST_FILENAME = "wordlists/short_words.txt"

SHOW_DEFINITIONS = False

# Images subdirectory
IMAGES_DIR = "images/"

# Board background image
BOARD_FILENAME = IMAGES_DIR + "board.png"

# Store the current game state image in this file for viewing purposes
BOARD_STATE_IMAGE = IMAGES_DIR + "current_state.png"

# Python executable (for launching the viewer in a separate process)
# If "python" doesn't launch the correct interpreter for your system, then change this (e.g. "python2.7")
PYTHON_EXECUTABLE = "python"

#

# Change the size of the game's board
# Visualization will not work with values other than 15!!!!
BOARD_SIZE = 15  # 15 is standard Scrabble board

RACK_MAX_SIZE = 7

BOARD_WORD_MULTIPLIERS = {
    (0, 0): 3,
    (0, 7): 3,
    (0, 14):3,
    (7, 0): 3,
    (7, 14):3,
    (14, 0): 3,
    (14, 7): 3,
    (14, 14):3,
    (1,1):2,
    (1,13):2,
    (2,2):2,
    (2,12):2,
    (3,3):2,
    (3,11):2,
    (4,4):2,
    (4,10):2,
    (7,7):2,
    (10,4):2,
    (10,10):2,
    (11,3):2,
    (11,11):2,
    (12,2):2,
    (12,12):2,
    (13,1):2,
    (13,13):2,
}

BOARD_LETTER_MULTIPLIERS = {
    (0, 3):2,
    (0, 11):2,
    (1, 5):3,
    (1, 9):3,
    (2, 6):2,
    (2, 8):2,
    (3, 0):2,
    (3, 7):2,
    (3,14):2,
    (5,1):3,
    (5,5):3,
    (5,9):3,
    (5,13):3,
    (6,2):2,
    (6,6):2,
    (6,8):2,
    (6,12):2,
    (7, 3):2,
    (7, 11):2,
    (8,2):2,
    (8,6):2,
    (8,8):2,
    (8,12):2,
    (9,1):3,
    (9,5):3,
    (9,9):3,
    (9,13):3,
    (11, 0):2,
    (11, 7):2,
    (11,14):2,
    (12, 6):2,
    (12, 8):2,
    (13, 5):3,
    (13, 9):3,
    (14, 3):2,
    (14, 11):2,
}

TILE_POINTS = {
    'a':1,
    'b':3,
    'c':3,
    'd':2,
    'e':1,
    'f':4,
    'g':2,
    'h':4,
    'i':1,
    'j':8,
    'k':5,
    'l':1,
    'm':3,
    'n':1,
    'o':1,
    'p':3,
    'q':10,
    'r':1,
    's':1,
    't':1,
    'u':1,
    'v':4,
    'w':4,
    'x':8,
    'y':4,
    'z':10
}
