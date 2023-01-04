# O(m * n * k) time | O(m * n * k) space - where m is the number of rows, n is the number of columns, and k is the number of obstacles
# this is the time and space complexity if we are not allowed to use the built-in sort method

# shortestPath function works by using a queue to keep track of the current position and the number of obstacles that can be removed
# we also use a set to keep track of the visited positions and the number of obstacles that can be removed
# we use a while loop to iterate through the queue
# we use a for loop to iterate through the queue
# we use a nested for loop to iterate through the four directions
# we use an if statement to check if the current position is the destination
# if it is, we return the current answer
# we use an if statement to check if the current position is valid and if the current position and the number of obstacles that can be removed has not been visited
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 3:
            return m + n - 2
        q = deque([(0, 0, k)])
        vis = {(0, 0, k)}
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                i, j, k = q.popleft()
                for a, b in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n:
                        if x == m - 1 and y == n - 1:
                            return ans
                        if grid[x][y] == 0 and (x, y, k) not in vis:
                            q.append((x, y, k))
                            vis.add((x, y, k))
                        if grid[x][y] == 1 and k > 0 and (x, y, k - 1) not in vis:
                            q.append((x, y, k - 1))
                            vis.add((x, y, k - 1))
        return -1