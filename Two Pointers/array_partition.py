from typing import List

# SOLUTION 1: Sorting - Optimal
# Time: O(n log n), Space: O(1) or O(n) depending on sort implementation
class Solution1:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total



# SOLUTION 2: Pythonic Slicing
# Time: O(n log n), Space: O(n) for the slice
class Solution2:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])