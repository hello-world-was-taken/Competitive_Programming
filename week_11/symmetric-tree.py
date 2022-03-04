#https://leetcode.com/problems/symmetric-tree/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def left_root(self, root_left):
        self.left_value.append(root_left)
        left_queue = deque()
        left_queue.append(root_left)
        while left_queue:
            temp_root = left_queue.popleft()
            if temp_root:
                for node in [temp_root.left, temp_root.right]:
                    if (node not in self.visited):
                        self.left_value.append(node) # adding it to the list of left values
                        left_queue.append(node) # adding it to the queue
                        self.visited.add(node)
                    elif node == None:
                        self.left_value.append(node)
            
    def right_root(self, root_right):
        self.right_value.append(root_right)
        right_queue = deque()
        right_queue.append(root_right)
        while right_queue:
            temp_root = right_queue.popleft()
            if temp_root:
                for node in [temp_root.right, temp_root.left]:
                    if (node not in self.visited):
                        self.right_value.append(node) # adding it to the list of left values
                        right_queue.append(node) # adding it to the queue
                        self.visited.add(node)
                    elif node == None:
                        self.right_value.append(node)
            
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.left_value = []
        self.right_value = []
        self.visited = set()
        
        
        if root:
            self.left_root(root.left)
            self.right_root(root.right)
        
        if len(self.right_value) != len(self.left_value):
            return False
        else:
            for i in range(len(self.right_value)):
                if self.right_value[i] and self.left_value[i]:
                    if self.right_value[i].val != self.left_value[i].val:
                        return False
                else:
                    if self.right_value[i] == None and self.left_value[i] == None:
                        pass
                    else:
                        return False
        return True
