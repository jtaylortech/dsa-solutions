def caesarCipherEncryptor(text,s):
    # stores the encrypted text
    result = ""

    # traverse the text one character at a time
    # ord() returns the unicode code point for a character and chr() returns the character for a unicode code point
    # ord('a') = 97 and ord('z') = 122
    # use the modulo operator to wrap around the alphabet and get the correct character for the encrypted text
    for i in range(len(text)):
        char = text[i]
        
        result += chr((ord(char) + s - 97) % 26 + 97)
            
    return result
