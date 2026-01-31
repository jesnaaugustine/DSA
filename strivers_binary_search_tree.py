class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    """
    :type root: Optional[TreeNode]
    :type val: int
    :rtype: Optional[TreeNode]
    """
    temp =root
    while temp is not None:
        if temp.val ==val:
            return temp
        if val<temp.val:
            temp = temp.left
        else:
            temp = temp.right
    return temp
def insertIntoBST(root, val):
    """
    :type root: Optional[TreeNode]
    :type val: int
    :rtype: Optional[TreeNode]
    """
    temp =root
    parent = None
    if root is None:
        return TreeNode(val)
    while temp:
        parent = temp
        if temp.val<val:
            temp=temp.right
        elif temp.val>val:
            temp =temp.left
    if parent.val<val:
        parent.right = TreeNode(val)
    else:
        parent.left = TreeNode(val)
    return root
def deleteNode(root, key):
    """
    :type root: Optional[TreeNode]
    :type key: int
    :rtype: Optional[TreeNode]
    """
    temp = root
    parent =None
    left_off=None
    while temp is not None:
        if temp.val ==key:
            if parent:
                parent.left = temp.left
                left_off = temp.right
                temp = temp.left
            else:
                root = temp.left
                left_off =temp.right
                temp = temp.left
            break
        elif temp.val>key:
            parent = temp
            temp = temp.left
            
        else:
            parent = temp
            temp = temp.right
            
    while temp:
        parent = temp
        temp = temp.right
        
    if left_off:
        parent.right = left_off
    return root
            
def kthSmallest(root, k):
    """
    :type root: Optional[TreeNode]
    :type k: int
    :rtype: int
    """
    arr =[]
    def inner(root_in):
        if root_in is None:
            return
        if len(arr)>=k:
            return
        inner(root_in.left)
        arr.append(root_in.val)
        inner(root_in.right)
            
    inner(root)
    print(arr)
    return arr[k-1]

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    temp = root
    while temp:
        if temp.val>p.val and temp.val>q.val:
            temp = temp.left
        elif temp.val<p.val and temp.val<q.val:
            temp = temp.right
        else:
            return temp
#98. Validate Binary Search Tree

def isValidBST(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    ans =[]
    def inner(root_in):
        if root_in is None:
            return 
        inner(root_in.left)
        ans.append(root_in.val)
        inner(root_in.right)
    inner(root)
    for i in range(1,len(ans)):
        if ans[i-1]>=ans[i]:
            return False
    return True
def isValidBST_1(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    def inner(root_in,min_r,max_r):
        if root_in is None:
            return True
        if root_in.val<=min_r or root_in.val>=max_r:
            return False
        lf = inner(root_in.left,min_r,root_in.val)
        rg =inner(root_in.right,root_in.val,max_r)
        if lf and rg:
            return True
        else:
            return False
    return inner(root,float('-inf'),float('inf'))    
 
def bstFromPreorder( preorder):
    """
    :type preorder: List[int]
    :rtype: Optional[TreeNode]
    """
    idx =0
    def inner(preorder,ma_rang):
        global idx
        if idx >=len(preorder):
            return
        if preorder[idx]>=ma_rang:
            return
        val =preorder[idx]
        root = TreeNode(val)
        idx = idx+1
        print(idx)
        root.left = inner(preorder,val)
        root.right = inner(preorder,ma_rang)
        return root
    return inner(preorder,float('inf'))
                
if __name__=='__main__':
    root = TreeNode(val =4,left =None,right =None)
    right = TreeNode(val =6,left =TreeNode(5),right =None)
    root.right =right
    print(searchBST(root, 6))
    print(insertIntoBST(root,3))
    preorder = [8,5,1,7,10,12]
    print(bstFromPreorder(preorder))
