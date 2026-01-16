
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
    def isSameTree_2(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def inner(root1,root2):
            if root1 is None and root2 is None:
                return True
            if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
                return False
            if root1.val !=root2.val:
                return False
            
            l=inner(root1.left,root2.left)
            r =inner(root1.right,root2.right)
            if not r or not l:
                return False
            else:
                return True
        return inner(p,q)
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        qu=[]
        ans =[]
        flag =False
        if root is None:
            return qu
        qu.append(root)
        while qu:
            x = len(qu)
            temp =[]
            for i in range(x):
                temp.append(qu[0].val)
                if qu[0].left is not None:
                    qu.append(qu[0].left)
                if qu[0].right is not None:
                    qu.append(qu[0].right)
                qu.pop(0)
            
            if flag:
                ans.append(temp[::-1])
                flag =False
            else:
                ans.append(temp)
                flag = True
        return ans
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        qu =[]
        qu.append(root)
        while qu:
            x = len(qu)
            temp =[]
            for i in range(x):
                
                if qu[0].left is not None:
                    temp.append(qu[0].left.val)
                    qu.append(qu[0].left)
                else:
                    temp.append(None)
                if qu[0].right is not None:
                    temp.append(qu[0].right.val)
                    qu.append(qu[0].right)
                else:
                    temp.append(None)
                qu.pop(0)
            if temp !=temp[::-1]:
                return False
        return True
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans =[]
        if root is None:
            return []
        qu =[root]
        while qu:
            x = len(qu)
            for i in range(x):
                if i==x-1:
                    ans.append(qu[0].val)
                if qu[0].left is not None:
                    qu.append(qu[0].left)
                if qu[0].right is not None:
                    qu.append(qu[0].right)
                qu.pop(0)
        return ans

    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        max_w =1
        qu ={0:root}
        while qu:
            temp ={}
            for item in qu.items():
                if item[1].left is not None:
                    temp[item[0]*2]=item[1].left
                if item[1].right is not None:
                    temp[item[0]*2+1]=item[1].right
            if temp:
                max_w =max(max_w,max(temp)-min(temp)+1)
            qu=temp
        return max_w
    ##leetcode: 114. Flatten Binary Tree to Linked List
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        ans =[]
        def inner(root1):
            if root1 is None:
                return
            ans.append(root1.val)
            inner(root1.left)
            inner(root1.right)
        inner(root)
        temp = root
        for i in range(1,len(ans)):
            temp.left =None
            temp.right = TreeNode(ans[i])
            temp=temp.right
        return root
    ###Leetcode:863. All Nodes Distance K in Binary Tree
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        self.parentmap ={}
        qu =[root]
        self.targetNode =None
        while qu:
            l = len(qu)
            for i in range(l):
                
                if qu[0].val ==target.val:
                    self.targetNode =qu[0]
                if qu[0].left is not None:
                    qu.append(qu[0].left)
                    self.parentmap[qu[0].left]=qu[0]
                if qu[0].right is not None:
                    qu.append(qu[0].right)
                    self.parentmap[qu[0].right]=qu[0]
                qu.pop(0)
        qu1=[self.targetNode]
        visited = [self.targetNode.val]
        c_level =0
        if k ==c_level:
            return [self.targetNode.val]
        while qu1:
            l = len(qu1)
            for i in range(l):
                if qu1[0].left is not None and qu1[0].left.val not in visited:
                    qu1.append(qu1[0].left)
                    visited.append(qu1[0].left.val)
                if qu1[0].right is not None and qu1[0].right.val not in visited:
                    qu1.append(qu1[0].right)
                    visited.append(qu1[0].right.val)
                if qu1[0] !=root and self.parentmap[qu1[0]].val not in visited:
                    qu1.append(self.parentmap[qu1[0]])
                    visited.append(self.parentmap[qu1[0]].val)
                qu1.pop(0)
            
            c_level +=1
            if c_level ==k:
                temp =[]
                for q in qu1:
                    temp.append(q.val)
                return temp
        return qu
    #Leetcode:222. Count Complete Tree Nodes
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        co =0
        if root is None:
            return co
        co =1
        qu =[root]
        while qu:
            l = len(qu)
            c_temp =0
            for i in range(l):
                if qu[0].left is not None:
                    qu.append(qu[0].left)
                    c_temp+=1
                else:
                    qu.pop(0)
                    break
                if qu[0].right is not None:
                    qu.append(qu[0].right)
                    c_temp+=1
                else:
                    qu.pop(0)
                    break
                qu.pop(0)
                
            co+=c_temp
            if c_temp<2*l:
                break
        return co
    '''  
    Problem Statement: Given a Binary Tree and a reference to a root belonging to it. Return the path from the root node to the given leaf node.
Note: No two nodes in the tree have the same data value and it is assured that the given node is present and a path always exists.
    '''
    def root2node(self,root,nodeval):
        self.ans =[]
        def inner(root1,new):
            if root1 is None:
                return False
            if root1.val ==nodeval:
                new.append(root1.val)
                self.ans =new[:]
                return True
            new.append(root1.val)
            f_l=inner(root1.left,new)
            f_r =inner(root1.right,new)
            if f_l or f_r:
                return True
            new.pop()
            return False
            
        inner(root,[])
        return self.ans
            

    #  leetcode:236. Lowest Common Ancestor of a Binary Tree     
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.parent ={}
        target ={}
        if root is None:
            return root
        qu =[root]
        level =0
        while qu:
            l = len(qu)
            for i in range(l):
                if qu[0]==q or qu[0] ==p:
                    target[qu[0]]=level
                if qu[0].left is not None:
                    qu.append(qu[0].left)
                    self.parent[qu[0].left]=qu[0]
                if qu[0].right is not None:
                    qu.append(qu[0].right)
                    self.parent[qu[0].right]=qu[0]
                qu.pop(0)
            level+=1
        while len(target)>1:
            temp =max(target.items(),key =lambda item: item[1])
            target.pop(temp[0])
            target[self.parent[temp[0]]]=temp[1]-1
        return target.keys()[0]
        
                

        

        
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
    print(sol.zigzagLevelOrder(root))
    print(sol.isSymmetric(root))
    print(sol.rightSideView(root))
    print(sol.widthOfBinaryTree(root))
    print(sol.flatten(root))
    print(sol.root2node(root,3))