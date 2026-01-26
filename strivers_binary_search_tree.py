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
            
if __name__=='__main__':
    root = TreeNode(val =4,left =None,right =None)
    right = TreeNode(val =6,left =TreeNode(5),right =None)
    root.right =right
    print(searchBST(root, 6))
    print(insertIntoBST(root,3))
