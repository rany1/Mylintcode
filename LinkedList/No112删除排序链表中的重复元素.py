"""
删除排序链表中的重复元素
http://www.lintcode.com/zh-cn/problem/remove-duplicates-from-sorted-list/
给定一个排序链表，删除所有重复的元素每个元素只留下一个。
给出 1->1->2->null，返回 1->2->null

给出 1->1->2->3->3->null，返回 1->2->3->null
Definition of ListNode

"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param: head: head is the head of the linked list
    @return: head of linked list
   -14->-14->-13->-13->-13->
    """
    def deleteDuplicates(self, head):
        # write your code here
        value =None;
        node=prenode=head;
        while node is not None:
            if value is None:
                prenode=node;
                value=node.val;
            else:
                if node.val==value :
                    if node.next is not None:
                        prenode.next=node.next;
                    else:
                        prenode.next=None;
                else:
                    prenode=node;
                    value=node.val;
            node=node.next;
        return head;
