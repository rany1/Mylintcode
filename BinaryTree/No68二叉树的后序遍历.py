"""
Definition of TreeNode:
http://www.lintcode.com/zh-cn/problem/binary-tree-postorder-traversal/
二叉树的后序遍历
给出一棵二叉树，返回其节点值的后序遍历
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
返回 [3,2,1]
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param: root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result=[];
        if root is None:
            return [];
        result=result+self.postorderTraversal(root.left);
       
        result=result+self.postorderTraversal(root.right);
        result.append(root.val);
        return result;
