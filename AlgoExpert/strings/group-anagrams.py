def groupAnagrams(words):
    # create hash table to store anagrams
    anagrams = {}

    # loop through each word and sort the letters so all of the words can appear the same
    # for example ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'] will become ['aet', 'aet', 'ant', 'aet', 'ant', 'abt']
    for idx in words:
        sortedWord = "".join(sorted(idx))
        # if the sorted word is in the hash table, append the like word to the list
        # if the sorted word is not in the hash table, add it
        if sortedWord in anagrams:
            anagrams[sortedWord].append(idx)
        else:
            anagrams[sortedWord] = [idx]

    # return the values of the hash table as a list
    return list(anagrams.values())