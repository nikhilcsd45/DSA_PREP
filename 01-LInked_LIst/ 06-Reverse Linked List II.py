# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy

        for _ in range(left-1):
            prev=prev.next

        start=prev.next
        curr=start
        prev2=None
        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev2
            prev2=curr
            curr=temp
        prev.next=prev2
        start.next=curr

        return dummy.next
        
        

        


        