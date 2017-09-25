class Solution:
    """
    两两交换链表中的节点
    http://www.lintcode.com/zh-cn/problem/swap-nodes-in-pairs/
    给一个链表，两两交换其中的节点，然后返回交换后的链表。
    给出 1->2->3->4, 你应该返回的链表是 2->1->4->3。
    @param: head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        if head is None or head.next is None:
            return head;

        newhead=pre=ListNode(0);
        tail=None;
        index=0;
        while head is not None:
            index=index+1;
            if index==1:
                pre=head;
            elif index==2:#head和pre插入新的链表中，先插head
                index=0;
                if tail is None:
                    newhead=ListNode(head.val);
                    tail=ListNode(pre.val);
                    newhead.next=tail;
                else:
                    tail.next=ListNode(head.val);
                    tail.next.next=ListNode(pre.val);
                    tail=tail.next.next;
            head=head.next;
        if index==1:#奇数个时，需要添加最后一个
            tail.next=pre;
        return newhead;
