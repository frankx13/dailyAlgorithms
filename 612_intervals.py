# This problem was asked by Stripe.
# Given a collection of intervals, find the minimum number of intervals you need to
# remove to make the rest of the intervals non-overlapping. Intervals can "touch", such as [0, 1] and [1, 2],
# but they won't be considered overlapping. For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the
# last interval can be removed and the first two won't overlap. The intervals are not necessarily sorted in any order.

def find_overlapping_intervals(intervals_collection):
    collection_indexer = {}
    collection_checker = {}
    interval_index = 0

    for interval in intervals_collection:
        interval_index += 1
        for number in intervals_collection[interval]:
            collection_indexer[interval_index] = number
        print(collection_indexer)


interval_1 = range(7, 10)
interval_2 = range(2, 5)
interval_3 = range(5, 8)

list_intervals = {'1': interval_1, '2': interval_2, '3': interval_3}

find_overlapping_intervals(list_intervals)
