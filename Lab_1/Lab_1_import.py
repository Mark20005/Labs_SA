import pandas as pd
import numpy as np


# Function to display the matrix with alternative names
def display_matrix(df, title):
    print(f"\n{title}")
    print(df.to_string(index=False))


# Formula for minimization
def minimize(x, min_value, max_value):
    return (max_value - x) / (max_value - min_value)


# Formula for maximization
def maximize(x, min_value, max_value):
    return (x - min_value) / (max_value - min_value)


# Function to normalize the matrix based on criteria
def normalize_matrix(df, criteria):
    matrix = df.values
    max_in_column = np.max(matrix, axis=0)
    min_in_column = np.min(matrix, axis=0)

    for j in range(matrix.shape[1]):
        if criteria[j] == 1:  # Apply maximization formula
            matrix[:, j] = maximize(matrix[:, j], min_in_column[j], max_in_column[j])
        else:  # Apply minimization formula
            matrix[:, j] = minimize(matrix[:, j], min_in_column[j], max_in_column[j])

    return pd.DataFrame(matrix, columns=df.columns, index=df.index)


while True:
    # -------------- Menu --------------
    task = int(input('Enter the task number (1 or 2) or 0 to exit: '))

    if task == 0:
        break

    if task == 1:
        # -------------- Task 1 --------------
        # Read the data from CSV or Excel
        matrix_file = input("Enter the file path for Task 1 alternatives matrix (CSV or Excel): ")
        weights_file = input("Enter the file path for Task 1 criteria weights (CSV or Excel): ")

        # Load data into pandas DataFrames
        if matrix_file.endswith('.csv'):
            alternatives_df = pd.read_csv(matrix_file,index_col=None,header=None)
        else:
            alternatives_df = pd.read_excel(matrix_file,index_col=None,header=None)

        if weights_file.endswith('.csv'):
            criteria_weights = pd.read_csv(weights_file, index_col=None,header=None).squeeze().values
        else:
            criteria_weights = pd.read_excel(weights_file, index_col=None,header=None).squeeze().values

        display_matrix(alternatives_df, "Evaluation Matrix of Alternatives Based on Criteria")

        # Calculate weighted scores
        weighted_scores = alternatives_df.mul(criteria_weights, axis=1)
        display_matrix(weighted_scores, "Weighted Scores")

        # Calculate utility function values
        utility_values = weighted_scores.sum(axis=1)
        print("\nUtility Function Values:")
        print(utility_values.to_string())

        # Find the best lawyer
        best_lawyer_index = utility_values.idxmax()
        print(f'\nMaximum utility function value: {utility_values[best_lawyer_index]} ({best_lawyer_index})')
        print(f'Therefore, the best choice is {best_lawyer_index}')
        input()

    elif task == 2:
        # -------------- Task 2 --------------
        # Read the data from CSV or Excel
        matrix_file = input("Enter the file path for Task 2 alternatives matrix (CSV or Excel): ")
        weights_file = input("Enter the file path for Task 2 criteria weights (CSV or Excel): ")

        # Load data into pandas DataFrames
        if matrix_file.endswith('.csv'):
            alternatives_df = pd.read_csv(matrix_file,index_col=None,header=None)

        else:
            alternatives_df = pd.read_excel(matrix_file,index_col=None,header=None)

        if weights_file.endswith('.csv'):
            criteria_weights = pd.read_csv(weights_file, index_col=None,header=None).squeeze().values
        else:
            criteria_weights = pd.read_excel(weights_file, index_col=None,header=None).squeeze().values
        print(criteria_weights)
        print(alternatives_df)
        display_matrix(alternatives_df, "Evaluation Matrix of Alternatives Based on Criteria")

        # Criteria (1 - maximize, -1 - minimize)
        criteria = [1, -1, 1, 1, 1]  # This can be read from the user or a file as well

        # Normalize the ratings
        normalized_df = normalize_matrix(alternatives_df, criteria)
        display_matrix(normalized_df, "Normalized Ratings")

        # Calculate weighted scores
        weighted_scores = normalized_df.mul(criteria_weights, axis=1)
        display_matrix(weighted_scores, "Weighted Scores")

        # Calculate utility function values
        utility_values = weighted_scores.sum(axis=1)
        print("\nUtility Function Values:")
        print(utility_values.to_string())

        # Find the best lawyer
        best_lawyer_index = utility_values.idxmax()
        print(f'\nMaximum utility function value: {utility_values[best_lawyer_index]:.5f} ({best_lawyer_index})')
        print(f'Therefore, the best choice is {best_lawyer_index}')
        input()

    else:
        print('Invalid task number!')
        input()
