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


def i_matrix_gen(e_width, e_height):
    """
    Generates I matrix
    :param e_width: Matrix columns
    :param e_height: Matrix height
    :return: I Matrix
    """
    i = 0
    e_height -= 1  # Remove the rightmost column (    | ) <----

    I = [[0 for i in range(e_width)] for j in range(e_height)]
    while i < e_width and i < e_height:
        I[i][i] = 1
        i += 1
    return I


def mul_matrix(mat_a, mat_b):
    """
    Multiplies two given matrixes
    https://www.geeksforgeeks.org/python-program-multiply-two-matrices/
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
    width_a, height_a = find_matrix_size(mat_a)
    width_b, height_b = find_matrix_size(mat_b)

    if width_a != height_b:  # check if the matrix can be multiplied.
        return False
    else:
        new_matrix = [[0 for i in range(width_b)] for j in range(height_a)]
        for i in range(height_a):
            for j in range(width_b):
                for k in range(height_b):
                    new_matrix[i][j] += mat_a[i][k] * mat_b[k][j]
        return new_matrix


def find_matrix_size(mat):
    """
    Finds the matrix size
    :param mat: Given matrix
    :return: Size of the matrix in width, height
    """
    return len(mat[0]), len(mat)


def print_matrix(mat):
    """
    Prints the matrix
    :param mat: The matrix
    :return: None

    """
    width, height = find_matrix_size(mat)
    print("Elementary matrix") if width == height else print("A:")
    for i in range(height):
        if width == height:
            print(mat[i])
        else:
            print(f'{mat[i][:-1]} | {mat[i][-1]}')


def matrixSolver(matrix):
    m, n = find_matrix_size(matrix)
    if m != n + 1:  # if matrix is not square. extra column is for solution vector
        return None
    e_matrix = i_matrix_gen(n, m)  # Elementary matrix keeper which will be I at the end.
    for row in range(n):  # for every row in rows
        pivot = matrix[row][row]  # taking pivot
        column = row  # taking column that being worked on
        if pivot == 0:  # in case pivot is 0
            found_pivot = False  # if we found the pivot flag
            for row2 in range(row + 1, n):  # searching for line with pivot not 0 from current line to last
                pivot = matrix[row2][column]  # taking pivot
                if pivot != 0:  # if pivot found break
                    found_pivot = True
                    e_matrix = exchange(matrix, row,
                                        row2)  # function that changes lines of row and c_row in 2dim matrix.
                    print_matrix(e_matrix)
                    print_matrix(matrix)
                    matrix = mul_matrix(e_matrix, matrix)  # lines changed.
                    print_matrix(matrix)
                    print("=====================================")
                    break
            if found_pivot == False:  # if pivot not found
                return None  # Matrix has no answer
        e_matrix = i_matrix_gen(n, m)
        e_matrix[row][row] *= 1 / pivot  # elementary matrix is now 1 / pivot to set pivot to 1 when multiplied.
        # From here we assume that the pivot is in the right place and it is equal to 1

        print_matrix(e_matrix)
        print_matrix(matrix)
        matrix = mul_matrix(e_matrix, matrix)  # setting pivot to 1
        print_matrix(matrix)
        print("=====================================")
        # Setting every element after pivot to 0 in the same column
        for row2 in range(row + 1, n):
            e_matrix = i_matrix_gen(n, m)
            e_matrix[row2][column] = -matrix[row2][column]

            print_matrix(e_matrix)
            print_matrix(matrix)
            matrix = mul_matrix(e_matrix, matrix)
            print_matrix(matrix)
            print("=====================================")

        # from this point we have an upper Triangular matrix
    column = n - 1
    while column > 0:
        row = column - 1
        while row >= 0:
            e_matrix = i_matrix_gen(n, m)
            e_matrix[row][column] = -matrix[row][column]
            print_matrix(e_matrix)
            print_matrix(matrix)
            matrix = mul_matrix(e_matrix, matrix)
            print_matrix(matrix)
            print("=====================================")
            row -= 1
        column -= 1


matrixSolver([[0.913, 0.659, 0.255], [0.457, 0.330, 0.126]])
