import copy

#yahakovi = 1, zeidal = 2
cycler_type=1
initial_variable=1

def is_diagonally_dominant(matrix):
    for rindex, row in enumerate(matrix):
        rowSum=0
        for cindex, col in enumerate(row):
            if (rindex!=cindex):
                rowSum+=col
        if (rowSum>row[rindex]):
            return False
    return True

def shift_to_diagonally_dominant(matrix):
    return
    #stub

def yahakovi(matrix,sum_vector,variable_vector):
    variable_archive=list(map(lambda x: initial_variable, variable_vector))
    for row in range(len(matrix)):
        curRowSum = - sum_vector[row]
        for col in range(len(matrix[row])):
            curRowSum += matrix[row][col] * variable_archive[col] if row != col else 0
        variable_vector[row] = curRowSum/-matrix[row][row]

def zeidal(matrix,sum_vector,variable_vector):
    for row in range(len(matrix)):
        curRowSum = - sum_vector[row]
        for col in range(len(matrix[row])):
            curRowSum += matrix[row][col] * variable_vector[col] if row != col else 0
        variable_vector[row] = curRowSum/-matrix[row][row]

def cycler(matrix,sum_vector,variable_vector,maxcycle):
    variable_vector=list(map(lambda x: initial_variable, variable_vector))
    for i in range(maxcycle):
        variable_archive=copy.deepcopy(variable_vector)
        if (cycler_type == 1):
            yahakovi(matrix,sum_vector,variable_vector)
        else:
            zeidal(matrix,sum_vector,variable_vector)
        flag=True
        for index in range(len(variable_vector)):
            difference = abs(variable_vector[index] - variable_archive[index])
            flag=flag and difference <= 0.0000001
        if (flag):
            return variable_vector, True
    return [], False

def main():
    print("Welcome to py-zeidal!")
    matrixA=[[2,0,1],[1,5,1],[0,3,10]]#[[4,2,0],[2,10,4],[0,4,5]]
    vectorB=[7,16,56]#[2,6,5]
    vector_variables=[5,5,5]
    print("Choose algorithm type:\n1 - yahakovi\n2 - zeidal\n")
    global cycler_type
    cycler_type = int(input("Enter choice: "))
    if (not is_diagonally_dominant(matrixA)):
        print("Not diagonally dominant")
        #check if matrix can still be solveable despite not being diagnoally dominant
        cycler(matrixA,vectorB,vector_variables,14)
        #check if matrix is solved
        print("Shifting rows to create diagonally dominant")
        shift_to_diagonally_dominant(matrixA)
    print("solving the matrix...")
    print(cycler(matrixA,vectorB,vector_variables,50))

main()
