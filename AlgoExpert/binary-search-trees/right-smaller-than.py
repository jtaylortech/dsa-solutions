# O(n^2) time | O(n) space - where n is the length of the array

# rightSmallerCounts stores the number of elements to the right of the current element that are smaller than the current element in an array
# we can use a brute force approach to solve this problem
# for loop to iterate through the array, rightSmallerCount is a variable that stores the number of elements to the right of the current element that are smaller than the current element
# for loop to iterate through the array starting at the next element to the right of the current element and ending at the last element in the array
# if the current element is greater than the element at the current index of the inner for loop, then increment rightSmallerCount by 1
# append rightSmallerCount to rightSmallerCounts
def rightSmallerThan(array):
    rightSmallerCounts = []
    for idx in range(len(array)):
        rightSmallerCount = 0
        for jdx in range(idx + 1, len(array)):
            if array[jdx] < array[idx]:
                rightSmallerCount += 1
        rightSmallerCounts.append(rightSmallerCount)
    return rightSmallerCounts