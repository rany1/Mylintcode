"""
Definition of TreeNode:
http://www.lintcode.com/zh-cn/problem/binary-tree-level-order-traversal/
给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）
给一棵二叉树 {3,9,20,#,#,15,7} ：

  3
 / \
9  20
  /  \
 15   7
返回他的分层遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
import Queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        result=[];
        if root is None:
            return [];
        q = Queue.Queue()
        result.append([root.val]);
        q.put(root);
        while not q.empty():
            qArr=[];
            aArr=[];
            while not q.empty():
                node=q.get();
                if node.left is not None:
                    qArr.append(node.left.val);
                    aArr.append(node.left);
                if node.right is not None:
                    qArr.append(node.right.val);
                    aArr.append(node.right);
            if len(qArr):
                result.append(qArr);
            for i in range(0,len(aArr)):
                q.put(aArr[i]);
        return result;
