from typing import List

# SOLUTION 1: Built-in Method - Optimal
# Time: O(n), Space: O(n)
class Solution1:
    def toLowerCase(self, s: str) -> str:
        return s.lower()




# SOLUTION 2: Manual ASCII Conversion
# Time: O(n), Space: O(n)
class Solution2:
    def toLowerCase(self, s: str) -> str:
        result = []
        for char in s:
            ascii_val = ord(char)
            if 65 <= ascii_val <= 90: # ASCII for 'A'-'Z'
                result.append(chr(ascii_val + 32))
            else:
                result.append(char)
        return "".join(result)