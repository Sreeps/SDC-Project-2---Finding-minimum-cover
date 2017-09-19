"""
Finding minimum set of implicants to cover the given function.
Authors: Arvind, Sripathi, Shantanu

"""

import numpy as np

# TODO: "A" Matrix is obtained
matrix = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
matrix = np.array([[1, 0, 1], [1, 1, 0], [1, 1, 1]])
cost = np.array([3, 1, 1])  # TODO : Fill this array with costs
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
# print(good_matrix)
