def validIPAddresses(string):
    ipAddressFound = []

    # for loop to get the first part of the IP address
    # range is 1 to 3 because the IP address cannot be more than 3 digits
    # and cannot be less than 1 digit
    # use the isValidParts function to check if the first part is valid
    # currentParts will be a list of the parts of the IP address
    for idx in range(1, min(len(string), 4)):
        currentIPAddressParts = ["","","",""]

        # use the isValidParts function to check if the first part is valid
        # if it is, add it to the currentIPAddressParts array
        currentIPAddressParts[0] = string[:idx]
        if not isValidParts(currentIPAddressParts[0]):
                continue

        # for loop to get the second part of the IP address
        # use the isValidParts function to check if the second part is valid
        # if it is, add it to the currentIPAddressParts array
        for jdx in range(idx + 1, idx + min(len(string) - idx, 4)):
            currentIPAddressParts[1] = string[idx:jdx]
            if not isValidParts(currentIPAddressParts[1]):
                continue

            # for loop to get the third and forth part of the IP address
            # use the isValidParts function to check if the third and forth part is valid
            # if it is, add it to the currentIPAddressParts array
            for kdx in range(jdx + 1, jdx + min(len(string) - jdx, 4)):
                currentIPAddressParts[2] = string[jdx:kdx]
                currentIPAddressParts[3] = string[kdx:]
                
                # if the third and forth part is valid, add the currentIPAddressParts to the ipAddressFound array
                # and join the array with a period
                if isValidParts(currentIPAddressParts[2]) and isValidParts(currentIPAddressParts[3]):
                    ipAddressFound.append(".".join(currentIPAddressParts))

    return ipAddressFound


# use the isValidParts function to check if each part is valid
def isValidParts(string):
    stringAsInt = int(string)
    if stringAsInt > 255:
        return False
    return len(string) == len(str(stringAsInt))