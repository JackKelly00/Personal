# Sudoku Project
# 1) Board Hard Coded In
# 2) Initial Board Printed
# 3) solve() called
#       If no empty spaces exist, board is complete
#       If find_empty() returns an empty space a num is inserted into that space and checked by
#       the valid() func.
#       If valid, num is entered into space, solve() is called recursively and this continues
#       until the board is full or there is no valid num for a space.
#       In that case, we backtrack to the previous square and set it to 0(empty).
#       The next num in the for is tried, if valid its entered, if not we backtrack again.
# 4) Once full, the solved board is printed.

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    for i in range(len(bo)):  # Gets the height of the board (len(bo) counts how many rows)
        if i % 3 == 0 and i != 0:  # Condition ensures lines are placed after 3rd and 6th row
            print("- - - - - - - - - - - - ")  # Prints when i = 3 and 6

        for j in range(len(bo[0])):  # Gets the length of a row, ie the width of the board
            if j % 3 == 0 and j != 0:  # Condition ensure a line is printed after the 3rd and 6th column
                print(" | ", end="")  # end="" ensures values will be printed on the same line

            if j == 8:
                print(bo[i][j])  # Prints the last digit of the row
            else:
                print(str(bo[i][j]) + " ", end="")  # str(bo[i][j]) converts the element to a string so that it can be
                                                    # with a space after it.


def find_empty(bo):  # Function to find an empty square. 0 denotes empty.
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # Row Column

    return None  # Triggers base case


def valid(bo, num, pos):
    # Check Row
    for i in range(len(bo[0])):                     # Simply gives the length of a row.
        if bo[pos[0]][i] == num and pos[1] != i:    # pos[0] gives us the row to check, [i] I will check each column in
            return False                            # that row. But, "pos[1] != i" ensures that the column with the
                                                    # number we just inserted isn't checked.
    # Check Column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check Box. Using integer div to determine which box we in.
    # E.g empty = 0,3. 0/3 = 0, 3/3 = 1. We in box 0,1
    box_y = pos[0] // 3  # pos[0] is the row of the empty square
    box_x = pos[1] // 3  # pos[1] is the col of the empty square

    for i in range(box_y * 3, box_y * 3 + 3):      # Range is 0-3 so rows 0-2 will be iterated through.
        for j in range(box_x * 3, box_x * 3 + 3):  # Range is 3-6 so columns 3-5 will be iterated through.
            if bo[i][j] == num and bo[i][j] != pos:
                return False  # If bo[i][j] != the num we inserted and were not checking the box we inserted into?

    return True  # False has not been returned so we return true meaning the pos is correct SO FAR


def solve(bo):
    # Base Case of Recursion, meaning once we reach this case, were done
    find = find_empty(bo)
    if not find:
        return True  # If no empty space is returned the board must be complete.
    else:
        row, col = find

    for i in range(1, 10):  # Loop through values 1-9 and attempt to put them in board
        if valid(bo, i, (row, col)):  # Check if adding them to our board is a valid solution
            bo[row][col] = i  # If valid we add to board

            if solve(bo):  # If a num is successfully entered into the board this func is called here(recursion)
                return True  # we then go down a level to another solve(bo)
                            # if the base case is triggered, the solve(bo) here is true and the return true here is
                            # triggered. This means every level will return true and we exit the recursion.

            bo[row][col] = 0  # This clears the previous square

    return False  # If no num is valid, we backtrack to the previous solve(bo)/square. i in the for will be at the
                    # element it was at when we called the solve(bo), meaning we carry on.

# Print Initial Board
print_board(board)
# Call Solve Function
solve(board)
# Space Between Boards
print("_______________________")
print("_______________________")
# Print Solved Board
print_board(board)
