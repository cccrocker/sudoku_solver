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
    # single occurrence in row
    row_occurrences = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    col_occurrences = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    block_occurrences = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for row in range(9) :
        for col in range(9) :
            if type(sudoku[row][col]) == list :
                pass
    # single occurrence in col
    # single occurrence in block
    return sudoku, missing_rows, missing_cols, changes

def find_block(row, col) :
    block = 3 * (row // 3) + (col // 3)
    return block