from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = [v for row in grid for v in row]
        rem = arr[0] % x
        
        for v in arr:
            if v % x != rem:
                return -1
        
        arr.sort()
        median = arr[len(arr) // 2]
        
        return sum(abs(v - median) // x for v in arr)
