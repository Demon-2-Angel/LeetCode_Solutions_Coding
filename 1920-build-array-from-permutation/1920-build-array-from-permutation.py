class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        f"""or i in nums:
            nums = nums[nums[i]]
        return nums"""
        return (nums[num] for num in nums)