# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        n-=1
        p=head
        while(p.next!=None):
            c+=1
            p=p.next
        s=c-n
        if s==0:
            head=head.next
            return head
        if c==0:
            head=None
            return head
        p1=head
        p2=head
        for i in range(s-1):
            p1=p1.next
            p2=p2.next
        p2=p2.next
        p1.next=p2.next
        p2=None
        return head