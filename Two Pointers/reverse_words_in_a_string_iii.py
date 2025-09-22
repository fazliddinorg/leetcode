from typing import List

# SOLUTION 1: Pythonic Split, Reverse, Join - Optimal
# Time: O(n), Space: O(n)
class Solution1:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)



# SOLUTION 2: Manual Two Pointers
# Time: O(n), Space: O(n)
class Solution2:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        start = 0
        for end in range(n + 1):
            if end == n or chars[end] == ' ':
                # Reverse the word from start to end-1
                left, right = start, end - 1
                while left < right:
                    chars[left], chars[right] = chars[right], chars[left]
                    left += 1
                    right -= 1
                start = end + 1
        return "".join(chars)