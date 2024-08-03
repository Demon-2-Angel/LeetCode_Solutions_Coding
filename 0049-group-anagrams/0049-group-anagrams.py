class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram[sorted_word].append(word)
        
        return list(anagram.values())