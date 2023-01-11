# O(n^2) time, O(n) space - where n is the target position


import collections


class Solution:
    # queue = [(moves, pos, vel)]
    # while statement to pop from queue and append to queue until pos == target
    def racecar(self, target: int) -> int:
        queue = collections.deque([(0, 0, 1)])
        while queue:
            moves, pos, vel = queue.popleft()

            if pos == target:
                return moves
            queue.append((moves + 1, pos + vel, 2 * vel))
          
            # if statement to check if pos + vel > target and vel > 0 or pos + vel < target and vel < 0
            # if true, append to queue with moves + 1, pos, -vel / abs(vel)
            if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                queue.append((moves + 1, pos, -vel / abs(vel)))