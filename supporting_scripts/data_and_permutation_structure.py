from import_manager import *

def permute_data(data, num_permutations):

    length = len(data)
    matrix = np.zeros((num_permutations, length))

    for i in range(num_permutations):
        matrix[i] = np.random.permutation(data)

    return matrix

