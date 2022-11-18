def insertionSort(array):
    # for loop to iterate over the array and sort it
    # while loop to make sure the current element is in the right place by comparing it to the previous element
    # if the current element is smaller than the previous element, swap them
    # while loop parameters: while the current element is smaller than the previous element and the current element is not the first element
    for idx in range(1, len(array)):
        while idx > 0 and array[idx] < array[idx - 1]:
            array[idx - 1], array[idx] = array[idx], array[idx - 1]
            idx -= 1

    return array
