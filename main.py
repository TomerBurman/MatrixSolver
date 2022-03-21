def exchange(matrix, row, row2):
    """
    Exchanges two rows in the matrix and returns new e_matrix to multiply the original in
    :param matrix: matrix in form of (A|b)
    :param row: pointer to row
    :param row2: pointer to row
    :return: e_matrix that changes the lines
    """
    e_matrix = i_matrix_gen(*find_matrix_size(matrix))  # generating an e matrix.
    e_matrix[row][row], e_matrix[row2][row2], e_matrix[row][row2], e_matrix[row2][row] = 0, 0, 1, 1
    return e_matrix


def i_matrix_gen(e_height, e_width):
    """
    Generates I matrix
    :param e_width: Matrix columns
    :param e_height: Matrix height
    :return: I Matrix
    """
    i = 0
    e_width -= 1  # Remove the rightmost column (    | ) <----

    I = [[0 for i in range(e_width)] for j in range(e_height)]
    while i < e_width and i < e_height:
        I[i][i] = 1
        i += 1
    return I


def mul_matrix(mat_a, mat_b):
    """
    Multiplies two given matrices ( Prints the matrices before the multiplication and after the multiplication )
    https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
    mat_a X mat_b
    :param mat_a: Matrix A
    :param mat_b: Matrix B
    :return: Multiplied Matrix /False if can't be multiplied
    -----------------------------------------------------------
            A                     B
    [   1   2   3   ]       [   7   8   ]       [   58   64  ]
    [   4   5   6   ]   X   [   9   10  ]   =   [   139  154 ]
                            [   11  12  ]
    ----------------------------------------------------------
    """
    height_a, width_a = find_matrix_size(mat_a)
    height_b, width_b = find_matrix_size(mat_b)

    # Print the matrices before the multiplication
    print_matrix(mat_a, "\tMatrix A:")
    print_matrix(mat_b, "\tMatrix B:")

    if width_a != height_b:  # check if the matrix can be multiplied.
        return False
    else:
        new_matrix = [[0 for i in range(width_b)] for j in range(height_a)]
        for i in range(height_a):
            for j in range(width_b):
                for k in range(height_b):
                    new_matrix[i][j] += mat_a[i][k] * mat_b[k][j]
        print_matrix(new_matrix, "\tSolved Matrix (A x B):")  # Print the matrix after the multiplication
        return new_matrix


def find_matrix_size(mat):
    """
    Finds the matrix size
      -------M------
    | (           )
    N (           )
    | (           )
    :param mat: Given matrix
    :return: Size of the matrix in width, height
    """
    return len(mat), len(mat[0])  # n , m


def print_matrix(mat, message=None):
    """
    Prints the matrix
    :param mat: The matrix
    :return: None
    """
    if message:
        print(f'\n{message}')
    height, width = find_matrix_size(mat)
    for i in range(height):
        print('[', end='')
        for j in range(width):
            if j + 1 == width:
                print(f'{mat[i][j]}', end=']\n')
            else:
                print(f'{mat[i][j]}', end=", ")


def matrix_solver(matrix):
    n, m = find_matrix_size(matrix)
    if m != n + 1:  # if matrix is not square. extra column is for solution vector
        return None
    e_matrix = i_matrix_gen(n, m)  # Elementary matrix keeper which will be I at the end.
    for row in range(n):  # for every row in rows
        #   RUNTIME: O(n)
        pivot = matrix[row][row]  # taking pivot
        column = row  # taking column that being worked on
        if pivot == 0:  # in case pivot is 0
            found_pivot = False  # if we found the pivot flag
            for row2 in range(row + 1, n):  # searching for line with pivot not 0 from current line to last
                #   RUNTIME: O(n)
                pivot = matrix[row2][column]  # taking pivot
                if pivot != 0:  # if pivot found break
                    found_pivot = True
                    e_matrix = exchange(matrix, row,
                                        row2)  # function that changes lines of row and c_row in 2dim matrix.
                    matrix = mul_matrix(e_matrix, matrix)  # lines changed.
                    print("=====================================")
                    break
            if not found_pivot:  # if pivot not found
                print("The matrix has unlimited number of solutions")
                return None  # Matrix has no answer
        e_matrix = i_matrix_gen(n, m)
        e_matrix[row][row] *= 1 / pivot  # elementry matrix is now 1 / pivot to set pivot to 1 when multiplied.

        matrix = mul_matrix(e_matrix, matrix)  # setting pivot to 1
        print("=====================================")
        # Setting every element after pivot to 0 in the same column
        for row2 in range(row + 1, n):
            #   RUNTIME: O(n)
            e_matrix = i_matrix_gen(n, m)
            e_matrix[row2][column] = -matrix[row2][column]

            matrix = mul_matrix(e_matrix, matrix)
            print("=====================================")
    # Till here we should have upper triangular matrix with pivots equal to 1
    for row in range(n - 1, -1, -1):
        #   RUNTIME: O(n)
        pivot = matrix[row][row]  # taking pivot
        column = row  # taking column that being worked on
        # Setting every element before pivot to 0 in the same column
        for row2 in range(row - 1, -1, -1):
            #   RUNTIME: O(n)
            e_matrix = i_matrix_gen(n, m)
            e_matrix[row2][column] = -matrix[row2][column]

            matrix = mul_matrix(e_matrix, matrix)
            print("=====================================")

    # TOTAL RUNTIME: O( n*(n+n) + n*n ) = O(2n^2) = O(n^2)
    # At this point we should have I matrix with the solutions

    # Save the solutions to an array and return them
    sol = []
    for i in range(n):
        sol.append(matrix[i][m - 1])
    return sol


def rearange_max_pivots(mat):
    """
    Rearange the pivots in the matrix so that the pivots will be the max in the column ( in absolute value )
    :param mat: The matrix that we want to change
    :return: new matrix with the changed rows
    """
    n, m = find_matrix_size(mat)
    for col in range(m - 1):
        pivot = mat[col][col]
        max_index = col
        for row in range(col, n):  # Find max pivot in current column
            if mat[row][col] > pivot:
                pivot = mat[row][col]
                max_index = row
        if pivot != mat[col][col]:
            e_mat = exchange(mat, col, max_index)
            mat = mul_matrix(e_mat, mat)
    return mat

mat = rearange_max_pivots([[0.457, 0.330, 0.127],[0.913, 0.659, 0.254]])
print("==================REARANGED THE MATRIX=====================")
print("==================STARTING THE SOLUTION====================")
sol = matrix_solver(mat)
print('The solution is: ', end='')
for i in range(len(sol)):
    print(f'X{i} : {sol[i]}, ', end=' ')
