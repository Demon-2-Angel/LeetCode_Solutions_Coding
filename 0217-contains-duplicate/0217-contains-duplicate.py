from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_count = defaultdict(int)
        
        for num in nums:
            freq_count[num] += 1
            
        result = {num : count for num, count in freq_count.items() if count >= 2}
        
        if result:
            return True
        else:
            return False