from operator import itemgetter
from itertools import groupby


def solution(A):
    output = []
    if len(A) <= 4:
        return 1
    for k, g in groupby(enumerate(A), lambda i_x: i_x[0] + i_x[1]):
        output.append(list(map(itemgetter(1), g)))
        print(output)
    return len(output)

A = [1, 5, 4, 9, 8, 7, 12, 13, 14]
print(solution(A))