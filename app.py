def sudoku_solve(sudoku) :
    sudoku, solved, missing_rows, missing_cols = check(sudoku, init = 1)
    message = "Success!"
    while not solved :
        print("Iterating...")

        sudoku, missing_rows, missing_cols, changes = solve(sudoku, missing_rows, missing_cols)

        if changes == 0:
            message = "Failed with " + str(len(missing_rows) + 1) + " cells left"
            break

        sudoku, solved, missing_rows, missing_cols = check(sudoku)
    
    print(message)
    for val in sudoku :
        print(val)
    # print(solved)
    # print(missing_rows)
    # print(missing_cols)
    return sudoku

def check(sudoku, init = 0) :
    print("Checking...")
    missing_rows = []
    missing_cols = []
    for i in range(9):
        for j in range(9):
            cell_solved = (type(sudoku[i][j]) == int)
            if cell_solved == False :
                solved = False
                missing_rows.append(i)
                missing_cols.append(j)
                if init == 1 :
                    sudoku[i][j] = list(range(1, 10))

    return sudoku, solved, missing_rows, missing_cols

def solve(sudoku, missing_rows, missing_cols) :
    print("Solving...")
    changes = 0
    if len(missing_rows) != len(missing_cols) :
        print("Error with length of missing cells")
        return sudoku, missing_rows, missing_cols

    for cell in range(len(missing_rows)) :
        row = missing_rows[cell]
        col = missing_cols[cell]
        fixed_cells = []
        
        for alt in range(9) :
            vals = sudoku[row][col]
            row_alt = sudoku[alt][col] if row != alt else 0
            col_alt = sudoku[row][alt] if col != alt else 0

            if row_alt in vals:
                sudoku[row][col].remove(row_alt)
                changes = 1
            if col_alt in vals :
                sudoku[row][col].remove(col_alt)
                changes = 1
        
        if len(vals) == 1 :
            sudoku[row][col] = vals[0]
            missing_rows[cell] = None
            missing_cols[cell] = None
            changes = 1
            
    return sudoku, missing_rows, missing_cols, changes