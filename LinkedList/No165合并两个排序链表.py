"""
合并两个排序链表
http://www.lintcode.com/zh-cn/problem/merge-two-sorted-lists/
将两个排序链表合并为一个新的排序链表
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。
Definition of ListNode

"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        h1=l1;
        h2=l2;

        first=head=None;
        while h1 is not  None or h2 is not None:
            if h1 is None:
                if head is None:
                   first= head=h2;
                else:
                    head.next=h2;
                    head=head.next;
                break;
            if h2 is None:
                if head is None:
                   first= head=h1;
                else:
                    head.next=h1;
                    head=head.next;
                break;
            if h1.val < h2.val:
                if head is None:
                   first= head=h1;
                else:
                    head.next=h1;
                    head=head.next;
                h1=h1.next;
            else:
                if head is None:
                   first= head=h2;
                else:
                    head.next=h2;
                    head=head.next;
                h2=h2.next;
        return first;

