from typing import List

# SOLUTION 1: Two Pointers - Optimal
# Time: O(n), Space: O(n) for char list
class Solution1:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            
            if left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)




# SOLUTION 2: Collect and Replace
# Time: O(n), Space: O(n)
class Solution2:
    def reverseVowels(self, s: str) -> str:
        vowels_set = "aeiouAEIOU"
        vowels_in_s = [c for c in s if c in vowels_set]
        result = []
        for char in s:
            if char in vowels_set:
                result.append(vowels_in_s.pop())
            else:
                result.append(char)
        return "".join(result)