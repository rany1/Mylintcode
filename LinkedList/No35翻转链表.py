"""
翻转一个链表
给出一个链表1->2->3->4->5->null，这个翻转后的链表为3->2->1->null
http://www.lintcode.com/zh-cn/problem/reverse-linked-list/
Definition of ListNode


"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    1->2->3->4->5->null，
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head is not None:
            preNode=head;
            currentNode =head.next;
            while currentNode is not None and currentNode.next is not None:
                nextNode=currentNode.next;
                currentNode.next=preNode;
                preNode=currentNode;
                currentNode=nextNode;
            currentNode.next=preNode;
            head.next=None;
            return currentNode;
