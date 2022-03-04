#https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# Not my solution. Finally caved and saw the discussion section. A travesty :-(



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_deepest(self, root, deep_val):
        if not root:
            return deep_val - 1
            
        left_depth = self.find_deepest(root.left, deep_val + 1)
        right_depth = self.find_deepest(root.right, deep_val + 1)
        
        self.max_depth = max(self.max_depth, left_depth, right_depth)
        
        if left_depth == right_depth == self.max_depth:
            self.node = root
            
        return max(left_depth, right_depth)
        
        
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.node = root
        self.max_depth = 0
        self.find_deepest(root, 0)
        return self.node
