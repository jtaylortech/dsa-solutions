def firstNonRepeatingCharacter(string):
    # for loop to iterate through the string and update the dictionary
    # if the character is not in the dictionary then add it to the dictionary
    # second for loop to iterate through the string and return the first character that has a frequency of 1
    # if no character has a frequency of 1 then return -1
    for idx in range(len(string)):
        duplicate = False
        for idx2 in range(len(string)):
            # if the character is not the same as the character at the current index then check if the character is the same as the character at the current index
            # if the character is the same as the character at the current index then set duplicate to True and break out of the for loop   
            if string[idx] == string[idx2] and idx != idx2:
                duplicate = True

        #returns the idx of the character that isn't a duplicate
        if not duplicate:
            return idx

    return -1

    

    
