from typing import List
from collections import defaultdict

# SOLUTION 1: Categorize by Sorted String - Optimal
# Time: O(n * k log k), Space: O(n * k) where n is # of strs, k is max length
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())



# SOLUTION 2: Categorize by Character Count
# Time: O(n * k), Space: O(n * k)
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Tuples are hashable and can be dict keys
            anagram_map[tuple(count)].append(s)
        return list(anagram_map.values())
