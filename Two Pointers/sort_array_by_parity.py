from typing import List

# SOLUTION 1: Two Pointers (In-place) - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_ptr = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[even_ptr], nums[i] = nums[i], nums[even_ptr]
                even_ptr += 1
        return nums


        

# SOLUTION 2: Using Extra Space
# Time: O(n), Space: O(n)
class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = [x for x in nums if x % 2 == 0]
        odds = [x for x in nums if x % 2 != 0]
        return evens + odds