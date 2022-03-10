# https://leetcode.com/problems/validate-binary-search-tree/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_wrong_place(self, root, range_val):
        is_bound = lambda range_val, root_val: min(range_val) < root_val < max(range_val) 
        if root:
            if not is_bound(range_val, root.val):
                return False
            
            if root.left:
                res = self.find_wrong_place(root.left, [range_val[0], root.val])
                if res == False:
                    return res
            if root.right:
                return self.find_wrong_place(root.right, [root.val, range_val[1]])
            
            return True
            
            
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            # for the values in the right subtree the should not be less than range[1]
            # and the values in the left subtree should not be greater than range[0]
            
            left_range = [float("-inf"), root.val]
            right_range = [root.val, float("inf")]
            
            res = True
            if root.left:
                res = self.find_wrong_place(root.left, left_range)
                if res == False:
                    return res
                
            if root.right:
                res = self.find_wrong_place(root.right, right_range)

        return res
