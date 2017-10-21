"""

Remove Essential Primes (RemEssPrimes.py)

Authors: Arvind, Shantanu, Sripathi

Accepts an input file containing prime implicant table (with or without cost)
and returns the reduced matrix without the essential prime implicants and a list
of essential prime implicants. Checks rows for min-terms covered by only one implicant
and removes that row as well as every other row corresponding to a min-term covered by
the essential prime implicant.

"""

import numpy as np


def RemEssPrimes(filename):

    PCNread = open(filename, "r")

    # Reading all lines of the file
    data = PCNread.readlines()
    data = [line.rstrip('\n') for line in data]

    # Getting the variable splitting order
    cost = data[0]
    cost = cost.split(" ")
    cost = np.array(list(map(int, cost)))
    # print(cost)

    matrix = np.array([])  # TODO
    for item in data[1:]:
        item = item.split(" ")
        temp = np.asarray(item)
        if matrix.size == 0:
            matrix = temp
        else:
            matrix = np.vstack((matrix, temp))
        matrix = np.atleast_2d(matrix)
    matrix = np.copy(matrix.astype(int))
    # print(matrix)

    # TODO: "A" Matrix is obtained
    # matrix = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
    # matrix = np.array([[1, 0, 1], [1, 1, 0], [1, 1, 1]])
    # cost = np.array([3, 1, 1])  # TODO : Fill this array with costs
    row_sum = np.sum(matrix, axis=1)
    index_1 = np.where((row_sum == 1), row_sum, 0).nonzero()[0]
    col_interested = np.zeros(matrix.shape[0])
    rows_gone = list()
    implicants = list()
    for i in index_1:
        # rows_gone.append(i)
        row_interested = matrix[i, :]
        col_ind = np.where((row_interested == 1), row_interested, 0).nonzero()[0]
        implicants.append(col_ind[0])
        col_interested += matrix[:, col_ind].flatten('F')
        col_interested[col_interested>1] = 1

    rows_gone.append(np.where((col_interested == 1), col_interested, 0).nonzero()[0])
    rows_gone = np.asarray(rows_gone[0])
    good_matrix = np.delete(matrix, rows_gone, 0)

    return good_matrix, implicants, cost
    # print(good_matrix)
