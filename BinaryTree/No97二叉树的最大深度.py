"""
Definition of TreeNode:
http://www.lintcode.com/zh-cn/problem/maximum-depth-of-binary-tree/
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的距离。
给出一棵如下的二叉树:

  1
 / \ 
2   3
   / \
  4   5
这个二叉树的最大深度为3.
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0;
        deptLeft= self.maxDepth(root.left);
        deptRight=self.maxDepth(root.right);
        if deptLeft>deptRight:
            return deptLeft+1;
        else:
            return deptRight+1;
