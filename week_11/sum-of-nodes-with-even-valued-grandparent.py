#https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calc_sum(self, root, p, gp):
        if root:
            if gp % 2 == 0:
                self.summation += root.val
            self.calc_sum(root.left, root.val, p)
            self.calc_sum(root.right, root.val, p)
        
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.summation = 0
        self.calc_sum(root, -1, -1)
        return self.summation
