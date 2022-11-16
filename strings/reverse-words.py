def reverseWordsInString(string):
    # characters is a list of characters in the string that we will modify in place to reverse the string
    # this is done because strings are immutable so we can't modify them in place, meaning we have to convert them to a list
    # reverseListRange() reverses the list in place so we don't have to copy the list
    characters = [char for char in string]
    reverseListRange(characters, 0, len(characters) - 1)

    # startOfWord is the index of the first character of the current word we are reversing
    # while we iterate through the list, we keep track of the index of the first character of the current word
    # when we reach the end of the word, we reverse the word in place
    # then we set startOfWord to the index of the first character of the next word and continue iterating
    startOfWord = 0
    while startOfWord < len(characters):
        endOfWord = startOfWord
        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1

        # we subtract 1 from endOfWord because we want to include the last character of the word
        reverseListRange(characters, startOfWord, endOfWord - 1)
        startOfWord = endOfWord + 1

    # we convert the list back to a string and return it
    return "".join(characters)


# this function reverses a list in place by swapping the first and last elements, then the second and second to last, etc.
def reverseListRange(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1