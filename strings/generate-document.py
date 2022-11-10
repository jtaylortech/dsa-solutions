def generateDocument(characters, document):
    #hash table (or dict) to store the key character and character counts
    charCounts = {}

    #for loop iterating through characters
    #if statement adding each character to the dictionary if it is not already present
    #when the current value is already present, the count will go up by 1
    for idx in characters:
        if idx not in charCounts:
            charCounts[idx] = 0 #sets default value to zero and adds it to the table

        charCounts[idx] += 1 #changes that default value to 1 and adds another when needed


    #for loop iterates through document
    #if statement to determine rather the character is present in the table or not
    #if the character isnt present == false
    #if there are 4 values of the character in the document but only 3 in the table == false
    for idx in document:
        if idx not in charCounts or charCounts[idx] == 0:
            return False

        #each time we come across a value that is in the table, we will subtract 1 to keep track of how many times we've used it
        #so if we needed 5 "J"s, and only had 4 stored, then we would return False, if there are => 5, then we are good
        charCounts[idx] -= 1

    return True
            
  