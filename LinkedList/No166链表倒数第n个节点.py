"""
链表倒数第n个节点
http://www.lintcode.com/zh-cn/problem/nth-to-last-node-in-list/
找到单链表倒数第n个节点，保证链表中节点的最少数量为n。
给出链表 3->2->1->5->null和n = 2，返回倒数第二个节点的值1.
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
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        # write your code here
        k=m=head;#两个指针，一个快，一个慢
        index=0;
        while k is not None:
            if n<=index: #当快的执行到 n位置时，慢的开始执行
                m=m.next;
            k=k.next;
            index=index+1;
        return m;
