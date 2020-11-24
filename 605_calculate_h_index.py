# This problem was asked by Palantir. In academia, the h-index is a metric used to calculate the impact of a
# researcher's papers. It is calculated as follows: A researcher has index h if at least h of her N papers have h
# citations each. If there are multiple h satisfying this formula, the maximum is chosen. For example, suppose N = 5,
# and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher
# has 3 papers with at least 3 citations. Given a list of paper citations of a researcher, calculate their h-index.


def calculate_h_index(citations):
    indexer = 0
    citations.sort(reverse=True)

    for citation in citations:
        if citation > indexer and not citation == 0:
            indexer += 1
        elif citation == indexer and not citation == 0:
            indexer += 1
        elif citation < indexer and not citation == 0 and not indexer == 0:
            return indexer + 1
        else:
            return indexer


citations_n = [0, 2, 1, 3, 4, 3, 2, 1]
h_index = calculate_h_index(citations_n)
print(h_index)
