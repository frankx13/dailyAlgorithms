# This problem was asked by Google. A knight's tour (ou algorithme du cavalier ou cavalier d'Euler) is a sequence of
# moves by a knight on a chessboard such that all squares are visited once. Given N, write a function to return the
# number of knight's tours on an N by N chessboard.

# def calculate_cases(chess_side_length):
#     if chess_side_length <= 4:
#         print("The minimum side length must be five")
#     elif chess_side_length >= 11:
#         print("The maximum side length must be t")
#     else:
#         number_cases = list(range(1, chess_side_length * chess_side_length + 1))
#         print(number_cases)
#         return number_cases

# We first consider a classic chessboard of 8x8
# Pour réussir un parcours, il suffit de choisir pour chaque nouveau
# saut une case libre parmi celle offrant le moins de sauts ultérieurs possibles, quitte à annuler les derniers coups
# en cas d'impasse : c'est un exercice classique de programmation.

# Our basic chessboard is going to be ordered like so :
#
# A .   1   2   3   4   5   6   7   8
# B .   9   10  11  12  13  14  15  16
# C .   17  18  19  20  21  22  23  24
# D .   25  26  27  28  29  30  31  32
# E .   33  34  35  36  37  38  39  40
# F .   41  42  43  44  45  46  47  48
# G .   49  50  51  52  53  54  55  56
# H .   57  58  59  60  61  62  63  64
#       .   .   .   .   .   .   .   .
#       1   2   3   4   5   6   7   8
#
# Initial knight's position will be in H1 - case 57 (this will be the starting point 0 with x = 0 and y = 0)

def create_2d_chessboard():
    """Create a 2 dimensional dictionary holding the chessboard coordinates for each case."""
    chessboard_2d_dictionary = {'a': {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8'},
                                'b': {'1': '9', '2': '10', '3': '11', '4': '12', '5': '13', '6': '14', '7': '15',
                                      '8': '16'},
                                'c': {'1': '17', '2': '18', '3': '19', '4': '20', '5': '21', '6': '22', '7': '23',
                                      '8': '24'},
                                'd': {'1': '25', '2': '26', '3': '27', '4': '28', '5': '29', '6': '30', '7': '31',
                                      '8': '32'},
                                'e': {'1': '33', '2': '34', '3': '35', '4': '36', '5': '37', '6': '38', '7': '39',
                                      '8': '40'},
                                'f': {'1': '41', '2': '42', '3': '43', '4': '44', '5': '45', '6': '46', '7': '47',
                                      '8': '48'},
                                'g': {'1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54', '7': '55',
                                      '8': '56'},
                                'h': {'1': '57', '2': '58', '3': '59', '4': '60', '5': '61', '6': '62', '7': '63',
                                      '8': '64'}}

    print(chessboard_2d_dictionary)


class Knight:
    # Position the knight at its starting place
    def __init__(self):
        self.letter = 'h'
        self.number = '57'
        self.x = 0
        self.y = 0
        self.cases_already_visited = {}

    # Move the knight on the chessboard
    def move_knight(self):
        self.check_left_start()
        self.check_up_start()
        self.check_right_start()
        self.check_down_start()

    # Check if there is enough room to move on a side
    def check_left_start(self):

    def check_up_start(self):

    def check_right_start(self):

    def check_down_start(self):

    def check_left_end(self):

    def check_up_end(self):

    def check_right_end(self):

    def check_down_end(self):


create_2d_chessboard()
# create_knight()
