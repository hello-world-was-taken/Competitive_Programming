#https://leetcode.com/problems/maximum-depth-of-n-ary-tree/



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def find_depth(self, root, depth):
        if root:
            if root.children:
                for child in root.children:
                    self.find_depth(child, depth+1)
            else:
                self.depth = max(self.depth, depth)
    
    def maxDepth(self, root: 'Node') -> int:
        self.depth = 0
        self.find_depth(root, 1)
        return self.depth
