"""
This function checks if all possible combinations of the rows of good matrix covers the function.

Author: Arvind, Sripathi, Shantanu
"""

import numpy as np
from minCover import good_matrix, implicants, cost

no_of_col = len(np.transpose(good_matrix))
global_implicant_list = list()
for i in range(1, 2 ** no_of_col):
    temp_implicant = list()
    temp_implicant.append(implicants.copy())
    character_pos = '{0:0'+str(no_of_col)+'b}'
    chosen = np.array([int(x) for x in character_pos.format(i)[:]])

    # First filter - removing essential implicants
    flag1 = 0
    for imp in implicants:
        if chosen[imp] == 1:
            flag1 = 1
            break
    if flag1 == 1:
        continue
    col_sum = np.zeros(len(good_matrix))
    # Filter 2 - covering check
    for i in list(np.where(chosen == 1)[0]):
        col_sum += good_matrix[:, i]
    flag2 = 0
    for st in col_sum:
        if st == 0:
            flag2 = 1
    if flag2 == 1:
        continue

    # Adding the non-essential implicants
    # print("Added")
    temp_implicant.append(list(np.where(chosen == 1)[0]))
    temp_implicant_flat = [item for sublist in temp_implicant for item in sublist]
    global_implicant_list.append(temp_implicant_flat)
# print(global_implicant_list)

# Finding cost for each cover
costlist = list()
for imp_list in global_implicant_list:
    # imp_list = np.array(imp_list)
    new_cost = 0
    for im in imp_list:
        new_cost += cost[im]
    costlist.append(new_cost)

costlist = np.array(costlist)
final_list = global_implicant_list[np.argmin(costlist)]
print(np.sort(final_list))
