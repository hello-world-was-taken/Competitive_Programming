#https://leetcode.com/problems/remove-duplicate-letters/



class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letter_count = {}
        
        for letter in s:
            if not letter_count.get(letter):
                letter_count[letter] = []
                letter_count[letter].append(1)
                # Rather than the true false to see whether we have previously visited it, we could 
                # have used a visited set to keep track of the values we have already pushed to the stack
                letter_count[letter].append(False)
            else:
                letter_count[letter][0] += 1
        
        letter_stack = []
        
        for letter in s:
            if not len(letter_stack):
                letter_stack.append(letter)
                letter_count[letter][1] = True
            else:
                while len(letter_stack) and letter_stack[-1] > letter and letter_count[letter_stack[-1]][0] > 1 and not letter_count[letter][1]:
                    letter_count[letter_stack[-1]][0] -= 1
                    letter_count[letter_stack[-1]][1] = False
                    letter_stack.pop()
                if not letter_count[letter][1]:
                    letter_stack.append(letter)
                    letter_count[letter][1] = True
                else:
                    letter_count[letter][0] -= 1
        
        ans = ""
        
        for i in letter_stack:
            ans += i
        
        return ans
