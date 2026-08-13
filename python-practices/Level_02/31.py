# 31. Matrix Calculator
# Input two matrices.
# Perform
#     • Addition
#     • Subtraction
#     • Multiplication
#     • Transpose
# Practice
#     • NumPy arrays
#     • matrix operations
# --------------------------

import numpy as np

def create_matrix():
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))

    matrix = []

    for i in range(rows):
        row = []

        for j in range(cols):
            value = int(input(f"Value [{i}][{j}]: "))
            row.append(value)

        matrix.append(row)

    return np.array(matrix)

def add_matrix(A, B):
    return A + B

def subtract_matrix(A, B):
    return A - B

def multiply_matrix(A, B):
    return np.matmul(A,B)

def transpose_matrix(A):
    return A.T

print("Matrix A")
A = create_matrix()

print("Matrix B")
B = create_matrix()

while True:
    print("\n--- Matrix Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose Matrix A")
    print("5. Exit")

    choice = int(input("Choose your option: "))

    if choice == 1:
        print("\nAddition:")
        print(add_matrix(A, B))

    elif choice == 2:
        print("\nSubtraction:")
        print(subtract_matrix(A, B))

    elif choice == 3:
        print("\nMultiplication:")
        print(multiply_matrix(A, B))

    elif choice == 4:
        print("\nTranspose of Matrix A:")
        print(transpose_matrix(A))

    elif choice == 5:
        print("Bye!")
        break

    else:
        print("Invalid choice.")              

