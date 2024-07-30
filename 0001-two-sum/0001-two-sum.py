class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_index = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    final_index.append(i)
                    final_index.append(j)
        final_index.sort()
        return final_index
                    
        