# SOLUTION 1: HashMap - MOST OPTIMAL
# Time: O(n), Space: O(n)
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

        return []


# SOLUTION 2: Two Pointers with Index Tracking
# Time: O(n log n), Space: O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()
        
        left, right = 0, len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return sorted([indexed_nums[left][1], indexed_nums[right][1]])
        
        return []
