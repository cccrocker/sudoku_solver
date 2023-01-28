def sudoku_solve(sudoku) :
    # Find the empty cells in the sudoku, and assign them with a list of possible values 1-9
    sudoku, solved, missing_rows, missing_cols = find_missing(sudoku, init = 1)
    # Assign default message
    message = "Success!"
    # If there are still empty cells...
    while not solved :
        # Notify user of iteration
        print("Iterating...")

        # Each step starts counting how many changes it's made
        changes = 0
        # Remove possible values based on filled values in the same row, column, and block
        sudoku, missing_rows, missing_cols, changes = simplify(sudoku, missing_rows, missing_cols, changes)
        # Fill cell if a number could only exist in that cell in its row, column, or block
        sudoku, missing_rows, missing_cols, changes = single_occurrence(sudoku, missing_rows, missing_cols, changes)

        # If no changes have been recorded, then the program has failed
        if changes == 0:
            # Assign failed message
            message = "Failed with " + str(len(missing_rows) + 1) + " cells left"
            break

        # Re-check for cells without a value
        sudoku, solved, missing_rows, missing_cols = find_missing(sudoku)
    
    # The program has finished, let the user know what was found
    print(message)
    for val in sudoku :
        print(val)

    return sudoku

# Fill empty cells with a list of 1-9, and grab a list of cells that haven't been solved
def find_missing(sudoku, init = 0) :
    # Notify user what we're doing
    print("Finding missing cells...")
    # Initialize the list of missing cells
    missing_rows = []
    missing_cols = []
    # Assign default state of puzzle
    solved = True
    # Iterate thru each cell
    for i in range(9):
        for j in range(9):
            # Determine if a cell is solved (is an integer) or not (either None or a list)
            cell_solved = (type(sudoku[i][j]) == int)
            if cell_solved == False :
                # Change state of puzzle
                solved = False
                # Append the unsolved cells row and col
                missing_rows.append(i)
                missing_cols.append(j)
                # If this is the first run (and the cell is None), assign it a list with numbers 1-9 as possible solutions
                if init == 1 :
                    sudoku[i][j] = list(range(1, 10))

    return sudoku, solved, missing_rows, missing_cols

# Remove possible solutions from a cell based on other values in its row, col, and block
def simplify(sudoku, missing_rows, missing_cols, changes) :
    # Notify user what we're doing
    print("Simplifying cell options...")
    # Check for weird errors
    if len(missing_rows) != len(missing_cols) :
        print("Error with length of missing cells")
        return sudoku, missing_rows, missing_cols
    
    # Iterate thru unsolved cells
    for cell in range(len(missing_rows)) :
        # Get row and col for unsolved cells
        row = missing_rows[cell]
        col = missing_cols[cell]
        # Get first row and col for the block
        block_row = 3 * (row // 3)
        block_col = 3 * (col // 3)
        
        # Iterate thru all 9 cells in the same row, col, and block
        for alt in range(9) :
            # Get the list of possible values in the cell
            vals = sudoku[row][col]
            # Figure out how the block will get iterated thru
            block_row_alt = block_row + (alt // 3)
            block_col_alt = block_col + (alt % 3)
            # Check other cells in the same row, col, and block
            row_alt = sudoku[alt][col] if row != alt else 0
            col_alt = sudoku[row][alt] if col != alt else 0
            block_alt = sudoku[block_row_alt][block_col_alt] if ((block_row_alt != row) & (block_col_alt != col)) else 0

            # If the unsolved cell still has a value that fills another cell in the same row, col, or block: remove it.
            if row_alt in vals:
                sudoku[row][col].remove(row_alt)
                changes = 1
            if col_alt in vals :
                sudoku[row][col].remove(col_alt)
                changes = 1
            if block_alt in vals :
                sudoku[row][col].remove(block_alt)
                changes = 1
        
        # If there is only 1 option left for the cell, assign it to the cell
        if len(vals) == 1 :
            sudoku[row][col] = vals[0]
            missing_rows[cell] = None
            missing_cols[cell] = None
            changes = 1
            
    return sudoku, missing_rows, missing_cols, changes

# TODO: Check each row, col, and block for a value option that only shows up once
def single_occurrence(sudoku, missing_rows, missing_cols, changes) :
    # start a count of occurrences, create list with indexes 0-9, and ignore the 0
    row_occurrences = [0 for _ in range(10)]
    col_occurrences = [0 for _ in range(10)]
    block_occurrences = [0 for _ in range(10)]
    # iterate thru all 9 rows, cols, and blocks once
    for row in range(9) :
        col = row // 3 + 3 * (row % 3) # row_col = 0_0, 1_3, 2_6, 3_1, 4_4, 5_7, 6_2, 7_5, 8_8
        # Get first row and col for the block
        block_row = 3 * (row // 3)
        block_col = 3 * (col // 3)
        # iterate thru cells in the row, col, and block
        for cell in range(9) :
            # Get the list of possible values in the cell
            vals = sudoku[row][col]
            # Figure out how the block will get iterated thru
            block_cell_row = block_row + (cell // 3)
            block_cell_col = block_col + (cell % 3)
            # Check other cells in the same row, col, and block
            row_opt = sudoku[cell][col] if type(sudoku[cell][col]) == list else []
            col_opt = sudoku[row][cell] if type(sudoku[row][cell]) == list else []
            block_opt = sudoku[block_cell_row][block_cell_col] if type(sudoku[block_cell_row][block_cell_col]) == list else []

            # TODO: Iterate thru the row/col/block_opt and increment the row/col/block_occurrences lists accordingly
            for val in row_opt:
                row_occurrences[val] += 1
            for val in col_opt:
                col_occurrences[val] += 1
            for val in block_opt:
                block_occurrences[val] += 1


    return sudoku, missing_rows, missing_cols, changes

def find_block(row, col) :
    block = 3 * (row // 3) + (col // 3)
    return block