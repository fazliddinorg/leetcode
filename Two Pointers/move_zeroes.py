from typing import List

# SOLUTION 1: Two Pointers (In-place) - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for i, right in enumerate(nums):
            if right != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
