from typing import List

# SOLUTION 1: List Concatenation - Optimal
# Time: O(n), Space: O(n)
class Solution1:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums



# SOLUTION 2: Manual Construction
# Time: O(n), Space: O(n)
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans