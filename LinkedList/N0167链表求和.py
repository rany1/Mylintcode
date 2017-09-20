
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    链表求和
    你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，
    使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。
    样例
给出两个链表 3->1->5->null 和 5->9->2->null，返回 8->0->8->null
    @param: l1: the first list
    @param: l2: the second list
    @return: the sum list of l1 and l2
    """

    def addLists(self, l1, l2):
        # write your code here
        tail=head=None;
        totalSum=0;
        while l1 is not None or l2 is not None:
            if l1 is not None:
                totalSum =totalSum+l1.val;
                l1=l1.next;
            if l2 is not None:
                totalSum=totalSum+l2.val;
                l2=l2.next;
            if head is None:
                head=ListNode(totalSum%10,None);

            else:
                if tail is None:
                    tail=ListNode(totalSum%10,None);
                    head.next=tail;
                else:
                    tail.next=ListNode(totalSum%10,None);
                    tail=tail.next;
            totalSum=int(totalSum/10);
        if totalSum==1:
            tail.next=ListNode(1,None);
        return head;
