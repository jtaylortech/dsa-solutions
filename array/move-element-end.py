def moveElementToEnd(array, toMove):
    # establish two pointers, one at the beginning and one at the end
    h = 0
    k = len(array) - 1

    # will run until h pointer passes k pointer
    while h < k:
        #double while loop because swaps will need to constantly occur
        while h < k and array[k] == toMove: 
            k -= 1
        if array[h] == toMove:
            array[h], array[k] = array[k], array[h] #completes the swap
        h += 1
    
    return array