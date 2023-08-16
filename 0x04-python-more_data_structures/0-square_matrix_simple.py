#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_list(row):
        new_list = []
        for i in row:
            new_list.append(i**2)
        return new_list
    new_matrix = list(map(square_list, matrix))
    return new_matrix
