# class Solution:
#     def findComplement(self, num: int) -> int:
#         length = num.bit_length()
#         mask = (1 << length) - 1
#         return num ^ mask
    
class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num)[2:]
        
        complement = ''.join('1' if bit=='0' else '0' for bit in binary_num)
        return int(complement,2)