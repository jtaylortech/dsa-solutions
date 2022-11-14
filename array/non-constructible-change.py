def nonConstructibleChange(coins):
    # sort the array of coins
    # define a variable that will keep track of the change
    coins.sort()
    currentChangeCreated = 0
    
    # iterate through the array of coins and check if the current coin is greater than the current change created + 1
    # if it is, then return the current change created + 1
    # update the current change created
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coin

    return currentChangeCreated + 1
    
