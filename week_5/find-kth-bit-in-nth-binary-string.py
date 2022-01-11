#QUESTION
#https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def bitString(self, n):
        if n == 0:
            return "0"
        partial_ans = self.bitString(n-1)
        
        inverted = ""
        for i in partial_ans:
            if i == "0":
                inverted += "1"
            elif i == "1":
                inverted += "0"
                
        str_len = len(inverted)
        i = str_len -1
        
        reversed_str = ""
        while i > -1:
            reversed_str += inverted[i]
            i -= 1
            
        
        return partial_ans + "1" + reversed_str
        
        
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.bitString(n)
        return ans[k-1]
