from ast import List

# O(nlog(n)) time | O(n) space - where n is the number of balloons in the array
# this is the time and space complexity of the optimal solution which uses a greedy algorithm to find the minimum number of arrows needed to burst all the balloons

# points is the list of balloons and each balloon is represented by a list of 2 integers
# the first integer is the x coordinate of the start of the balloon and the second integer is the x coordinate of the end of the balloon
# the minimum number of arrows needed to burst all the balloons is returned at the end of the function

# sort the balloons by the x coordinate of the end of the balloon
# define the number of arrows as 1
# define the x coordinate of the end of the first balloon as the first end
# iterate through the balloons and find the minimum number of arrows needed to burst all the balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort by x_end
        points.sort(key = lambda x : x[1])
        
        arrows = 1
        first_end = points[0][1]
        for x_start, x_end in points:
            # if the current balloon starts after the end of another one,
            # one needs one more arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end
        
        return arrows