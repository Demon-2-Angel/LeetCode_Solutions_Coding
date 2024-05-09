class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i in range(len(happiness)):
            if k > 0 and happiness[i] - i > 0:
                res += (happiness[i] - i)
                k -=1
            else:
                return res
        return res