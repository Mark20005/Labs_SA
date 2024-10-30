import numpy as np
def chooseMethod(choice, matrix):
    '''
    Calls method to solve problem accoding to the choice
    Parameters
    choice - choice
    matrix - input matrix
    Return - 0 to exit the loop
    '''
    match choice:
        case "1":Laplace(matrix)
        case "2":Wald(matrix)
        case "3":Savage(matrix)  
        case "4":Hurwitz(matrix)   
        case "5":Bayes(matrix)       
        case "6":Lehmann(matrix)   
        case "0":return 0
def printText():
    '''
    Prints text menu for user
    '''
    print("0. - Exit")
    print("1. - Laplas")
    print("2. - Vald")
    print("3. - Savidge")
    print("4. - Gurvits")
    print("5. - Baies-Laplas")
    print("6. - Hodge-Leman")
def readFile(path):
    '''
    Reads the matrix from file and multiplies by weights if necessary 
    Parameters
    path - string that represents name of the file
    Return 
    matrix that was read from file
    '''
    matrix = np.loadtxt(path,
                 delimiter=";")
    print(matrix)
    return matrix

def printMaxResult(vector):
    '''
    Prints vector, its maximum value and its index
    Parameters
    vector - array
    '''
    print("Vector",vector,"Best alternative at",np.argmax(vector)+1,"with value",np.max(vector))
def Laplace(matrix):
    '''
    Solves the problem with Laplas criteria
    Parameters
    matrix - matrix of values
    '''
    multiplyer=1/np.shape(matrix)[1]
    row_sums = multiplyer*np.sum(matrix, axis=1)
    print(row_sums)
    printMaxResult(row_sums)

def Wald(matrix):
    '''
    Solves the problem with Wald criteria
    Parameters
    matrix - matrix of values
    '''
    vector = (np.min(matrix,axis=1))
    printMaxResult(vector)

def Savage(matrix):
   '''
    Solves the problem with Savage criteria
    Parameters
    matrix - matrix of values
   '''
   maxArr = np.max(matrix, axis=0)
   payMatrix = -matrix + maxArr
   print(payMatrix)
   vector=np.max(payMatrix,axis=1)
   print("Vector",vector,"Best alternative at",np.argmin(vector),"with value",np.min(vector))

def Hurwitz(matrix):
    '''
    Solves the problem with Hurwitz criteria
    Parameters
    matrix - matrix of values
    '''
    l=float(input("Enter lambda "))
    vector=(l*np.min(matrix,axis=1)+(1-l)*np.max(matrix,axis=1))
    printMaxResult(vector)

def Bayes(matrix):
    '''
    Solves the problem with Bayes criteria
    Parameters
    matrix - matrix of values
    '''
    coeffs=np.fromstring(input("Enter coefficients "),sep=" ")
    result_multiply = np.sum(matrix[:] * coeffs, axis=1)
    printMaxResult(result_multiply)

def Lehmann(matrix):
    '''
    Solves the problem with Khodg-Lehmann criteria
    Parameters
    matrix - matrix of values
    '''
    coeffs=np.fromstring(input("Enter coefficients "),sep=" ")
    l=float(input("enter lambda "))
    result_multiply = (1-l)*np.min(matrix,axis=1)+l*np.sum(matrix * coeffs, axis=1)
    print(result_multiply)
    printMaxResult(result_multiply)

def main():
    '''
    main method of the program
    '''
    match (input("Choose task 1/2:  ")):
        case "1":
            matrix = readFile("Lab_4/lab4/data/lab4(1).csv")
        case "2":
            matrix = readFile("Lab_4/lab4/data/lab4(2).csv")
    printText()
    choice=input()
    while(True):
        if(chooseMethod(choice,matrix)==0):
            break
        choice=input()

if __name__ == "__main__":
    main()