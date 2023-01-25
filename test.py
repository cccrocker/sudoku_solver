import app

template = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [7, 5, 4, 8, 3, 9, 6, 2, 1],
    [8, 6, 9, 1, 2, 7, 4, 3, 5],
    [9, 3, 7, 5, 1, 8, 2, 6, 4],
    [2, 8, 5, 7, 6, 4, 1, 9, 3],
    [6, 4, 1, 3, 9, 2, 8, 5, 7],
    [5, 7, 8, 6, 4, 3, 9, 1, 2],
    [3, 9, 6, 2, 7, 1, 5, 4, 8],
    [4, 1, 2, 9, 8, 5, 3, 7, 6]
]

test = [
    [1, 2, 3, 4, 5, 6, None, None, None],
    [None, None, None, None, 3, 9, None, None, 1],
    [8, 6, None, None, None, None, None, 3, None],
    [None, None, None, None, None, 8, None, 6, None],
    [None, None, 5, None, None, None, 1, None, None],
    [None, 4, None, 3, None, None, None, None, None],
    [None, 7, None, None, None, None, None, 1, 2],
    [3, None, None, 2, 7, None, None, None, None],
    [None, None, None, 9, 8, 5, 3, 7, 6]
]

# print(test)

app.sudoku_solve(test)