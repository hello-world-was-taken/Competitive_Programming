#https://leetcode.com/problems/binary-tree-tilt/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tilt_sum(self, root):
        if root != None:
            if root.left == None and root.right == None:
                return
            self.tilt_sum(root.left)
            self.tilt_sum(root.right)
            curr_left = 0 if root.left == None else root.left.val
            curr_right = 0 if root.right == None else root.right.val
            root.val += (curr_left + curr_right)
            self.summation += abs(curr_left - curr_right)
        
        
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.summation = 0
        self.tilt_sum(root)
        return self.summation
