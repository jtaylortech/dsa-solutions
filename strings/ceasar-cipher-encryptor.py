def caesarCipherEncryptor(text,s):
    result = ""

    for i in range(len(text)):    #transverse the plain text
        char = text[i]
        
        result += chr((ord(char) + s - 97) % 26 + 97)  #encrypts the characters
            
    return result
