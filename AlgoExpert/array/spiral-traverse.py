def spiralTraverse(array):
    # creates an array to store the values of the array
    # starts at the top left corner of the array and goes right
    # then goes down, then goes left, then goes up
    # then goes right, then goes down, then goes left, then goes up
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    # while loop to iterate through the array and append the values to the result array
    # for each iteration, we change the start and end row and column
    while startRow <= endRow and startCol <= endCol:
        # traverses from left to right the top row of the array and appends the values to the result array
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # traverses from top to bottom the right column of the array and appends the values to the result array
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # traverses from right to left the bottom row of the array and appends the values to the result array
        # we need to check if the startRow is equal to the endRow because if it is, we have already traversed the row
        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # traverses from bottom to top the left column of the array and appends the values to the result array
        # we need to check if the startCol is equal to the endCol because if it is, we have already traversed the column
        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        # increments the startRow and startCol and decrements the endRow and endCol to push the bounds inwards and breaks out of the while loop
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1


    return result