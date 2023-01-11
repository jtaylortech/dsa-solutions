import math

def arrayOfProducts(array):
    sums = []

    # iterate through the array and calculate the product of all the numbers except the current number
    # append the product to the sums array
    # return the sums array
    for idx, _ in enumerate(array):
        before_idx = math.prod(array[:idx])
        after_idx = math.prod(array[idx+1:])
        sums.append(before_idx*after_idx)

    return sums