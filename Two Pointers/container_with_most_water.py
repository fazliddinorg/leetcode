from typing import List

# SOLUTION 1: Two Pointers - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

        

# SOLUTION 2: Brute Force
# Time: O(n²), Space: O(1)
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1, n):
                max_area = max(max_area, min(height[i], height[j]) * (j-i))
        return max_area
