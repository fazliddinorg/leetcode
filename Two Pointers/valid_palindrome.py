from typing import List

# SOLUTION 1: Two Pointers - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True



# SOLUTION 2: Filter and Compare
# Time: O(n), Space: O(n)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        return filtered_chars == filtered_chars[::-1]