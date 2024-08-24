class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array first
        final = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for i
            
            j, k = i + 1, len(nums) - 1  # j should start from i + 1
            
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                
                if three_sum == 0:
                    final.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1
        
        return final
