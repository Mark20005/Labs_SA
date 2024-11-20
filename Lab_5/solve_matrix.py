import scipy as sc;
import numpy as np;

def find_optimum(matrix,type):
    matrix=optimize_Matrix(matrix)
    c=np.ones(len(matrix))
    b=np.ones(len(matrix))
    bounds = [(0, None)] * len(matrix)
    if(type=="min"):
        matrix=np.transpose(matrix)
        matrix=-matrix
        b=-b  
    else:
        c=-c
    res=sc.optimize.linprog(c,A_ub=matrix,b_ub=b,bounds=bounds)
    result=1/res.fun*res.x
    return(-result if(type=="max") else result)

def optimize_rows(matrix):
    rows, cols = matrix.shape
    comparisons = []
    for i in range(rows - 1):
        for j in range(i + 1, rows):
            if(np.all( matrix[i,:] >=  matrix[j,:])):
                comparisons.append(j)
    return np.delete(matrix,comparisons,0)    

def optimize_cols(matrix):
    rows, cols = matrix.shape
    comparisons = []
    for i in range(cols - 1):
        for j in range(i + 1, cols):
           if (np.all(matrix[:, i] >= matrix[:, j])):
            comparisons.append(j)    
    return np.delete(matrix,comparisons,1)    

def optimize_Matrix(matrix):
    matrix=optimize_rows(matrix)
    matrix=optimize_cols(matrix)
    return matrix
def get_upper_bound(matrix):
    return np.min(np.max(matrix, axis=0))
def get_lower_bound(matrix):
    return np.max(np.min(matrix, axis=1)) 
def check_clear_strategies(matrix):
    return get_upper_bound(matrix)==get_lower_bound(matrix)

  


