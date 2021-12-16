#QUESTION
#https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n):
        temp = 1
        answer = []
        while(temp <= n):
            if((temp % 5 == 0) and (temp % 3 == 0)):
                answer.append("FizzBuzz")
            elif(temp % 5 == 0):
                answer.append("Buzz")
            elif(temp % 3 == 0):
                answer.append("Fizz")
            else:
                answer.append(str(temp))
            
            temp += 1
        
        return answer
