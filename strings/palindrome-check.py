def isPalindrome(string):
    flippedString = ""
    for idx in reversed(range(len(string))):
        flippedString += string[idx]
    return flippedString == string