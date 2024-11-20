import numpy as np
from solve_matrix import find_optimum,check_clear_strategies,get_lower_bound,get_upper_bound

def main():
    matrix=np.loadtxt("lab5_task1.csv",
                      delimiter=";")

    if (check_clear_strategies(matrix)):
        print("There is solution in clear strategies",)
    else:
        print("No solution in clear strategies",get_lower_bound(matrix),"!=",get_upper_bound(matrix))
        print("Best solution for 1st player",find_optimum(matrix,"min"))
        print("Best solution for 2st player",find_optimum(matrix,"max"))

if __name__ == "__main__":
    main()