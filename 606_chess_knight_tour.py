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
# Initial knight's position will be in H1 - case 57 (this will be the starting point 0 with x = 1 and y = 1)

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
        self.x = 1
        self.y = 1
        self.predicted_x = 1
        self.predicted_y = 1
        self.cases_already_visited = {}

        self.start_left_possible = False
        self.start_up_possible = False
        self.start_right_possible = False
        self.start_down_possible = False

        self.end_left_possible = False
        self.end_up_possible = False
        self.end_right_possible = False
        self.end_down_possible = False

        self.start_possible_moves = []
        self.possible_moves = []

        self.start_predict_moves = []
        self.possible_moves_predicted_actual = []
        self.possible_moves_predicted_clone = []

        self.best_predict_move = 'Null'

    # Move the knight on the chessboard
    # Left move is x-2, y ||| Upward move is x, y +2 ||| Right move is x+2, y ||| Down move is x, y-2
    def scan_possible_movements(self):
        self.check_left_start()
        self.check_up_start()
        self.check_right_start()
        self.check_down_start()

        for possibility in self.start_possible_moves:
            if possibility == 'left' or possibility == 'right':
                self.check_up_end(possibility)
                self.check_down_end(possibility)
            elif possibility == 'up' or possibility == 'down':
                self.check_left_end(possibility)
                self.check_right_end(possibility)

        print(f"First move list : {self.possible_moves}")
        self.predict_next_move(self.possible_moves)

    # Check if there is enough room to move on a side
    def check_left_start(self):
        if (self.x - 2) > 0:
            self.start_possible_moves.append('left')

    def check_up_start(self):
        if (self.y + 2) < 8:
            self.start_possible_moves.append('up')

    def check_right_start(self):
        if (self.x + 2) < 8:
            self.start_possible_moves.append('right')

    def check_down_start(self):
        if (self.y - 2) > 0:
            self.start_possible_moves.append('down')

    def check_left_end(self, start_movement):
        if start_movement == 'up':
            if (self.x - 1) > 0:
                self.possible_moves.append('up_left')

        if start_movement == 'down':
            if (self.x - 1) > 0:
                self.possible_moves.append('down_left')

    def check_up_end(self, start_movement):
        if start_movement == 'left':
            if (self.y + 1) < 8:
                self.possible_moves.append('left_up')

        if start_movement == 'right':
            if (self.y + 1) < 8:
                self.possible_moves.append('right_up')

    def check_right_end(self, start_movement):
        if start_movement == 'up':
            if (self.x + 1) < 8:
                self.possible_moves.append('up_right')

        if start_movement == 'down':
            if (self.x + 1) < 8:
                self.possible_moves.append('down_right')

    def check_down_end(self, start_movement):
        if start_movement == 'left':
            if (self.y - 1) > 0:
                self.possible_moves.append('left_down')

        if start_movement == 'right':
            if (self.y - 1) > 0:
                self.possible_moves.append('right_down')

    def predict_next_move(self, list_possible_moves):
        for move in list_possible_moves:
            self.predicted_x = 0
            self.predicted_y = 0

            if move == 'left_up':
                self.predicted_x -= 2
                self.predicted_y += 1

            elif move == 'left_down':
                self.predicted_x -= 2
                self.predicted_y -= 1

            elif move == 'up_left':
                self.predicted_x -= 1
                self.predicted_y += 2

            elif move == 'up_right':
                self.predicted_x += 1
                self.predicted_y += 2

            elif move == 'right_up':
                self.predicted_x += 2
                self.predicted_y += 1

            elif move == 'right_down':
                self.predicted_x += 2
                self.predicted_y -= 1

            elif move == 'down_left':
                self.predicted_x -= 1
                self.predicted_y -= 2

            elif move == 'down_right':
                self.predicted_x += 1
                self.predicted_y -= 2

            if 8 > self.predicted_x > 0 and 8 > self.predicted_y > 0:
                self.count_predicted_possibilities(move)

        print(self.possible_moves_predicted_actual)

    def count_predicted_possibilities(self, move_tested):
        self.possible_moves_predicted_clone.clear()
        self.check_predict_left_start()
        self.check_predict_up_start()
        self.check_predict_right_start()
        self.check_predict_down_start()

        for possibility_predict in self.start_predict_moves:
            if possibility_predict == 'left' or possibility_predict == 'right':
                self.check_predict_up_end(possibility_predict)
                self.check_predict_down_end(possibility_predict)
            elif possibility_predict == 'up' or possibility_predict == 'down':
                self.check_predict_left_end(possibility_predict)
                self.check_predict_right_end(possibility_predict)

        print(f"\nSecond move list for {move_tested} first movement : \n{self.possible_moves_predicted_clone}")
        actual_list_size = len(self.possible_moves_predicted_actual)
        actual_clone_size = len(self.possible_moves_predicted_clone)
        print(f"Actual list is {actual_list_size} long, clone list is {actual_clone_size} long.")

        if actual_list_size == 0 or actual_list_size >= actual_clone_size:
            self.possible_moves_predicted_actual = self.clone_list(self.possible_moves_predicted_clone)
            print(f"Actual list is {actual_list_size} long, clone list is {actual_clone_size} long.")
            self.best_predict_move = move_tested
            print(f"Best move is {self.best_predict_move} until now.")

    def check_predict_left_start(self):
        if (self.predicted_x - 2) > 0:
            self.start_predict_moves.append('left')

    def check_predict_up_start(self):
        if (self.predicted_y + 2) < 8:
            self.start_predict_moves.append('up')

    def check_predict_right_start(self):
        if (self.predicted_x + 2) < 8:
            self.start_predict_moves.append('right')

    def check_predict_down_start(self):
        if (self.predicted_y - 2) > 0:
            self.start_predict_moves.append('down')

    def check_predict_left_end(self, start_movement):
        if start_movement == 'up':
            if (self.predicted_x - 1) > 0:
                self.possible_moves_predicted_clone.append('up_left')

        if start_movement == 'down':
            if (self.predicted_x - 1) > 0:
                self.possible_moves_predicted_clone.append('down_left')

    def check_predict_up_end(self, start_movement):
        if start_movement == 'left':
            if (self.predicted_y + 1) < 8:
                self.possible_moves_predicted_clone.append('left_up')

        if start_movement == 'right':
            if (self.predicted_y + 1) < 8:
                self.possible_moves_predicted_clone.append('right_up')

    def check_predict_right_end(self, start_movement):
        if start_movement == 'up':
            if (self.predicted_x + 1) < 8:
                self.possible_moves_predicted_clone.append('up_right')

        if start_movement == 'down':
            if (self.predicted_x + 1) < 8:
                self.possible_moves_predicted_clone.append('down_right')

    def check_predict_down_end(self, start_movement):
        if start_movement == 'left':
            if (self.predicted_y - 1) > 0:
                self.possible_moves_predicted_clone.append('left_down')

        if start_movement == 'right':
            if (self.predicted_y - 1) > 0:
                self.possible_moves_predicted_clone.append('right_down')

    def clone_list(self, list_to_copy):
        list_copy = []
        list_copy.extend(list_to_copy)
        return list_copy


create_2d_chessboard()
my_knight = Knight()
my_knight.scan_possible_movements()
