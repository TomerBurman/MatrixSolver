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
    Multiplies two given matrices ( Prints the matrices before the multiplication and after the multiplication )
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

    # Print the matrices before the multiplication
    print_matrix(mat_a)
    print_matrix(mat_b)

    if width_a != height_b:  # check if the matrix can be multiplied.
        return False
    else:
        new_matrix = [[0 for i in range(width_b)] for j in range(height_a)]
        for i in range(height_a):
            for j in range(width_b):
                for k in range(height_b):
                    new_matrix[i][j] += mat_a[i][k] * mat_b[k][j]
        print_matrix(new_matrix)  # Print the matrix after the multiplication
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
    for i in range(height):
        print(mat[i])


def matrix_solver(matrix):
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
            e_matrix = i_matrix_gen(n, m)
            e_matrix[row2][column] = -matrix[row2][column]

            matrix = mul_matrix(e_matrix, matrix)
            print("=====================================")
    # Till here we should have upper triangular matrix with pivots equal to 1
    for row in range(n - 1, -1, -1):
        pivot = matrix[row][row]  # taking pivot
        column = row  # taking column that being worked on
        # Setting every element before pivot to 0 in the same column
        for row2 in range(row - 1, -1, -1):
            e_matrix = i_matrix_gen(n, m)
            e_matrix[row2][column] = -matrix[row2][column]

            matrix = mul_matrix(e_matrix, matrix)
            print("=====================================")

    # At this point we should have I matrix with the solutions

    # Save the solutions to an array and return them
    sol = []
    for i in range(n):
        sol.append(matrix[i][m - 1])
    return sol


sol = matrix_solver([[1, 1, -2, 7], [2, -1, 1, 0], [1, 1, -1, 6]])
print(f'The solution is: {sol}')
