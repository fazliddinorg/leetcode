from typing import List

# SOLUTION 1: Two Pointers (In-place) - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx, odd_idx = 0, 1
        n = len(nums)
        while even_idx < n and odd_idx < n:
            if nums[even_idx] % 2 != 0 and nums[odd_idx] % 2 == 0:
                nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            
            if nums[even_idx] % 2 == 0:
                even_idx += 2
            if nums[odd_idx] % 2 != 0:
                odd_idx += 2
        return nums

# SOLUTION 2: Using Extra Space
# Time: O(n), Space: O(n)
class Solution2:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 != 0]
        result = [0] * len(nums)
        result[::2] = evens
        result[1::2] = odds
        return result