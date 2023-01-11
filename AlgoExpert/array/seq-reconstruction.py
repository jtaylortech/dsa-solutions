from ast import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_edge_counts = defaultdict(int)
        
        for seq in sequences:
            for i in range(1, len(seq)):
                graph[seq[i-1]].append(seq[i])
                in_edge_counts[seq[i]] += 1
        
        # the 1st num must have 0 incoming edge
        if in_edge_counts[nums[0]] > 0:
            return False
            
        stack = [nums[0]]
        i = 1
                
        while stack:
            node = stack.pop()
            for child in graph[node]:
                in_edge_counts[child] -= 1
                if not in_edge_counts[child]:
                    # return false 
                    # if there are any other nodes with 0 incoming edges
                    # or the node with 0 incoming edges != nums[i]
                    if stack or child != nums[i]:
                        return False
                    stack.append(child)
                    i += 1

        return i == len(nums)