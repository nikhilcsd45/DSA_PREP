class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        
        dummy1=ListNode(-1)
        before=dummy1
        dummy2=ListNode(-1)
        after=dummy2
        while head:
            if head.val<x:
                before.next=head
                before=before.next

            else:
                after.next=head
                after=after.next
            head=head.next
        after.next=None
        before.next=dummy2.next
        return dummy1.next
        


        