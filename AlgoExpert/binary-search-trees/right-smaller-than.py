# O(n^2) time | O(n) space - where n is the length of the array
def rightSmallerThan(array):
    rightSmallerCounts = []
    for idx in range(len(array)):
        rightSmallerCount = 0
        for jdx in range(idx + 1, len(array)):
            if array[jdx] < array[idx]:
                rightSmallerCount += 1
        rightSmallerCounts.append(rightSmallerCount)
    return rightSmallerCounts