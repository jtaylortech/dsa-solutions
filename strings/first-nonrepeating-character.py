def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        duplicate = False
        for idx2 in range(len(string)):
            #if the two current characters are the same, but idx is at 2 and idx2 is at 3,
                #then that means the character at idx is equal to the character at idx2
            if string[idx] == string[idx2] and idx != idx2:
                duplicate = True

        #returns the idx of the character that isn't a duplicate
        if not duplicate:
            return idx

    return -1

    

    
