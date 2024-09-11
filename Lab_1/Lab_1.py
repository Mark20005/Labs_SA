import os   # for clearing the console
import numpy as np

# function to print the matrix with alternative names
def display_matrix(matrix, alternatives):
    for i in range(matrix.shape[0]):
        print(alternatives[i], matrix[i])

# formula for minimization
def minimize(x, min_value, max_value):
    return (max_value - x) / (max_value - min_value)

# formula for maximization
def maximize(x, min_value, max_value):
    return (x - min_value) / (max_value - min_value)

# function to normalize the matrix based on criteria
def normalize_matrix(matrix, criteria):
    if matrix.shape[0] == len(criteria):
        # max and min elements for each column
        max_in_column = np.max(matrix, axis=0)
        min_in_column = np.min(matrix, axis=0)

        for j in range(matrix.shape[1]):
            if criteria[j] == 1:    # apply maximization formula
                matrix[:, j:j + 1] = np.apply_along_axis(maximize, 0, matrix[:, j:j + 1], min_in_column[j], max_in_column[j])
            else:    # apply minimization formula
                matrix[:, j:j+1] = np.apply_along_axis(minimize, 0, matrix[:, j:j+1], min_in_column[j], max_in_column[j])
        return matrix
    else:
        return False

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # -------------- Menu --------------
    task = int(input('Enter the task number: '))
    if task == 1:
        # -------------- Task 1 --------------

        # names of the lawyers
        lawyer_names = ['A1', 'A2', 'A3', 'A4']

        print('\nEvaluation matrix of alternatives based on criteria:')
        lawyer_ratings = np.array([
          # C1  C2  C3  C4
            [3,  7,  2,  9],    # A1
            [8,  3,  6,  7],    # A2
            [4,  8,  3,  5],    # A3
            [9,  6,  5,  4],    # A4
        ])

        display_matrix(lawyer_ratings, lawyer_names)

        print('\nCriteria weight vector:')
        criteria_weights = np.array([8, 9, 6, 7])
        print(criteria_weights)

        print('\nWeighted scores:')
        weighted_ratings = lawyer_ratings * criteria_weights
        display_matrix(weighted_ratings, lawyer_names)

        print('\nUtility function values:')
        utility_values = np.sum(weighted_ratings, axis=1)
        display_matrix(utility_values, lawyer_names)

        print('\nMaximum utility function value:', end=' ')
        best_lawyer_index = np.argmax(utility_values)
        print(utility_values[best_lawyer_index], '(' + lawyer_names[best_lawyer_index] + ')')
        print('\nTherefore, the best choice is lawyer', lawyer_names[best_lawyer_index])
        input()
    elif task == 2:
        # -------------- Task 2 --------------

        # names of the lawyers
        lawyer_names = ['A1', 'A2', 'A3', 'A4', 'A5']

        # criteria (1 - maximize, -1 - minimize)
        criteria = [1, -1, 1, 1, 1]

        np.set_printoptions(formatter={'all': lambda x: '\t' + str(x)})  # output formatting

        print('\nEvaluation matrix of alternatives based on criteria:')
        lawyer_ratings = np.array([
          # C1  C2  C3  C4  C5
            [85, 30, 22, 0.65, 6],   # A1
            [60, 20, 10, 0.6, 7],    # A2
            [30, 12, 5, 0.45, 5],    # A3
            [75, 24, 13, 0.7, 8],    # A4
            [40, 15, 7, 0.55, 7],    # A5
        ])
        display_matrix(lawyer_ratings, lawyer_names)

        print('\nCriteria weight vector:')
        criteria_weights = np.array([7, 5, 6, 8, 6])
        print(criteria_weights)

        np.set_printoptions(formatter={'all': lambda x: '\t' + f"{x:.5f}"})
        print('\nNormalized ratings:')
        normalized_ratings = normalize_matrix(lawyer_ratings, criteria)
        display_matrix(normalized_ratings, lawyer_names)

        print('\nWeighted scores:')
        weighted_ratings = normalized_ratings * criteria_weights
        display_matrix(weighted_ratings, lawyer_names)

        print('\nUtility function values:')
        utility_values = np.sum(weighted_ratings, axis=1)
        display_matrix(np.column_stack([utility_values]), lawyer_names)

        print('\nMaximum utility function value:', end=' ')
        best_lawyer_index = np.argmax(utility_values)
        print(f"{utility_values[best_lawyer_index]:.5f}", '(' + lawyer_names[best_lawyer_index] + ')')
        print('\nTherefore, the best choice is lawyer', lawyer_names[best_lawyer_index])
        input()
    elif task == 0:
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid task number!')
        input()
