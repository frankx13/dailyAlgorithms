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

def create_2d_chessboard(side_length):
    a, b = side_length, side_length
    chessboard_dictionary = {}

    letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    pointer = 0
    indexer_letter = 'a'
    indexer_number = 0

    while pointer != 64:
        pointer += 1
        if indexer_number <= 8:
            indexer_letter = letters_list[0] + str(pointer)
            indexer_number = pointer
        elif 16 >= indexer_number > 8:
            indexer_letter = letters_list[1] + str(pointer)
            indexer_number = pointer
        elif 24 >= indexer_number > 16:
            indexer_letter = letters_list[2] + str(pointer)
            indexer_number = pointer
        elif 32 >= indexer_number > 24:
            indexer_letter = letters_list[3] + str(pointer)
            indexer_number = pointer
        elif 40 >= indexer_number > 32:
            indexer_letter = letters_list[4] + str(pointer)
            indexer_number = pointer
        elif 48 >= indexer_number > 40:
            indexer_letter = letters_list[5] + str(pointer)
            indexer_number = pointer
        elif 56 >= indexer_number > 48:
            indexer_letter = letters_list[6] + str(pointer)
            indexer_number = pointer
        elif 64 >= indexer_number > 56:
            indexer_letter = letters_list[7] + str(pointer)
            indexer_number = pointer

        chessboard_dictionary[indexer_letter] = indexer_number

    print(chessboard_dictionary)


chess_side_length = 8
create_2d_chessboard(chess_side_length)
# TODO: Replace the chessboard_dictionary 1D by another in 2D
