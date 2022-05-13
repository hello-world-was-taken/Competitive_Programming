# https://leetcode.com/problems/fruit-into-baskets/



class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit1 = fruits[0]
        fruit2 = None
        _max = 0
        i = j = 0

        for k, num in enumerate(fruits):
            if num != fruit1:
                j = k
                fruit2 = num
                break
                
        first_occurence_of_fruit1 = -1
        first_occurence_of_fruit2 = j
        
        while i < len(fruits) and j < len(fruits):
            if first_occurence_of_fruit1 == -1 and fruits[j] == fruit1:
                first_occurence_of_fruit1 = j
                first_occurence_of_fruit2 = -1
                
            if first_occurence_of_fruit2 == -1 and fruits[j] == fruit2:
                first_occurence_of_fruit2 = j
                first_occurence_of_fruit1 = -1
                
            if fruits[j] == fruit1 or fruits[j] == fruit2:
                pass
            else:
                i = max(first_occurence_of_fruit1, first_occurence_of_fruit2)
                first_occurence_of_fruit2 = j
                first_occurence_of_fruit1 = -1
                fruit1 = fruits[i]
                fruit2 = fruits[j]
            
            _max = max(_max, j-i+1)
            j += 1
            
        return _max
        
