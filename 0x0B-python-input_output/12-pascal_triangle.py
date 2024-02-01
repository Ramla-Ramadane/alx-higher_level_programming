#!/usr/bin/python3
'''Pascal's Triangle'''


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for idx in range(len(tri) - 1):
            tmp.append(tri[idx] + tri[idx + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
