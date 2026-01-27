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
def deleteNode(self, root, key):
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
            



                    
if __name__=='__main__':
    root = TreeNode(val =4,left =None,right =None)
    right = TreeNode(val =6,left =TreeNode(5),right =None)
    root.right =right
    print(searchBST(root, 6))
    print(insertIntoBST(root,3))
