# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a=[]
    def travs(self,root):
        if not root:
            return 
        self.travs(root.left)
        self.a.append(root.val)
        self.travs(root.right)
    
                
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.travs(root)
        return self.a
        
     
        
      