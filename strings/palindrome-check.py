def isPalindrome(string):
    #stores the reversed string
    flippedString = ""
    # for loop to iterate through the string and add the characters to the flippedString
    # reversed() returns a reversed iterator
    # flippedString works by adding the characters to the front of the string so the characters are in reverse order
    for idx in reversed(range(len(string))):
        flippedString += string[idx]
    return flippedString == string