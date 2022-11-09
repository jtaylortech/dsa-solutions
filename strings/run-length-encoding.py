def runLengthEncoding(string):
    #defines empty list to store characters, later in the code, this will be converted into a string via .join
    encodedStringCharacters = []
    #current run length is set to 1 because the inputted string will be non-empty
    currentRunLength = 1

    #loops through characters in string and stores the current value and the value prior
    for idx in range(1, len(string)):
        currentCharacter = string[idx]
        previousCharacter = string[idx - 1]

        #if the current value doesn't match the previous value, then it will break out of if statement
        #once the run length exceeds 9, will break out of if statement to begin the run length again from 1
        #converts the run length integer into a string and appends it to the list and also adds the previous character value
        #the string for example could be 6, and the previous value could be J which would make up [6J] etc etc
        if currentCharacter != previousCharacter or currentRunLength ==9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharacter)
            currentRunLength = 0

        currentRunLength += 1

    # breaks out of the if statement to make the final run through the string
    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) -1])

    #converts the array into a string
    return "".join(encodedStringCharacters)