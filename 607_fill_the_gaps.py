# This problem was asked by Walmart Labs.
# There are M people sitting in a row of N seats, where M < N. Your task is
# to redistribute people such that there are no gaps between any of them, while keeping overall movement to a
# minimum. For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where 0 represents an
# empty seat and 1 represents a person. In this case, one solution would be to place the person on the right in the
# fourth seat. We can consider the cost of a solution to be the sum of the absolute distance each person must move,
# so that the cost here would be five. Given an input such as the one above, return the lowest possible cost of
# moving people to remove all gaps.

def organize_sitting(room_plan_list):
    indexer = 0
    pointer_holes = []
    pointer_people = []

    for element in room_plan_list:
        if element == 0:
            pointer_holes.append(indexer)
        elif element == 1:
            pointer_people.append(indexer)
        indexer += 1


    print(pointer_holes)
    print(pointer_people)


# n = 7, m = 9
people_and_chairs = [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
organize_sitting(people_and_chairs)
