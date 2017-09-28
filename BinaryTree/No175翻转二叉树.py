"""
Definition of TreeNode:
http://www.lintcode.com/zh-cn/problem/invert-binary-tree/
翻转一棵二叉树
Example
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        if root is not None:
            temp=root.left;
            root.left=root.right;
            root.right=temp;
            self.invertBinaryTree(root.left);
            self.invertBinaryTree(root.right);
        
