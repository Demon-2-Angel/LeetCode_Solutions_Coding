class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        nums = sorted(nums)
        count = 0
        
        while first < last:
            if (nums[first] + nums[last]) < target:
                count = count + (last - first)
                first += 1
            else :
                last -= 1
        
        return count
