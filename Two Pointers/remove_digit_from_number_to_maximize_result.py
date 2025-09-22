from typing import List

# SOLUTION 1: Greedy Approach - Optimal
# Time: O(n), Space: O(n)
class Solution1:
    def removeDigit(self, number: str, digit: str) -> str:
        last_occurrence_index = -1
        for i in range(len(number)):
            if number[i] == digit:
                if i + 1 < len(number) and number[i+1] > digit:
                    return number[:i] + number[i+1:]
                last_occurrence_index = i
        return number[:last_occurrence_index] + number[last_occurrence_index+1:]



# SOLUTION 2: Brute Force
# Time: O(n^2), Space: O(n)
class Solution2:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num_str = ""
        for i in range(len(number)):
            if number[i] == digit:
                current_num_str = number[:i] + number[i+1:]
                if max_num_str == "" or current_num_str > max_num_str:
                    max_num_str = current_num_str
        return max_num_str