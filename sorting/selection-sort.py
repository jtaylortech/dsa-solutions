def selectionSort(array):
    # set current index to 0 because we start at the beginning of the array
    # while loop will continue until we reach the end of the array
    # set smallest index to current index because we assume the current index is the smallest
    # for loop will continue until we reach the end of the array
    # if the value at the current index is greater than the value at the smallest index then we set the smallest index to the current index
    # after the for loop we swap the value at the current index with the value at the smallest index
    # increment the current index by 1 and repeat the process
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for idx in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[idx]:
                smallestIdx = idx
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array


def swap (idx, jdx, array):
    array[idx], array[jdx] = array[jdx], array[idx]