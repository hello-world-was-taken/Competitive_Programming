#QUESTION
#https://leetcode.com/problems/sorting-the-sentence/submissions/
#NEEDS SERIOUS REFACTORING

class Solution:
    def sortSentence(self, s):
        split_sentence = s.split()
        
        len_split = len(split_sentence)
        
        mini_index = 0
        ans_string = ""
        innerLoop = False
        
        for j in range(len_split):
            mini = int(split_sentence[j][-1])
            innerLoop = False
            for i in range(j+1, len_split):
                if (int(split_sentence[i][-1])) < mini:
                    print("inside")
                    mini = int(split_sentence[i][-1])
                    mini_index = i
                    innerLoop = True
                
                    
            if(innerLoop):
                split_sentence[j], split_sentence[mini_index] = split_sentence[mini_index], split_sentence[j]
            

            print(split_sentence)
            word = split_sentence[j][:-1]
            print(word)
            if j != (len_split - 1):
                ans_string += word + " "
            else:
                ans_string += word
        
        return ans_string
