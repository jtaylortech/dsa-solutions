def firstDuplicateValue(array):
    # set up a dictionary to store the values we've seen
    seen = set()

    # iterate through the array
    # if the current value is in the dictionary, return the current value
    # otherwise, add the current value to the dictionary
    # return -1 if we never find a duplicate
    for idx in array:
        if idx in seen:
            return idx
        seen.add(idx)

    return -1
