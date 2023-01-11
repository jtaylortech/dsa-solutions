def mergeOverlappingIntervals(intervals):
    # if there is only one interval, return it; as it is already merged
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals

    # sort the intervals by the first value of the interval
    # if the first value of the interval is the same, sort by the second value of the interval
    # result is a list of sorted intervals and holds the first interval
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]

    # for loop through the intervals starting from the second interval to the end of the intervals
    # if statement to check if the first value of the interval is less than or equal to the second value of the last interval in the result
    # if it is, we update the second value of the last interval in the result to the max of the second value of the last interval in the result and the second value of the interval
    # if it is not, we append the interval to the result
    for idx in intervals[1:]:
        if idx[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], idx[1])
        else:
            result.append(idx)

    return result