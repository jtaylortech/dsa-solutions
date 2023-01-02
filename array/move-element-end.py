# O(n) time | O(1) space - where n is the length of the input array
# this is the time complexity because we are using a while loop to iterate through the array once
# this is the space complexity because we are not creating any new data structures
def moveElementToEnd(array, toMove):
    # establish two pointers, one at the beginning and one at the end
    h = 0
    k = len(array) - 1

    # will run until h pointer passes k pointer
    # will use the if statement to check if the value at the h pointer is equal to the value we want to move
    # if it is, use the while loop to check if the value at the k pointer is equal to the value we want to move
    # if it is, we will decrement the k pointer
    # otherwise, we will swap the values at the h and k pointers
    # also increment the h pointer
    while h < k:
        while h < k and array[k] == toMove: 
            k -= 1
        if array[h] == toMove:
            array[h], array[k] = array[k], array[h]
    
    return array