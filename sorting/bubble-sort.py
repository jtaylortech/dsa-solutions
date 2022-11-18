def bubbleSort(array):
    # sets isSorted to false so that the while loop runs at least once and then checks if the array is sorted
    # sets counter to 0 to keep track of the number of swaps made and then increments it by 1 each time a swap is made
    isSorted = False
    counter = 0

    # while loop runs until the array is sorted
    # sets isSorted to true so that the while loop will stop running if the array is sorted
    # for loop runs through the array and compares each element to the next element and swaps them if the first element is greater than the second element using the swap function
    # if a swap is made, isSorted is set to false so that the while loop will run again
    while not isSorted:
        isSorted = True
        for idx in range(len(array) - 1 - counter):
            if array[idx] > array[idx + 1]:
                swap(idx, idx + 1, array)
                isSorted = False
        counter += 1

    return array


# swap function swaps the elements at the given indices in the given array
def swap(idx, jdx, array):
    array[idx], array[jdx] = array[jdx], array[idx]
