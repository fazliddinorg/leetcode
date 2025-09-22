from typing import List

# SOLUTION 1: Two Pointers (Slow and Fast) - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1 # Pointer for the next unique element's position
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k




# SOLUTION 2: Using Pop
# Time: O(n^2) in worst case (pop from middle), Space: O(1)
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)