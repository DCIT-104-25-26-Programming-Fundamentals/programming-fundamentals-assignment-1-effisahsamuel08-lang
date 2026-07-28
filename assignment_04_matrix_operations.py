# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def print_matrix(matrix):
    """Helper function to display a matrix in a neat, aligned grid format."""
    for row in matrix:
        # Formats each number to take at least 3 spaces for alignment
        print(" ".join(f"{val:>3}" for val in row))
    print()


def read_matrix(rows, cols, matrix_name="matrix"):
    """Helper function to read a matrix of size rows x cols from user input."""
    matrix = []
    for i in range(rows):
        while True:
            try:
                line = input(f"Enter row {i + 1}: ")
                row = [int(x) for x in line.split()]
                if len(row) != cols:
                    print(f"Error: You must enter exactly {cols} values.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid integers separated by spaces.")
    return matrix


# ==========================================
# PART A - Transpose a Matrix
# ==========================================
def transpose_matrix(matrix):
    """ Computes and returns the transpose of an M x N matrix."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Create an empty N x M result matrix filled with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Use nested loops to swap rows and columns
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed


# ==========================================
# PART B - Add Two Matrices
# ==========================================
def add_matrices(matrix_A, matrix_B):
    """ Computes and returns the element-wise sum of two M x N matrices."""
    rows = len(matrix_A)
    cols = len(matrix_A[0])
    
    # Create an empty M x N result matrix filled with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Use nested loops to add elements position-by-position
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_A[i][j] + matrix_B[i][j]
            
    return result


# ==========================================
# PART C - Multiply Two Matrices
# ==========================================
def multiply_matrices(matrix_A, matrix_B):
    """Computes and returns the product of an M x N and an N x P matrix."""
    rows_A = len(matrix_A)
    cols_A = len(matrix_A[0])
    rows_B = len(matrix_B)
    cols_B = len(matrix_B[0])
    
    # Create an empty M x P result matrix filled with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Use nested loops to calculate dot products
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # Or range(rows_B) since cols_A == rows_B
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
                
    return result


# ==========================================
# Main Execution / Demonstration
# ==========================================
def main():
    print("--- PART A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("\nEnter elements for the matrix:")
    matrix_A = read_matrix(rows, cols)
    
    print("\nOriginal Matrix:")
    print_matrix(matrix_A)
    
    transposed = transpose_matrix(matrix_A)
    print("Transposed Matrix:")
    print_matrix(transposed)
    
    
    print("--- PART B: Add Two Matrices ---")
    print(f"Enter a second {rows}x{cols} matrix to add to the first one:")
    matrix_B = read_matrix(rows, cols)
    
    print("\nMatrix B:")
    print_matrix(matrix_B)
    
    sum_matrix = add_matrices(matrix_A, matrix_B)
    print("Result of Matrix Addition (A + B):")
    print_matrix(sum_matrix)
    
    
    print("--- PART C: Multiply Two Matrices ---")
    print(f"Matrix A is of size {rows}x{cols}.")
    print(f"Matrix B for multiplication must have {cols} rows.")
    cols_C = int(input("Enter number of columns for Matrix B: "))
    
    print(f"\nEnter elements for a {cols}x{cols_C} Matrix B:")
    matrix_C = read_matrix(cols, cols_C)
    
    print("\nMatrix A:")
    print_matrix(matrix_A)
    print("Matrix B:")
    print_matrix(matrix_C)
    
    product_matrix = multiply_matrices(matrix_A, matrix_C)
    print(f"Result of Matrix Multiplication (A * B) of size {rows}x{cols_C}:")
    print_matrix(product_matrix)


if __name__ == "__main__":
    main()

