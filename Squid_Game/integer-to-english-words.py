# https://leetcode.com/problems/integer-to-english-words/


class Solution:
    def numberToWords(self, num: int) -> str:
        # "" at the first idx is used for offset -> meaning less_than_20[1] = "one", less_than_20[5] = "five" and so on
        less_than_20 =[ "","One","Two","Three","Four","Five"
                       ,"Six","Seven","Eight","Nine","Ten",
                       "Eleven","Twelve","Thirteen","Fourteen","Fifteen",
                       "Sixteen","Seventeen","Eighteen","Nineteen"]
        
        tens = ["","Ten","Twenty","Thirty","Forty","Fifty",
                "Sixty","Seventy","Eighty","Ninety"]
        
        thousands = [""," Thousand"," Million"," Billion"]
        
        if num == 0:
            return "Zero"
        
        def recur(num, place):
            if num == 0:
                return ""
            
            elif num < 20:
                return  less_than_20[ num ] + thousands[place]
            
            elif num < 100:
                second = num % 10
                num //= 10
                first = num
                if second > 0:
                    return tens[first] + " " + less_than_20[second] + thousands[place]
                return tens[first] + thousands[place]
            
            elif num < 1000:
                first = num // 100
                part = recur(num % 100, 0)
                if part:
                    return less_than_20[first] + " Hundred " + part + thousands[place]
                return less_than_20[first] + " Hundred" + thousands[place]
        
        ans = []
        _round = 0
        while num > 0:
            _mod = num % 1000
            res = recur( _mod, _round )
            
            if res:
                ans.append( res )
            
            num //= 1000
            _round += 1
            
        ans.reverse()  
        return " ".join( ans )
