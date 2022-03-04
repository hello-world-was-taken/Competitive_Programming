#https://leetcode.com/problems/average-of-levels-in-binary-tree/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        visited = set()
        if root:
            self.ans = [root.val]
            queue.append(root)
            first = True
            temp_queue = deque()
            while queue:
                temp_root = queue.popleft()
                while queue or first:

                    if len(queue):
                        temp_root = queue.popleft()
                    first = False
                    summation = 0
                    count = 0
                    if temp_root:
                        if temp_root.left:
                            temp_queue.append(temp_root.left)
                        if temp_root.right:
                            temp_queue.append(temp_root.right)
                    
                    if not len(queue):
                        for node in temp_queue:
                            summation += node.val
                            
                        if len(temp_queue):
                            self.ans.append(summation/len(temp_queue))
                        queue = temp_queue.copy()
                        temp_queue = deque()
                        
                
        return self.ans
