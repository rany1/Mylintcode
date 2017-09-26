"""
二叉树的前序遍历
http://www.lintcode.com/zh-cn/problem/binary-tree-preorder-traversal/
给出一棵二叉树 {1,#,2,3},

   1
    \
     2
    /
   3
 返回 [1,2,3].
Definition of TreeNode:

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        result=[];
        if root is None:
            return [];
        result.append(root.val);
        result=result+self.preorderTraversal(root.left);
        result=result+self.preorderTraversal(root.right);
        return result;
