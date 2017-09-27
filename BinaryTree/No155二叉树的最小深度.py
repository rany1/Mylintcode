"""
Definition of TreeNode:
http://www.lintcode.com/zh-cn/problem/minimum-depth-of-binary-tree/
给定一个二叉树，找出其最小深度。

二叉树的最小深度为根节点到最近叶子节点的距离。
Example
给出一棵如下的二叉树:

        1

     /     \ 

   2       3

          /    \

        4      5  

这个二叉树的最小深度为 2
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0;
        depthLeft =self.minDepth(root.left);
        depthRight=self.minDepth(root.right);
        if depthLeft==0:
            return depthRight+1;
        if depthRight==0:
            return depthLeft+1;
        if depthLeft<depthRight:
            return depthLeft+1;
        else:
            return depthRight+1;
