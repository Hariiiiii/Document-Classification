import numpy as np
import nltk

from classify import read_from_file

X = np.array([
    [4, 3],
    [6, 2],
    [2, 5],
    [7, 7],
    [2, 1],
    [7, 4],
    [4, 6],
    [7, 9],
    [3, 3],
    [5, 8],
    [4, 7],
    [8, 7]
], np.int32)

Y = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
], np.int32)

read_from_file('trained_set.txt')

# classify(X, Y)
