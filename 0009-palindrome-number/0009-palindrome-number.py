class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        y = x[::-1]
        if x == y:
            return True
        return False