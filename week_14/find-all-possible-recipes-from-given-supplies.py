# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/



class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        can_cook = defaultdict(list)
        dep_count = defaultdict(int)
        
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                can_cook[ingredient].append(recipe)
            dep_count[recipe] = len(ingredients[i])
        
        cooked = []
        queue = deque(supplies)
        while queue:
            item = queue.popleft()
            
            for recipe in can_cook[item]:
                dep_count[recipe] -= 1
                if dep_count[recipe] == 0:
                    cooked.append(recipe)
                    queue.append(recipe)
            
        return cooked
