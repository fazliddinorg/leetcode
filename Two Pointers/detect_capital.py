from typing import List

# SOLUTION 1: Built-in String Methods - Optimal
# Time: O(n), Space: O(1)
class Solution1:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()



# SOLUTION 2: Manual Count and Check
# Time: O(n), Space: O(1)
class Solution2:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        cap_count = sum(1 for char in word if 'A' <= char <= 'Z')
        
        if cap_count == n: return True # All caps
        if cap_count == 0: return True # All lower
        if cap_count == 1 and 'A' <= word[0] <= 'Z': return True # Title case
        
        return False