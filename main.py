# Pull in JSON with the sudoku numbers, where the cells are listed by row {{r1c1, r1c2, ...}{r2c1, r2c2, ...}...} and create solution-in-progress (SIP)

# initialize number masks (these are recreations of the Sudoku through the lens of a single number)
masks = []
for mask in range(9):
  for row in range(9):
    for col in range(9):
      block = 3*(row//3) + col
      # create masks

# update the masks and sip
def update(row, col, num):
  block = 3*(row//3) + col
  
  # update sip
  if sip[row][col] == '':
    sip[row][col] = num
  else:
    print("Error")
    break
  
  # update masks
  for section in ["row", "col", "block"]:
    print("updating " + section)
    for i in range(9):
      if section == "row" and i = row:
        continue
      if section == "col" and i = col:
        continue
      if section == "block" and i # need to continue this logic
