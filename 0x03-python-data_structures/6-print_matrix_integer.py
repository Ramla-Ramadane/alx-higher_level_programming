#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for row in matrix:
        for col in row:
            if row.index(col) == len(row) - 1:
                print("{:d}".format(col))
            else:
                print("{:d}".format(col), end=" ")
