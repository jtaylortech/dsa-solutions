def sortedSquaredArray(array):
    # initializes an empty array
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        # iterates through array and with the variable "value"
        # squares the values and stores them in sortedSquares
        value = array[idx]
        sortedSquares[idx] = value * value
        
    # squaring the values in the array can make them come out of order so i'm sorting them again
    sortedSquares.sort()
    return sortedSquares



    # array = [-2, -4, 3, 5]
    # sortedSquares = []
    # value = -2**-2, -4**-4, 3**3, 5**5
    # sortedSquares = [-4, 16, 9, 25]
    # sortedSquares.sort()

