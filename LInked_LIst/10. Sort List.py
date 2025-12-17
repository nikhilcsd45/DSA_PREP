class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def mergesort(l, r):
            dummy = ListNode(-1)
            tail = dummy
    
            while l and r:
                if l.val < r.val:
                    tail.next = l     
                    l = l.next
                else:
                    tail.next = r      
                    r = r.next
                tail = tail.next

            tail.next = l or r
            return dummy.next

        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)


        return mergesort(left, right)






        
        