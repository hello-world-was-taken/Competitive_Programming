#https://leetcode.com/problems/path-sum/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_sum(self, root, curr_sum):
        if root != None:
            curr_sum += root.val
            if root.left == None and root.right == None:
                return self.target_sum == curr_sum
        
            res = False
            if root.left != None:
                res = self.find_sum(root.left, curr_sum)
            if res == False and root.right != None:
                res = self.find_sum(root.right, curr_sum) 
            return res
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # self.summation = 0
        self.target_sum = targetSum
        return self.find_sum(root, 0) if root != None else False
