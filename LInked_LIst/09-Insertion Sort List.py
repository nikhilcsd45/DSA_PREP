class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head   # 0 or 1 node => already sorted

        # Dummy node as start of sorted list
        dummy = ListNode(float("-inf"))

        curr = head
        while curr:
            next_node=curr.next
            prev=dummy
            while prev.next and prev.next.val<curr.val:
                prev=prev.next
            
            curr.next=prev.next
            prev.next=curr


            curr=next_node
            

        return dummy.next


    

