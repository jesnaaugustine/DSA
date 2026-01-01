
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
    


    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans =[]
        def inner(que):
            if len(que)==0:
                return
            ans_temp =[]
            q_temp=[]

            for q in que:
                ans_temp.append(q.val)
                if q.left is not None:
                    q_temp.append(q.left)
                if q.right is not None:
                    q_temp.append(q.right)
            ans.append(ans_temp)
            que = q_temp
            inner(que)
        if root is not None:
            inner([root])
        return ans
    
    ###depth of a tree
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def inner(root_in):
            if root_in is None:
                return 0
            left = inner(root_in.left)
            right = inner(root_in.right)
            return max(left,right)+1
        return inner(root)
if __name__=='__main__':
    root = TreeNode(val =1,left =None,right =None)
    right = TreeNode(val =2,left =TreeNode(3),right =None)
    root.right =right
    sol = Solution()
    print(sol.preorderTraversal(root))
    print(sol.inorderTraversal(root))
    print(sol.postorderTraversal(root))
    print(sol.levelOrder(root))
    print(sol.maxDepth(root))