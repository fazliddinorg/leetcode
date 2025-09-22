from typing import List

# SOLUTION 1: Two Pointers (In-place) - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1




# SOLUTION 2: Built-in Method
# Time: O(n), Space: O(1)
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()