def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0

    # traverse through both arrays to look for subsequent matches
    # if statement to iterate through the arrays only moving forward if the two values match
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    
    # can only be true if the entirety of the sequence array is in the array which is why this return method works
    return seqIdx == len(sequence)

    
    