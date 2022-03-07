#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        left_right = True
        final_ans = []
        while queue:
            size = len(queue)
            current_level = []
        
            for i in range(size):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    current_level.append(node.val)
            if len(current_level):
                if left_right:
                    final_ans.append(current_level)  
                else:
                    current_level.reverse()
                    final_ans.append(current_level)
            left_right = not left_right
            
        return final_ans
