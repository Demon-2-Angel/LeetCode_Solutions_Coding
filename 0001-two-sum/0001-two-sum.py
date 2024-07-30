class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """final_index = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    final_index.append(i)
                    final_index.append(j)
        final_index.sort()
        return final_index"""
        
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []