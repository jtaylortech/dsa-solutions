def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0

    # traverse through both arrays to look for subsequent matches
        # use the while loop to check if the array pointer is less than the length of the array
    # if the two values match, we will increment both pointers
    # otherwise, we will only increment the array pointer
    # if the sequence pointer reaches the end of the sequence array, we will return true
    # otherwise, we will return false
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    
    # can only be true if the entirety of the sequence array is in the array which is why this return method works
    return seqIdx == len(sequence)

    
    