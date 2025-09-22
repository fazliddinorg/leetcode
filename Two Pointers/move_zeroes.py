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




# SOLUTION 2: Using Extra Space
# Time: O(n), Space: O(n)
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zeros = [num for num in nums if num != 0]
        num_zeros = len(nums) - len(non_zeros)
        
        for i in range(len(non_zeros)):
            nums[i] = non_zeros[i]
        for i in range(len(non_zeros), len(nums)):
            nums[i] = 0