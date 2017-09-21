
"""
删除链表中倒数第n个节点
http://www.lintcode.com/zh-cn/problem/remove-nth-node-from-end-of-list/
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。
链表中的节点个数大于等于n
给出链表1->2->3->4->5->null和 n = 2.
删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.
Definition of ListNode

"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        k=m=head;#快慢2个指针
        while k is not None:
            if(n<0):
                m=m.next;
            n=n-1;
            k=k.next;
        n.next=n.next.next;
        return head;
