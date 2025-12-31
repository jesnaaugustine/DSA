
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
    

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans =[]
        def inner(root_in):
            if root_in is None:
                return
            inner(root_in.left)
            ans.append(root_in.val)
            inner(root_in.right)
        inner(root)
        return ans
    

    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans =[]
        def inner(root_in):
            if root_in is None:
                return
            inner(root_in.left)
            inner(root_in.right)
            ans.append(root_in.val)
        inner(root)
        return ans
    
if __name__=='__main__':
    root = TreeNode(val =1,left =None,right =None)
    right = TreeNode(val =2,left =TreeNode(3),right =None)
    root.right =right
    sol = Solution()
    print(sol.preorderTraversal(root))
    print(sol.inorderTraversal(root))
    print(sol.postorderTraversal(root))