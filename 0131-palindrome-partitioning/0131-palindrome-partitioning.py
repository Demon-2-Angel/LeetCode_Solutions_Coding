import copy

class Solution:
    def is_palindrome(self,target):
        left,right = 0,len(target)-1
        while left <= right:
            if target[left] != target[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        result,current_candidate = [],[]
        def helper(start_index, current_candidate):
            # if you don't deepcopy below you will get empty list due to referring var in python
            current_candidate = copy.deepcopy(current_candidate)
            if start_index >= len(s):
                result.append(current_candidate)
            for i in range(start_index,len(s)):
                if self.is_palindrome(s[start_index:i+1]):
                    current_candidate.append(s[start_index:i+1])
                    helper(i+1, current_candidate)
                    current_candidate.pop()
            return
        helper(0,[])
        return result