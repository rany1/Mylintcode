"""
http://www.lintcode.com/zh-cn/problem/partition-list/
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。
你应该保留两部分内链表节点原有的相对顺序。
给定链表 1->4->3->2->5->2->null，并且 x=3
返回 1->2->2->4->3->5->null
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        leftTail=left=ListNode(0);
        rightTail= right=ListNode(0);
        node=head;
        while node is not None:
            if node.val>=x:
                leftTail.next=node;
                leftTail=node;
            else:
                rightTail.next=node;
                rightTail=node;
            node=node.next;
        rightTail.next=None;
        leftTail.next=right.next;
        return left.next;
