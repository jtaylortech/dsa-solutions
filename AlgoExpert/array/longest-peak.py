def longestPeak(array):
    # sets longestPeak to 0 because if there is no peak, the longest peak is 0
    # sets idx to 1 because we need to check the previous and next value of the current value
    longestPeakLength = 0
    idx = 1

    # while loop to iterate through the array while idx is less than the length of the array - 1
    while idx < len(array) - 1:
        # isPeak checks if the current value is greater than the previous and next value
        # if it is, we increment the currentPeakLength by 1
        isPeak = array[idx - 1] < array [idx] and array[idx] > array[i + 1]
        if not isPeak:
            idx += 1
            continue

        # leftIdx - 2 because we need to check the previous value of the previous value of the current value to see if it is a peak
        # rightIdx + 2 because we need to check the next value of the next value of the current value to see if it is a peak
        # while loop to iterate through the array while the leftIdx is greater than or equal to 0 and the value of the leftIdx is less than the value of the leftIdx + 1
        # while loop to iterate through the array while the rightIdx is less than the length of the array and the value of the rightIdx is less than the value of the rightIdx - 1
        leftIdx = idx - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = idx + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        # currentPeakLength is the difference between the rightIdx and the leftIdx - 1
        # longestPeakLength is the max of the currentPeakLength and the longestPeakLength
        # idx is set to the rightIdx because we have already checked the values in between the leftIdx and the rightIdx and we don't need to check them again
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        idx = rightIdx

    return longestPeakLength
        



""" 
1. Find all the peaks with strictly
2. See how long these peaks are by going left and right
3. Compare values of the peaks length and return the longest peak 
"""