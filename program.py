#yahakovi = 1, zeidal = 2
cycler_type=1

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
    return
    #stub

def zeidal(matrix,sum_vector,variable_vector):
    return
    #stub

def cycler(matrix,sum_vector,variable_vector,cycle,maxcycle):
    return
    #stub

def main():
    print("Welcome to py-zeidal!")
    matrixA=[[4,2,0],[2,10,4],[0,4,5]]
    vectorB=[2,6,5]
    vector_variables=[1,1,1]
    print("Choose algorithm type:\n1 - yahakovi\n2 - zeidal\n")
    cycler_type=int(input("Enter choice: "))
    if (is_diagonally_dominant(matrixA)):
        print("Not diagonally dominant")
        #check if matrix can still be solveable despite not being diagnoally dominant
        cycler(matrixA,vectorB,vector_variables,0,14)
        #check if matrix is solved
        print("Shifting rows to create diagonally dominant")
        shift_to_diagonally_dominant(matrixA)
    print("solving the matrix...")
    cycler(matrixA,vectorB,vector_variables,0,50)

main()
