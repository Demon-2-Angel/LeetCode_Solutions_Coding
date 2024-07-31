from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = defaultdict(int)
        frequency_t = defaultdict(int)
        s = list(s)
        t = list(t)
        
        for s_letters in s:
            frequency_s[s_letters] += 1
        for t_letters in t:
            frequency_t[t_letters] += 1
        
        if frequency_s.items() == frequency_t.items():
            return True
        else:
            return False