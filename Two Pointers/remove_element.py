from typing import List

# SOLUTION 1: Two Pointers (Slow and Fast) - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the next position to place a non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# SOLUTION 2: Two Pointers (From Both Ends)
# Time: O(n), Space: O(1)
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1  # Reduce array size
            else:
                i += 1
        return n