"""
Definition of TreeNode:
http://www.lintcode.com/zh-cn/problem/binary-tree-inorder-traversal/
给出一棵二叉树,返回其中序遍历
给出二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [1,3,2].
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result=[];
        if root is None:
            return [];
        result=result+self.inorderTraversal(root.left);
        result.append(root.val);
        result=result+self.inorderTraversal(root.right);
        return result;
