from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(dict(Counter(nums).most_common(k)))
        
"""
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
        
        # Step 2: Sort the numbers by frequency and return the top k
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Extract the top k frequent elements
        return [item[0] for item in sorted_items[:k]]

"""
        
            
"""
from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        count = Counter(nums)
        
        # Use a heap to get the k most frequent elements
        return heapq.nlargest(k, count.keys(), key=count.get)

"""