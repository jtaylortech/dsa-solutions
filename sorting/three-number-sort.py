def threeNumberSort(array, order):
    # store the first and last value of the order array
    firstValue = order[0]
    thirdValue = order[2]

    # set the first index to 0 because we start at the beginning of the array
    # for loop to iterate through the array and swap the first value with the value at the first index
    # same for the third value
    firstIdx = 0
    for idx in range(len(array)):
        if array[idx] == firstValue:
            array[firstIdx], array[idx] = array[idx], array[firstIdx]
            firstIdx += 1

    # for loop range is -1, -1, -1 because we want to iterate through the array backwards
    thirdIdx = len(array) - 1
    for idx in range(len(array) -1, -1, -1):
        if array[idx] == thirdValue:
            array[thirdIdx], array[idx] = array[idx], array[thirdIdx]
            thirdIdx -= 1

    return array
