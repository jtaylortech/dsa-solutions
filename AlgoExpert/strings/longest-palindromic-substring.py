def longestPalindromicSubstring(string):
    # for loop to iterate through the string and check if the substring is a palindrome
    # if the substring is a palindrome then check if the length of the substring is greater than the current longest palindrome
    # if the length of the substring is greater than the current longest palindrome then update the longest palindrome
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j + 1]
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
    return longest

# defines the isPalindrome function
# checks if the string is equal to the reversed string
# returns True if the string is equal to the reversed string
# while loop to iterate through the string and add the characters to the flippedString by adding the characters to the front of the string
# if statement to check if the string is equal to the flippedString
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True