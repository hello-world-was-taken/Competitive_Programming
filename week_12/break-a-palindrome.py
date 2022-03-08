#https://leetcode.com/problems/break-a-palindrome/



class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        first_non_a = None
        for index, letter in enumerate(palindrome):
            if letter != 'a' and first_non_a == None:
                # print("index: ", index, "letter: ", letter)
                first_non_a = index
            if len(palindrome) %2 and first_non_a and first_non_a == len(palindrome)//2:
                first_non_a = None
        
        if not first_non_a and len(palindrome) > 1 and palindrome[len(palindrome)-1] == 'a':
            first_non_a = len(palindrome) - 1
        elif first_non_a == None or len(palindrome) == 1:
            return ""
        
        new_str = ""
        
        letter_to_be_swapped = 'b' if first_non_a == len(palindrome) - 1 and palindrome[first_non_a] == 'a' else 'a'
        
        
        for i, v in enumerate(palindrome):
            if i == first_non_a:
                new_str += letter_to_be_swapped
            else:
                new_str += v
        
        return new_str
    
