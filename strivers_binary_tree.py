
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    #preorder traversal
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans =[]
        def inner(root_in):
            if root_in is None:
                return
            ans.append(root_in.val)
            inner(root_in.left)
            inner(root_in.right)
        inner(root)
        return ans