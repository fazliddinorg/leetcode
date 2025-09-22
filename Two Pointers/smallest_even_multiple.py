from typing import List

# SOLUTION 1: Conditional Logic - Optimal
# Time: O(1), Space: O(1)
class Solution1:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n * 2



# SOLUTION 2: Bitwise Operation
# Time: O(1), Space: O(1)
class Solution2:
    def smallestEvenMultiple(self, n: int) -> int:
        # If n is odd, (n & 1) is 1. We shift left by 1 (multiply by 2).
        # If n is even, (n & 1) is 0. We shift left by 0 (multiply by 1).
        return n << (n & 1)