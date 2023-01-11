def minimumCharactersForWords(words):
    # created a dictionary to store the max frequency of each character
    maxCharFreq = {}

    # for loop to iterate through the words and update the maxCharFreq
    for word in words:
        charFreq = countCharFreq(word) #1
        updateMaxFreqs(charFreq, maxCharFreq) #2

    return makeArrayFromCharFreq(maxCharFreq) #3

        
# counts the frequency of each character in a string by iterating through the string and updating the dictionary
def countCharFreq(string): #1
    charFreq = {}
    for character in string:
        if character not in charFreq:
            charFreq[character] = 0
        charFreq[character] += 1

    return charFreq


# updates the maxCharFreq dictionary by iterating through the charFreq dictionary and updating the maxCharFreq dictionary
# if the character is not in the maxCharFreq dictionary then update the maxCharFreq dictionary 
def updateMaxFreqs(freqs, maxFreq): #2
    for character in freqs:
        freq = freqs[character]

        if character in maxFreq:
            maxFreq[character] = max(freq, maxFreq[character])
        else:
            maxFreq[character] = freq


# makes an array of characters from the maxCharFreq dictionary
# iterates through the maxCharFreq dictionary and appends the character to the array the number of times it appears in the dictionary
def makeArrayFromCharFreq(charFreq): #3
    characters = []

    for character in charFreq:
        freq = charFreq[character]

        for idx in range(freq):
            characters.append(character)

    return characters