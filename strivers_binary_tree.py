
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
    
    #return true if it is a Balanced Binary Tree else return false. A Binary Tree is balanced if, for all nodes in the tree, the difference between left and right subtree height is not more than 1..
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        def inner(root_in):
            if root_in is None:
                return 0
            left = inner(root_in.left)
            right = inner(root_in.right)
            if left ==-1 or right ==-1:
                return -1
            if abs(left-right)>1:
                return -1
            else:
                return max(left,right)+1
        
        ind = inner(root)
        if ind ==-1:
            return False
        else:
            return True
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi =0
        def inner(root_in):
            if root_in is None:
                return 0
            left = inner(root_in.left)
            right = inner(root_in.right)
            self.maxi = max(self.maxi,left+right)
            return max(left,right)+1
        inner(root)
        return self.maxi  


    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = float('-inf')
        def inner(root_in):
            if root_in is None:
                return 0
            left_s = max(0,inner(root_in.left))
            right_s= max(0,inner(root_in.right))
            self.maxi = max(self.maxi,left_s+right_s+root_in.val)

            return max(left_s,right_s)+root_in.val
        inner(root)
        return self.maxi

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        self.ans1=[]
        self.ans2 =[]
        def inner(root1,ans):
            if root1 is None:
                ans.append(None)
                return
            ans.append(root1.val)
            inner(root1.left,ans)
            inner(root1.right,ans)
        inner(p,self.ans1)
        inner(q,self.ans2)
        return True if self.ans1 ==self.ans2 else  False
    
    
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
    print(sol.isBalanced(root))
    print(sol.diameterOfBinaryTree(root))
    print(sol.maxPathSum(root))